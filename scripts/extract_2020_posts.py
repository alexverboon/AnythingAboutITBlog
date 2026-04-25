#!/usr/bin/env python3
"""
Extract 2020 posts from WordPress XML export with full metadata and markdown content.
"""

import xml.etree.ElementTree as ET
import os
import re
import json
from datetime import datetime
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import html

# Target posts: (year, month, slug)
TARGET_POSTS = [
    (2020, 11, "preparing-my-application-guard-for-office-test-lab"),
    (2020, 10, "monitoring-service-principal-sign-ins-with-azuread-and-azure-sentinel"),
    (2020, 9, "mtp-advanced-hunting-public-free-e-mail-services"),
    (2020, 9, "hunting-for-local-group-membership-changes"),
    (2020, 7, "generating-advanced-hunting-queries-with-powershell"),
    (2020, 6, "defender-atp-advanced-hunting-with-ti-from-urlhaus"),
    (2020, 6, "managing-time-zone-and-date-formats-in-microsoft-defender-security-center"),
    (2020, 6, "advance-your-microsoft-defender-atp-hunting-skills-using-the-atomic-execution-framework"),
    (2020, 5, "meet-the-new-microsoft-defender-atp-evaluation-lab"),
    (2020, 5, "windows-10-2004-what-is-new-in-the-windows-security-app"),
    (2020, 4, "how-to-create-your-defender-atp-admin-audit-log-dashboard"),
    (2020, 3, "how-to-deploy-your-jump-host-in-azure"),
    (2020, 1, "user-spam-phish-submissions-configuration-in-office-365-part-1"),
    (2020, 1, "microsoft-threat-protection-using-advanced-hunting-to-see-whats-going-on-with-your-mail"),
]

class HTMLToMarkdownConverter(HTMLParser):
    """Convert HTML to Markdown"""
    def __init__(self):
        super().__init__()
        self.text = []
        self.in_paragraph = False
        self.in_strong = False
        self.in_em = False
        self.in_code = False
        self.in_pre = False
        self.in_list = False
        self.list_items = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'p':
            self.in_paragraph = True
        elif tag == 'strong' or tag == 'b':
            self.text.append('**')
            self.in_strong = True
        elif tag == 'em' or tag == 'i':
            self.text.append('*')
            self.in_em = True
        elif tag == 'code':
            self.text.append('`')
            self.in_code = True
        elif tag == 'pre':
            self.text.append('```\n')
            self.in_pre = True
        elif tag == 'a':
            href = attrs_dict.get('href', '#')
            self.text.append('[')
        elif tag == 'img':
            src = attrs_dict.get('src', '')
            alt = attrs_dict.get('alt', 'image')
            self.text.append(f'![{alt}]({src})')
        elif tag == 'br':
            self.text.append('\n')
        elif tag == 'h1':
            self.text.append('\n# ')
        elif tag == 'h2':
            self.text.append('\n## ')
        elif tag == 'h3':
            self.text.append('\n### ')
        elif tag == 'ul':
            self.in_list = True
        elif tag == 'li':
            self.text.append('\n- ')

    def handle_endtag(self, tag):
        if tag == 'p':
            self.text.append('\n\n')
            self.in_paragraph = False
        elif tag == 'strong' or tag == 'b':
            self.text.append('**')
            self.in_strong = False
        elif tag == 'em' or tag == 'i':
            self.text.append('*')
            self.in_em = False
        elif tag == 'code':
            self.text.append('`')
            self.in_code = False
        elif tag == 'pre':
            self.text.append('\n```\n')
            self.in_pre = False
        elif tag == 'a':
            self.text.append('](#)')
        elif tag == 'h1' or tag == 'h2' or tag == 'h3':
            self.text.append('\n\n')
        elif tag == 'ul':
            self.text.append('\n\n')
            self.in_list = False

    def handle_data(self, data):
        if data.strip():
            # Unescape HTML entities
            text = html.unescape(data)
            self.text.append(text)

    def get_markdown(self):
        result = ''.join(self.text).strip()
        # Clean up multiple newlines
        result = re.sub(r'\n\n\n+', '\n\n', result)
        return result


def extract_images_from_html(html_content):
    """Extract image filenames from HTML content"""
    images = []
    # Match img src attributes
    pattern = r'src=["\']([^"\']*)["\']'
    matches = re.findall(pattern, html_content)
    for match in matches:
        filename = os.path.basename(match)
        if filename:
            images.append(filename)
    return images


def parse_wordpress_xml(xml_file):
    """Parse WordPress XML export"""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Define namespaces
    namespaces = {
        'wp': 'http://wordpress.org/export/1.2/',
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'dc': 'http://purl.org/dc/elements/1.1/',
        'excerpt': 'http://wordpress.org/export/1.2/excerpt/',
    }
    
    posts = []
    
    # Find all items
    for item in root.findall('.//item'):
        title_elem = item.find('title')
        title = title_elem.text if title_elem is not None else ''
        
        slug_elem = item.find('wp:post_name', namespaces)
        slug = slug_elem.text if slug_elem is not None else ''
        
        post_date_gmt_elem = item.find('wp:post_date_gmt', namespaces)
        post_date_gmt = post_date_gmt_elem.text if post_date_gmt_elem is not None else ''
        
        post_type_elem = item.find('wp:post_type', namespaces)
        post_type = post_type_elem.text if post_type_elem is not None else 'post'
        
        # Only process published posts
        if post_type != 'post':
            continue
        
        # Parse date to get year and month
        try:
            dt = datetime.fromisoformat(post_date_gmt.replace('Z', '+00:00'))
            year = dt.year
            month = dt.month
        except:
            continue
        
        # Check if this is a target post
        if (year, month, slug) not in TARGET_POSTS:
            continue
        
        # Extract metadata
        author_elem = item.find('dc:creator', namespaces)
        author = author_elem.text if author_elem is not None else ''
        
        content_encoded_elem = item.find('content:encoded', namespaces)
        html_content = content_encoded_elem.text if content_encoded_elem is not None else ''
        
        # Extract tags and categories
        tags = []
        categories = []
        for category in item.findall('category'):
            domain = category.get('domain', '')
            term = category.get('nicename', '')
            if domain == 'post_tag':
                tags.append(term)
            elif domain == 'category' and term != 'uncategorized':
                categories.append(term)
        
        # Extract images
        images = extract_images_from_html(html_content)
        
        # Get first image as hero (or first image in content)
        hero_image = images[0] if images else ''
        
        # Convert HTML to markdown
        converter = HTMLToMarkdownConverter()
        try:
            converter.feed(html_content)
            markdown_content = converter.get_markdown()
        except:
            markdown_content = html_content
        
        # Get description (first 100-150 chars)
        description = markdown_content[:150].replace('\n', ' ').strip()
        if len(markdown_content) > 150:
            description += '...'
        
        posts.append({
            'title': title,
            'date_iso': post_date_gmt,
            'slug': slug,
            'description': description,
            'author': author,
            'tags': tags,
            'categories': categories,
            'images': images,
            'hero_image': hero_image,
            'html_content': html_content,
            'markdown_content': markdown_content,
            'year': year,
            'month': month,
        })
    
    return posts


def verify_images_exist(year, month, images):
    """Verify if image files exist in WordPress uploads folder"""
    upload_path = f"C:\\Dev\\Alex\\NewBlog\\wp-source\\uploads\\{year}\\{month:02d}"
    results = {}
    
    for img in images:
        img_path = os.path.join(upload_path, img)
        results[img] = os.path.exists(img_path)
    
    return results


def save_post_body(year, month, slug, markdown_content):
    """Save post body to file"""
    output_dir = "C:\\Dev\\Alex\\blog\\AnythingAboutITBlog\\scripts\\tmp"
    os.makedirs(output_dir, exist_ok=True)
    
    filename = f"body-{year}-{month:02d}-{slug}.md"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    return filepath


def main():
    xml_file = "C:\\Dev\\Alex\\NewBlog\\anythingaboutit.WordPress.2026-04-11.xml"
    
    print("Parsing WordPress XML export...")
    posts = parse_wordpress_xml(xml_file)
    
    print(f"Found {len(posts)} target posts from 2020")
    
    results = []
    
    for post in posts:
        print(f"\nProcessing: {post['title']}")
        print(f"  Slug: {post['slug']}")
        print(f"  Date: {post['date_iso']}")
        print(f"  Images found: {len(post['images'])}")
        
        # Save body file
        body_filepath = save_post_body(post['year'], post['month'], post['slug'], post['markdown_content'])
        print(f"  Saved body to: {body_filepath}")
        
        # Verify images
        image_verify = verify_images_exist(post['year'], post['month'], post['images'])
        missing_images = [img for img, exists in image_verify.items() if not exists]
        
        if missing_images:
            print(f"  WARNING: Missing images: {missing_images}")
        
        results.append({
            'title': post['title'],
            'date': post['date_iso'],
            'slug': post['slug'],
            'description': post['description'],
            'year': post['year'],
            'month': post['month'],
            'author': post['author'],
            'tags': post['tags'],
            'categories': post['categories'],
            'image_list': post['images'],
            'hero_image': post['hero_image'],
            'body_file_path': body_filepath,
            'images_verified': image_verify,
        })
    
    # Save results to JSON
    output_json = "C:\\Dev\\Alex\\blog\\AnythingAboutITBlog\\scripts\\extracted_2020_posts.json"
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✓ Extracted {len(results)} posts")
    print(f"✓ Results saved to: {output_json}")
    print(f"\nStructured results:")
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
