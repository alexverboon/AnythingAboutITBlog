#!/usr/bin/env python3
"""Display structured summary of extracted 2020 posts"""

import json

with open('extracted_2020_posts.json') as f:
    posts = json.load(f)

print("=" * 100)
print("WORDPRESS 2020 POSTS EXTRACTION SUMMARY")
print("=" * 100)
print()

for i, post in enumerate(posts, 1):
    print(f"{i}. {post['title']}")
    print(f"   Date: {post['date']} (UTC)")
    print(f"   Slug: {post['slug']}")
    print(f"   Author: {post['author']}")
    print(f"   Year/Month: {post['year']}/{post['month']:02d}")
    print(f"   Description: {post['description']}")
    print(f"   Tags: {', '.join(post['tags']) if post['tags'] else 'None'}")
    print(f"   Categories: {', '.join(post['categories']) if post['categories'] else 'None'}")
    print(f"   Images: {len(post['image_list'])} files")
    print(f"   Hero Image: {post['hero_image']}")
    print(f"   Body File: {post['body_file_path']}")
    print(f"   All Images Verified: {all(post['images_verified'].values())}")
    print()

print("=" * 100)
print(f"TOTAL: {len(posts)} posts extracted successfully")
print("=" * 100)
print()

# Check for any missing images
missing = []
for post in posts:
    for img, verified in post['images_verified'].items():
        if not verified:
            missing.append(f"{post['slug']}: {img}")

if missing:
    print("WARNING: Missing images:")
    for m in missing:
        print(f"  - {m}")
else:
    print("✓ All images verified in source directories")
