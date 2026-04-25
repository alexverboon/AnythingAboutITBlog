#!/usr/bin/env python3
"""
Extract 2019 posts from WordPress XML export with full metadata and markdown content.
"""

import xml.etree.ElementTree as ET
import os
import re
import json
from datetime import datetime
from html.parser import HTMLParser
import html

# Target posts: slug only (year/month resolved from XML)
TARGET_SLUGS = {
    "powershell-7-group-policy-settings-and-eventlogs",
    "setting-up-kali-in-windows-10-wsl-2-0",
    "microsoft-defender-advanced-threat-protection-respond-actions-events",
    "how-to-identify-orphan-group-policy-content-within-the-sysvol-folder",
    "how-to-generate-a-monthly-defender-atp-threat-and-vulnerability-report",
    "windows-defender-more-than-just-antivirus-part-2",
    "microsoft-defender-atp-advanced-hunting-whos-logging-on-with-local-admin-rights",
    "windows-defender-more-than-just-antivirus-part-1",
    "importing-gpo-security-baselines-with-powershell",
    "extract-configmgr-script-status-results-with-powershell",
    "how-to-accelerate-your-microsoft-defender-atp-evaluation",
    "configmgr-cmpivot-the-powershell-script-the-events",
    "monitoring-windows-defender-cloud-protection-service-connectivity-with-configmgr",
    "testing-windows-defender-maps-connectivity-with-powershell",
    "the-case-of-running-the-device-and-credential-guard-hardware-readiness-tool-and-unknown-architecture",
    "managing-role-based-access-rbac-for-microsoft-defender-advanced-threat-protection",
    "exploring-microsoft-cloud-app-security-with-powershell-part1",
    "retrieving-windows-defender-exploit-guard-windows-event-logs-with-powershell",
    "how-configure-splunk-to-pull-windows-defender-atp-alerts",
    "configuring-windows-defender-credential-guard-with-configmgr",
    "windows-7-hybrid-join-and-mfa-ramblings",
    "how-to-enable-dkim-in-office-365",
    "how-to-manage-laps-debuglogging-with-powershell",
    "how-to-monitor-your-azure-ad-emergency-account-with-cloud-app-security",
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
            pass  # newlines added on end
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
            # Skip obviously non-image filenames
            if re.search(r'\.(png|jpg|jpeg|gif|webp|svg|bmp)(\?.*)?$', filename, re.IGNORECASE):
                seen.add(filename)
                images.append(filename)
    return images


def parse_wordpress_xml(xml_file):
    """Parse WordPress XML export and return target 2019 posts."""
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
        slug = slug_elem.text if slug_elem is not None else ''

        if slug not in TARGET_SLUGS:
            continue

        status_elem = item.find('wp:status', namespaces)
        # Accept publish or future; skip drafts
        status = status_elem.text if status_elem is not None else ''
        if status not in ('publish', 'future', 'private'):
            pass  # still include – some exports mark as 'publish'

        title_elem = item.find('title')
        title = title_elem.text if title_elem is not None else ''

        post_date_gmt_elem = item.find('wp:post_date_gmt', namespaces)
        post_date_gmt = post_date_gmt_elem.text if post_date_gmt_elem is not None else ''

        try:
            dt = datetime.fromisoformat(post_date_gmt)
            year = dt.year
            month = dt.month
        except Exception:
            try:
                dt = datetime.strptime(post_date_gmt, '%Y-%m-%d %H:%M:%S')
                year = dt.year
                month = dt.month
            except Exception:
                print(f"  WARNING: Could not parse date '{post_date_gmt}' for slug '{slug}'")
                year = 2019
                month = 1

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

        # Description: first ~150 chars of plain text
        desc_plain = re.sub(r'\s+', ' ', markdown_content.replace('\n', ' ')).strip()
        description = desc_plain[:150]
        if len(desc_plain) > 150:
            description += '...'

        # ISO 8601 UTC date
        date_iso = post_date_gmt.replace(' ', 'T') + 'Z' if post_date_gmt and 'T' not in post_date_gmt else post_date_gmt

        posts.append({
            'title': title,
            'date': date_iso,
            'slug': slug,
            'description': description,
            'year': year,
            'month': month,
            'author': author,
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

    print("Parsing WordPress XML export for 2019 posts...")
    posts = parse_wordpress_xml(xml_file)

    if not posts:
        print("ERROR: No matching posts found. Check slugs or XML path.")
        return

    print(f"Found {len(posts)} of {len(TARGET_SLUGS)} target posts")

    found_slugs = {p['slug'] for p in posts}
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
            'tags': post['tags'],
            'categories': post['categories'],
            'image_list': post['image_list'],
            'hero_image': post['hero_image'],
            'body_file_path': body_filepath,
        })

    output_json = "C:\\Dev\\Alex\\blog\\AnythingAboutITBlog\\scripts\\extracted_2019_posts.json"
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n[OK] Extracted {len(results)} posts")
    print(f"[OK] JSON saved to: {output_json}")
    print("\n--- JSON preview ---")
    for r in results:
        print(json.dumps({k: v for k, v in r.items() if k != 'html_content'}, indent=2))


if __name__ == '__main__':
    main()
