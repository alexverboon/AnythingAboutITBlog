#!/usr/bin/env python3
"""
Extract 2016 posts from WordPress XML export with full metadata and markdown content.
"""

import xml.etree.ElementTree as ET
import os
import re
import json
from datetime import datetime
from html.parser import HTMLParser
import html

TARGET_SLUGS = {
    "powershell-script-get-msoluserinformation",
    "powershell-script-get-msolrolememberdetails",
    "powershell-script-get-winbuildinfo",
    "windows-10-upgrade-analytics-notes-and-powershell-snippets",
    "clean-up-unused-azure-resources-with-powershell",
    "powershell-script-to-run-the-windows-app-certification-kit",
    "tooltip-iedigest",
    "office-365-powershell-script-to-retrieve-accountsku-license-information",
    "powershell-script-get-iscmssecbulletininfo",
    "creating-a-virtual-network-using-azure-resource-manager-part-2",
    "creating-a-virtual-network-using-azure-resource-manager-part-1",
    "a-little-helper-script-for-the-azure-set-azurermvmsourceimage-cmdlet",
    "the-grouppolicy-xtended-powershell-module",
    "tooltip-policy-analzyer",
}

TARGET_POST_IDS = {
    "6935",
}

FALLBACK_POST_METADATA = {
    "6935": {
        "title": "Microsoft Operations Management Suite - Notes",
        "slug": "microsoft-operations-management-suite-notes",
        "description": "Notes on Microsoft Operations Management Suite.",
    }
}

# Slugs whose local thumbnail files are absent — rewrite to remote image links instead
REMOTE_IMAGE_ONLY_SLUGS: set = set()


class HTMLToMarkdownConverter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.in_strong = False
        self.in_em = False
        self.in_code = False
        self.in_pre = False
        self.in_list = False
        self._pending_href = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'p':
            pass
        elif tag in ('strong', 'b'):
            self.text.append('**')
            self.in_strong = True
        elif tag in ('em', 'i'):
            self.text.append('*')
            self.in_em = True
        elif tag == 'code':
            if not self.in_pre:
                self.text.append('`')
            self.in_code = True
        elif tag == 'pre':
            self.text.append('\n```\n')
            self.in_pre = True
        elif tag == 'a':
            self._pending_href = attrs_dict.get('href', '#')
            self.text.append('[')
        elif tag == 'img':
            src = attrs_dict.get('src', '')
            alt = attrs_dict.get('alt', 'image')
            filename = os.path.basename(src) if src else src
            self.text.append(f'\n![{alt}](images/{filename})\n')
        elif tag == 'br':
            self.text.append('\n')
        elif tag == 'h1':
            self.text.append('\n# ')
        elif tag == 'h2':
            self.text.append('\n## ')
        elif tag == 'h3':
            self.text.append('\n### ')
        elif tag == 'h4':
            self.text.append('\n#### ')
        elif tag in ('ul', 'ol'):
            self.in_list = True
        elif tag == 'li':
            self.text.append('\n- ')
        elif tag == 'blockquote':
            self.text.append('\n> ')

    def handle_endtag(self, tag):
        if tag == 'p':
            self.text.append('\n\n')
        elif tag in ('strong', 'b'):
            self.text.append('**')
            self.in_strong = False
        elif tag in ('em', 'i'):
            self.text.append('*')
            self.in_em = False
        elif tag == 'code':
            if not self.in_pre:
                self.text.append('`')
            self.in_code = False
        elif tag == 'pre':
            self.text.append('\n```\n')
            self.in_pre = False
        elif tag == 'a':
            href = self._pending_href or '#'
            self.text.append(f']({href})')
            self._pending_href = None
        elif tag in ('h1', 'h2', 'h3', 'h4'):
            self.text.append('\n\n')
        elif tag in ('ul', 'ol'):
            self.text.append('\n\n')
            self.in_list = False
        elif tag == 'blockquote':
            self.text.append('\n\n')

    def handle_data(self, data):
        self.text.append(html.unescape(data))

    def get_markdown(self):
        result = ''.join(self.text).strip()
        return re.sub(r'\n{3,}', '\n\n', result)


def extract_images_from_html(html_content):
    images, seen = [], set()
    for match in re.findall(r'src=["\']([^"\']*)["\']', html_content):
        filename = os.path.basename(match)
        if filename and filename not in seen and re.search(r'\.(png|jpg|jpeg|gif|webp|svg|bmp)(\?.*)?$', filename, re.IGNORECASE):
            seen.add(filename)
            images.append(filename)
    return images


def convert_linked_local_images_to_remote(markdown_content):
    pattern = re.compile(
        r'\[\s*!\[([^\]]*)\]\(images/[^)]+\)\s*\]\((https?://[^)]+)\)',
        re.MULTILINE,
    )
    return pattern.sub(lambda m: f'![{m.group(1)}]({m.group(2)})', markdown_content)


def parse_post_datetime(gmt, local, fallback_year):
    for val in (gmt, local):
        if not val or val == '0000-00-00 00:00:00':
            continue
        try:
            return datetime.strptime(val, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            continue
    print(f"  WARNING: Could not parse dates gmt='{gmt}' local='{local}'")
    return datetime(fallback_year, 1, 1)


def to_iso(gmt, local, dt):
    src = gmt if (gmt and gmt != '0000-00-00 00:00:00') else local
    if src and src != '0000-00-00 00:00:00':
        return src.replace(' ', 'T') + 'Z'
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')


def parse_wordpress_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    ns = {
        'wp': 'http://wordpress.org/export/1.2/',
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'dc': 'http://purl.org/dc/elements/1.1/',
    }

    posts = []
    for item in root.findall('.//item'):
        pt = item.find('wp:post_type', ns)
        if pt is None or pt.text != 'post':
            continue

        slug_el = item.find('wp:post_name', ns)
        slug = (slug_el.text or '') if slug_el is not None else ''

        pid_el = item.find('wp:post_id', ns)
        post_id = (pid_el.text or '') if pid_el is not None else ''

        gmt_el = item.find('wp:post_date_gmt', ns)
        gmt = (gmt_el.text or '') if gmt_el is not None else ''
        local_el = item.find('wp:post_date', ns)
        local = (local_el.text or '') if local_el is not None else ''

        dt = parse_post_datetime(gmt, local, 2016)
        if dt.year != 2016:
            continue

        # Must match slug or explicit post_id list
        if slug not in TARGET_SLUGS and post_id not in TARGET_POST_IDS:
            continue

        title_el = item.find('title')
        title = (title_el.text or '') if title_el is not None else ''

        fallback = FALLBACK_POST_METADATA.get(post_id, {})
        if not slug:
            slug = fallback.get('slug', f'untitled-post-{post_id}')
        if not title:
            title = fallback.get('title', f'Untitled Post {post_id}')

        author_el = item.find('dc:creator', ns)
        author = (author_el.text or '') if author_el is not None else ''

        content_el = item.find('content:encoded', ns)
        html_content = (content_el.text or '') if content_el is not None else ''

        tags, categories = [], []
        for cat in item.findall('category'):
            domain = cat.get('domain', '')
            nicename = cat.get('nicename', '')
            if domain == 'post_tag':
                tags.append(nicename)
            elif domain == 'category' and nicename.lower() != 'uncategorized':
                categories.append(nicename)

        images = extract_images_from_html(html_content)
        hero_image = images[0] if images else ''

        converter = HTMLToMarkdownConverter()
        try:
            converter.feed(html_content)
            markdown_content = converter.get_markdown()
        except Exception as exc:
            print(f"  WARNING: conversion failed for '{slug}': {exc}")
            markdown_content = html_content

        if slug in REMOTE_IMAGE_ONLY_SLUGS:
            markdown_content = convert_linked_local_images_to_remote(markdown_content)
            images = []
            hero_image = ''

        desc_plain = re.sub(r'\s+', ' ', markdown_content.replace('\n', ' ')).strip()
        description = desc_plain[:150] + ('...' if len(desc_plain) > 150 else '')
        if not description:
            description = fallback.get('description', '')

        posts.append({
            'title': title,
            'date': to_iso(gmt, local, dt),
            'slug': slug,
            'description': description,
            'year': dt.year,
            'month': dt.month,
            'author': author,
            'post_id': post_id,
            'tags': tags,
            'categories': categories,
            'image_list': images,
            'hero_image': hero_image,
            'markdown_content': markdown_content,
        })

    return posts


def save_post_body(year, month, slug, markdown_content):
    output_dir = "C:\\Dev\\Alex\\blog\\AnythingAboutITBlog\\scripts\\tmp"
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, f"body-{year}-{month:02d}-{slug}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    return filepath


def main():
    xml_file = "C:\\Dev\\Alex\\NewBlog\\anythingaboutit.WordPress.2026-04-11.xml"
    print("Parsing WordPress XML export for 2016 posts...")
    posts = parse_wordpress_xml(xml_file)

    if not posts:
        print("ERROR: No matching posts found.")
        return

    print(f"Found {len(posts)} posts")
    results = []
    for post in sorted(posts, key=lambda p: p['date'], reverse=True):
        print(f"\nProcessing: {post['title']}")
        print(f"  Slug  : {post['slug']}")
        print(f"  Date  : {post['date']}")
        print(f"  Images: {len(post['image_list'])}")
        body_filepath = save_post_body(post['year'], post['month'], post['slug'], post['markdown_content'])
        print(f"  Saved : {body_filepath}")
        results.append({
            'title': post['title'],
            'date': post['date'],
            'slug': post['slug'],
            'description': post['description'],
            'year': post['year'],
            'month': f"{post['month']:02d}",
            'author': post['author'],
            'post_id': post['post_id'],
            'tags': post['tags'],
            'categories': post['categories'],
            'image_list': post['image_list'],
            'hero_image': post['hero_image'],
            'body_file_path': body_filepath,
        })

    output_json = "C:\\Dev\\Alex\\blog\\AnythingAboutITBlog\\scripts\\extracted_2016_posts.json"
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\n[OK] Extracted {len(results)} posts -> {output_json}")


if __name__ == '__main__':
    main()
