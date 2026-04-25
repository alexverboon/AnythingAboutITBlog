#!/usr/bin/env python3
import re

# Read the extracted posts
input_file = r'C:\Dev\Alex\blog\AnythingAboutITBlog\extracted_posts.txt'
output_file = r'C:\Dev\Alex\blog\AnythingAboutITBlog\extracted_posts_final.txt'

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace full image URLs with bare filenames
# Pattern: ![](https://www.verboon.info/wp-content/uploads/YYYY/MM/filename.png)
# Replace with: ![](filename.png)
content = re.sub(
    r'!\[\]\(https://www\.verboon\.info/wp-content/uploads/\d{4}/\d{2}/([^/]+\.png)\)',
    r'![](\1)',
    content,
    flags=re.IGNORECASE
)

# Also handle any other URL patterns that might exist
content = re.sub(
    r'!\[\]\(https?://[^/]+/(?:[^/]+/)*([^/]+\.(?:png|jpg|jpeg|gif))\)',
    r'![](\1)',
    content,
    flags=re.IGNORECASE
)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Cleaned output written to: {output_file}")
