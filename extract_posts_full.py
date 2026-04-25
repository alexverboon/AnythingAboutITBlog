#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import sys
import re
import json
from datetime import datetime

# XML file path
xml_file = r'C:\Dev\Alex\NewBlog\anythingaboutit.WordPress.2026-04-11.xml'

# Namespaces
ns = {
    'wp': 'http://wordpress.org/export/1.2/',
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'excerpt': 'http://wordpress.org/export/1.2/excerpt/',
    'wfw': 'http://wellformedweb.org/CommentAPI/'
}

# Target slugs
target_slugs = [
    'use-microsoft-endpoint-configuration-manager-to-configure-the-windows-print-spooler-service',
    'use-advanced-hunting-to-identify-defender-clients-with-outdated-definitions'
]

def extract_image_filenames(content_html):
    """Extract image filenames from HTML content"""
    images = []
    # Find image URLs
    pattern = r'<img[^>]+src=["\']?([^"\'>\s]+)["\']?'
    matches = re.findall(pattern, content_html, re.IGNORECASE)
    for match in matches:
        # Extract just the filename
        filename = match.split('/')[-1]
        if filename and filename not in images:
            images.append(filename)
    return images

def html_to_markdown(html_content):
    """Simple HTML to Markdown conversion"""
    md = html_content
    # Basic conversions
    md = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\n\1\n\n', md, flags=re.IGNORECASE | re.DOTALL)
    md = re.sub(r'<br\s*/?>', '\n', md, flags=re.IGNORECASE)
    md = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', md, flags=re.IGNORECASE | re.DOTALL)
    md = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', md, flags=re.IGNORECASE | re.DOTALL)
    md = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', md, flags=re.IGNORECASE | re.DOTALL)
    md = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', md, flags=re.IGNORECASE | re.DOTALL)
    md = re.sub(r'<a\s+href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', md, flags=re.IGNORECASE | re.DOTALL)
    md = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', md, flags=re.IGNORECASE | re.DOTALL)
    md = re.sub(r'<pre[^>]*>(.*?)</pre>', r'```\n\1\n```', md, flags=re.IGNORECASE | re.DOTALL)
    md = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n# \1\n', md, flags=re.IGNORECASE | re.DOTALL)
    md = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n## \1\n', md, flags=re.IGNORECASE | re.DOTALL)
    md = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n### \1\n', md, flags=re.IGNORECASE | re.DOTALL)
    md = re.sub(r'<img[^>]+src=["\']?([^"\'>\s]+)["\']?[^>]*>', r'![](\1)', md, flags=re.IGNORECASE)
    md = re.sub(r'<ul[^>]*>(.*?)</ul>', r'\n\1\n', md, flags=re.IGNORECASE | re.DOTALL)
    md = re.sub(r'<ol[^>]*>(.*?)</ol>', r'\n\1\n', md, flags=re.IGNORECASE | re.DOTALL)
    md = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', md, flags=re.IGNORECASE | re.DOTALL)
    # Remove remaining HTML tags
    md = re.sub(r'<[^>]+>', '', md)
    # Clean up extra newlines
    md = re.sub(r'\n\n+', '\n\n', md)
    md = md.strip()
    return md

def extract_post_data(item_element):
    """Extract all relevant post data from an item element"""
    data = {}
    
    # Basic fields
    title_elem = item_element.find('title')
    data['title'] = title_elem.text if title_elem is not None and title_elem.text else ''
    
    date_elem = item_element.find('wp:post_date_gmt', ns)
    data['date_gmt'] = date_elem.text if date_elem is not None and date_elem.text else ''
    
    post_id_elem = item_element.find('wp:post_id', ns)
    data['post_id'] = post_id_elem.text if post_id_elem is not None else ''
    
    post_name_elem = item_element.find('wp:post_name', ns)
    data['post_name'] = post_name_elem.text if post_name_elem is not None else ''
    
    # Creator
    creator_elem = item_element.find('dc:creator', ns)
    data['creator'] = creator_elem.text if creator_elem is not None else ''
    
    # Categories
    categories = []
    tags = []
    for cat in item_element.findall('category'):
        domain = cat.get('domain')
        nicename = cat.get('nicename')
        cat_text = cat.text
        if domain == 'category' and cat_text:
            categories.append(cat_text)
        elif domain == 'post_tag' and cat_text:
            tags.append(cat_text)
    
    data['categories'] = categories
    data['tags'] = tags
    
    # Content
    content_elem = item_element.find('content:encoded', ns)
    data['content_html'] = content_elem.text if content_elem is not None else ''
    
    # Extract images from content
    data['images'] = extract_image_filenames(data['content_html'])
    
    # Convert HTML to Markdown
    data['content_markdown'] = html_to_markdown(data['content_html'])
    
    return data

def convert_date_to_iso(date_str):
    """Convert WordPress date to ISO format"""
    try:
        # WordPress format: 2021-07-10 15:07:17
        dt = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        return dt.strftime('%Y-%m-%dT%H:%M:%SZ')
    except:
        return date_str

def main():
    print("Parsing XML file...")
    sys.stdout.flush()
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
    except Exception as e:
        print(f"Error parsing XML: {e}")
        sys.exit(1)
    
    # Find all items
    items = root.findall('.//item')
    print(f"Total items found: {len(items)}")
    sys.stdout.flush()
    
    # Search for target posts
    found_posts = {}
    for item in items:
        post_name_elem = item.find('wp:post_name', ns)
        if post_name_elem is not None and post_name_elem.text in target_slugs:
            slug = post_name_elem.text
            print(f"Found post with slug: {slug}")
            data = extract_post_data(item)
            found_posts[slug] = data
            sys.stdout.flush()
    
    # Output results to file
    output_file = r'C:\Dev\Alex\blog\AnythingAboutITBlog\extracted_posts.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        for slug, data in found_posts.items():
            f.write(f"\n{'='*100}\n")
            f.write(f"POST: {slug}\n")
            f.write(f"{'='*100}\n\n")
            
            f.write(f"TITLE: {data['title']}\n")
            f.write(f"DATE: {convert_date_to_iso(data['date_gmt'])}\n")
            f.write(f"SLUG: {data['post_name']}\n")
            f.write(f"CATEGORIES: {', '.join(data['categories'])}\n")
            f.write(f"TAGS: {', '.join(data['tags'])}\n")
            
            # Identify hero image (usually first image)
            hero_image = data['images'][0] if data['images'] else ''
            f.write(f"HERO_IMAGE: {hero_image}\n")
            
            # Remaining images as body images
            body_images = data['images'][1:] if len(data['images']) > 1 else []
            f.write(f"BODY_IMAGES: {', '.join(body_images)}\n")
            
            f.write(f"\nBODY_MARKDOWN:\n")
            f.write(data['content_markdown'])
            f.write(f"\n\n")
    
    print(f"\nResults written to: {output_file}")

if __name__ == '__main__':
    main()
