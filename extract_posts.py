#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import sys
import re

# XML file path
xml_file = r'C:\Dev\Alex\NewBlog\anythingaboutit.WordPress.2026-04-11.xml'

# Namespaces
ns = {
    'wp': 'http://wordpress.org/export/1.2/',
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'excerpt': 'http://wordpress.org/export/1.2/excerpt/'
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
    matches = re.findall(pattern, content_html)
    for match in matches:
        # Extract just the filename
        filename = match.split('/')[-1]
        if filename:
            images.append(filename)
    return images

def extract_post_data(item_element):
    """Extract all relevant post data from an item element"""
    data = {}
    
    # Basic fields
    data['title'] = (item_element.find('title') or ET.Element('title')).text or ''
    data['date'] = (item_element.find('wp:post_date', ns) or ET.Element('date')).text or ''
    data['date_gmt'] = (item_element.find('wp:post_date_gmt', ns) or ET.Element('date_gmt')).text or ''
    data['post_id'] = (item_element.find('wp:post_id', ns) or ET.Element('id')).text or ''
    data['post_name'] = (item_element.find('wp:post_name', ns) or ET.Element('name')).text or ''
    
    # Creator
    data['creator'] = (item_element.find('dc:creator', ns) or ET.Element('creator')).text or ''
    
    # Categories
    categories = []
    for cat in item_element.findall('category'):
        if cat.get('domain') == 'category':
            cat_text = (cat.find('..') or ET.Element('cat'))
            if cat.text:
                categories.append(cat.text)
    data['categories'] = categories
    
    # Tags
    tags = []
    for tag in item_element.findall('category'):
        if tag.get('domain') == 'post_tag':
            if tag.text:
                tags.append(tag.text)
    data['tags'] = tags
    
    # Content
    content_elem = item_element.find('content:encoded', ns)
    data['content_html'] = content_elem.text if content_elem is not None else ''
    
    # Extract images from content
    data['images'] = extract_image_filenames(data['content_html'])
    
    # Attachments
    data['attachments'] = []
    for attachment in item_element.findall('wp:attachment', ns):
        url = (attachment.find('wp:attachment_url', ns) or ET.Element('url')).text or ''
        if url:
            data['attachments'].append(url)
    
    return data

def main():
    print("Parsing XML file...")
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
    except Exception as e:
        print(f"Error parsing XML: {e}")
        sys.exit(1)
    
    # Find all items
    items = root.findall('.//item')
    print(f"Total items found: {len(items)}")
    
    # Search for target posts
    found_posts = {}
    for item in items:
        post_name_elem = item.find('wp:post_name', ns)
        if post_name_elem is not None and post_name_elem.text in target_slugs:
            slug = post_name_elem.text
            print(f"\nFound post with slug: {slug}")
            data = extract_post_data(item)
            found_posts[slug] = data
            print(f"  Title: {data['title'][:60]}")
            print(f"  Date: {data['date_gmt']}")
    
    # Output results
    print(f"\n\nTotal posts found: {len(found_posts)}")
    for slug, data in found_posts.items():
        print(f"\n{'='*80}")
        print(f"POST: {slug}")
        print(f"{'='*80}")
        print(f"Title: {data['title']}")
        print(f"Date GMT: {data['date_gmt']}")
        print(f"Categories: {', '.join(data['categories'])}")
        print(f"Tags: {', '.join(data['tags'])}")
        print(f"Images found: {len(data['images'])}")
        if data['images']:
            print(f"Image files: {', '.join(data['images'][:5])}")
        print(f"\nContent length: {len(data['content_html'])} chars")

if __name__ == '__main__':
    main()
