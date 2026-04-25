#!/usr/bin/env python3
"""
Extract 2017 posts from WordPress XML export with full metadata and markdown content.
"""

import xml.etree.ElementTree as ET
import os
import re
import json
from datetime import datetime
from html.parser import HTMLParser
import html

TARGET_SLUGS = {
    "exploring-microsoft-security-update-information-with-powershell",
    "powershell-script-update-poshmodule",
    "powershell-script-get-batterychargestatus",
    "how-to-check-if-control-flow-guard-is-enabled",
    "creating-and-managing-azure-storage-tables-with-powershell",
    "retrieving-office-365-roadmap-information-with-powershell",
    "office-365-centralized-deployment-service",
    "configmgr-client-policy-settings-get-cmclientpolicysettings",
    "deploying-configmgr-current-branch-in-azure-dev-test-lab",
    "how-to-link-an-oms-workspace-with-an-azure-automation-account",
    "oms-log-analytics-http-data-collector-api-work-notes",
    "select-myazurermsubscription",
    "download-and-install-the-windows-assessment-and-deployment-kit-with-powershell",
    "retrieve-azure-virtual-machine-size-information-with-powershell",
}

TARGET_POST_IDS = {
    "6973",
}

FALLBACK_POST_METADATA = {
    "6973": {
        "title": "Untitled Draft 6973",
        "slug": "untitled-draft-6973",
        "description": "Imported placeholder draft from the WordPress export.",
    }
}

REMOTE_IMAGE_ONLY_SLUGS = {
    "exploring-microsoft-security-update-information-with-powershell",
    "deploying-configmgr-current-branch-in-azure-dev-test-lab",
    "how-to-link-an-oms-workspace-with-an-azure-automation-account",
    "oms-log-analytics-http-data-collector-api-work-notes",
    "retrieve-azure-virtual-machine-size-information-with-powershell",
    "select-myazurermsubscription",
}


class HTMLToMarkdownConverter(HTMLParser):
    """Convert HTML to Markdown"""

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
        text = html.unescape(data)
        self.text.append(text)

    def get_markdown(self):
        result = ''.join(self.text).strip()
        result = re.sub(r'\n{3,}', '\n\n', result)
        return result


def extract_images_from_html(html_content):
    """Extract unique image filenames from HTML content (preserving order)."""
    images = []
    seen = set()
    pattern = r'src=["\']([^"\']*)["\']'
    for match in re.findall(pattern, html_content):
        filename = os.path.basename(match)
        if filename and filename not in seen:
            if re.search(r'\.(png|jpg|jpeg|gif|webp|svg|bmp)(\?.*)?$', filename, re.IGNORECASE):
                seen.add(filename)
                images.append(filename)
    return images


def convert_linked_local_images_to_remote(markdown_content):
    """Replace linked local thumbnails with direct remote image links."""
    pattern = re.compile(
        r'\[\s*!\[([^\]]*)\]\(images/[^)]+\)\s*\]\((https?://[^)]+)\)',
        re.MULTILINE,
    )
    return pattern.sub(lambda match: f'![{match.group(1)}]({match.group(2)})', markdown_content)


def parse_post_datetime(post_date_gmt, post_date_local, fallback_year):
    """Parse post dates from WXR, falling back from GMT to local time."""
    for value in (post_date_gmt, post_date_local):
        if not value or value == '0000-00-00 00:00:00':
            continue
        try:
            return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            continue

    print(f"  WARNING: Could not parse dates GMT='{post_date_gmt}' local='{post_date_local}'")
    return datetime(fallback_year, 1, 1)


def to_iso_datetime(post_date_gmt, post_date_local, dt):
    """Format a WXR date as ISO 8601 UTC-like output for front matter."""
    source = post_date_gmt
    if not source or source == '0000-00-00 00:00:00':
        source = post_date_local
    if source and source != '0000-00-00 00:00:00':
        return source.replace(' ', 'T') + 'Z'
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')


def parse_wordpress_xml(xml_file):
    """Parse WordPress XML export and return target 2017 posts."""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    namespaces = {
        'wp': 'http://wordpress.org/export/1.2/',
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'dc': 'http://purl.org/dc/elements/1.1/',
    }

    posts = []

    for item in root.findall('.//item'):
        post_type_elem = item.find('wp:post_type', namespaces)
        if post_type_elem is None or post_type_elem.text != 'post':
            continue

        slug_elem = item.find('wp:post_name', namespaces)
        slug = slug_elem.text if slug_elem is not None and slug_elem.text is not None else ''

        post_id_elem = item.find('wp:post_id', namespaces)
        post_id = post_id_elem.text if post_id_elem is not None and post_id_elem.text is not None else ''

        if slug not in TARGET_SLUGS and post_id not in TARGET_POST_IDS:
            continue

        title_elem = item.find('title')
        title = title_elem.text if title_elem is not None and title_elem.text is not None else ''

        post_date_gmt_elem = item.find('wp:post_date_gmt', namespaces)
        post_date_gmt = post_date_gmt_elem.text if post_date_gmt_elem is not None else ''
        post_date_local_elem = item.find('wp:post_date', namespaces)
        post_date_local = post_date_local_elem.text if post_date_local_elem is not None else ''

        dt = parse_post_datetime(post_date_gmt, post_date_local, 2017)
        year = dt.year
        month = dt.month

        fallback = FALLBACK_POST_METADATA.get(post_id, {})
        if not slug:
            slug = fallback.get('slug', f'untitled-post-{post_id}')
        if not title:
            title = fallback.get('title', f'Untitled Post {post_id}')

        author_elem = item.find('dc:creator', namespaces)
        author = author_elem.text if author_elem is not None else ''

        content_encoded_elem = item.find('content:encoded', namespaces)
        html_content = content_encoded_elem.text if content_encoded_elem is not None else ''

        tags = []
        categories = []
        for category in item.findall('category'):
            domain = category.get('domain', '')
            nicename = category.get('nicename', '')
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
            print(f"  WARNING: HTML→MD conversion failed for '{slug}': {exc}")
            markdown_content = html_content

        if slug in REMOTE_IMAGE_ONLY_SLUGS:
            markdown_content = convert_linked_local_images_to_remote(markdown_content)
            images = []
            hero_image = ''

        desc_plain = re.sub(r'\s+', ' ', markdown_content.replace('\n', ' ')).strip()
        description = desc_plain[:150]
        if len(desc_plain) > 150:
            description += '...'
        if not description:
            description = fallback.get('description', '')

        date_iso = to_iso_datetime(post_date_gmt, post_date_local, dt)

        posts.append({
            'title': title,
            'date': date_iso,
            'slug': slug,
            'description': description,
            'year': year,
            'month': month,
            'author': author,
            'post_id': post_id,
            'tags': tags,
            'categories': categories,
            'image_list': images,
            'hero_image': hero_image,
            'html_content': html_content,
            'markdown_content': markdown_content,
        })

    return posts


def save_post_body(year, month, slug, markdown_content):
    """Save post markdown body to scripts/tmp/body-YYYY-MM-slug.md"""
    output_dir = "C:\\Dev\\Alex\\blog\\AnythingAboutITBlog\\scripts\\tmp"
    os.makedirs(output_dir, exist_ok=True)
    filename = f"body-{year}-{month:02d}-{slug}.md"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    return filepath


def main():
    xml_file = "C:\\Dev\\Alex\\NewBlog\\anythingaboutit.WordPress.2026-04-11.xml"

    print("Parsing WordPress XML export for 2017 posts...")
    posts = parse_wordpress_xml(xml_file)

    if not posts:
        print("ERROR: No matching posts found. Check targets or XML path.")
        return

    target_count = len(TARGET_SLUGS) + len(TARGET_POST_IDS)
    print(f"Found {len(posts)} of {target_count} target posts")

    found_slugs = {p['slug'] for p in posts if p['post_id'] not in TARGET_POST_IDS}
    missing = TARGET_SLUGS - found_slugs
    if missing:
        print(f"\nWARNING: {len(missing)} slugs not found in XML:")
        for s in sorted(missing):
            print(f"  - {s}")

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

    output_json = "C:\\Dev\\Alex\\blog\\AnythingAboutITBlog\\scripts\\extracted_2017_posts.json"
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n[OK] Extracted {len(results)} posts")
    print(f"[OK] JSON saved to: {output_json}")


if __name__ == '__main__':
    main()