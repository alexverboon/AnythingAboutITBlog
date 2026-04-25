#!/usr/bin/env python3
"""
Extract all WordPress posts for a specific year with metadata and markdown content.
"""

import argparse
import html
import json
import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from html.parser import HTMLParser


class HTMLToMarkdownConverter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.in_pre = False
        self._pending_href = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag in ("strong", "b"):
            self.text.append("**")
        elif tag in ("em", "i"):
            self.text.append("*")
        elif tag == "code":
            if not self.in_pre:
                self.text.append("`")
        elif tag == "pre":
            self.text.append("\n```\n")
            self.in_pre = True
        elif tag == "a":
            self._pending_href = attrs_dict.get("href", "#")
            self.text.append("[")
        elif tag == "img":
            src = attrs_dict.get("src", "")
            alt = attrs_dict.get("alt", "image")
            filename = os.path.basename(src) if src else src
            self.text.append(f"\n![{alt}](images/{filename})\n")
        elif tag == "br":
            self.text.append("\n")
        elif tag == "h1":
            self.text.append("\n# ")
        elif tag == "h2":
            self.text.append("\n## ")
        elif tag == "h3":
            self.text.append("\n### ")
        elif tag == "h4":
            self.text.append("\n#### ")
        elif tag == "li":
            self.text.append("\n- ")
        elif tag == "blockquote":
            self.text.append("\n> ")

    def handle_endtag(self, tag):
        if tag == "p":
            self.text.append("\n\n")
        elif tag in ("strong", "b"):
            self.text.append("**")
        elif tag in ("em", "i"):
            self.text.append("*")
        elif tag == "code":
            if not self.in_pre:
                self.text.append("`")
        elif tag == "pre":
            self.text.append("\n```\n")
            self.in_pre = False
        elif tag == "a":
            href = self._pending_href or "#"
            self.text.append(f"]({href})")
            self._pending_href = None
        elif tag in ("h1", "h2", "h3", "h4", "ul", "ol", "blockquote"):
            self.text.append("\n\n")

    def handle_data(self, data):
        self.text.append(html.unescape(data))

    def get_markdown(self):
        result = "".join(self.text).strip()
        return re.sub(r"\n{3,}", "\n\n", result)


def extract_images_from_html(html_content):
    images = []
    seen = set()
    for match in re.findall(r"src=[\"']([^\"']*)[\"']", html_content):
        filename = os.path.basename(match)
        if filename and filename not in seen and re.search(r"\.(png|jpg|jpeg|gif|webp|svg|bmp)(\?.*)?$", filename, re.IGNORECASE):
            seen.add(filename)
            images.append(filename)
    return images


def extract_image_src_map(html_content):
    src_map = {}
    for match in re.findall(r"src=[\"']([^\"']*)[\"']", html_content):
        filename = os.path.basename(match)
        if not filename:
            continue
        if filename not in src_map:
            src_map[filename] = match
    return src_map


def convert_linked_local_images_to_remote(markdown_content):
    pattern = re.compile(
        r"\[\s*!\[([^\]]*)\]\(images/[^)]+\)\s*\]\((https?://[^)]+)\)",
        re.MULTILINE,
    )
    return pattern.sub(lambda m: f"![{m.group(1)}]({m.group(2)})", markdown_content)


def parse_post_datetime(gmt, local, fallback_year):
    for val in (gmt, local):
        if not val or val == "0000-00-00 00:00:00":
            continue
        try:
            return datetime.strptime(val, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue
    return datetime(fallback_year, 1, 1)


def to_iso(gmt, local, dt):
    src = gmt if (gmt and gmt != "0000-00-00 00:00:00") else local
    if src and src != "0000-00-00 00:00:00":
        return src.replace(" ", "T") + "Z"
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def slugify(text):
    text = html.unescape(text or "")
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")


def parse_wordpress_xml(xml_file, target_year):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    ns = {
        "wp": "http://wordpress.org/export/1.2/",
        "content": "http://purl.org/rss/1.0/modules/content/",
        "dc": "http://purl.org/dc/elements/1.1/",
    }

    posts = []
    used_slugs = set()
    for item in root.findall(".//item"):
        pt = item.find("wp:post_type", ns)
        if pt is None or pt.text != "post":
            continue

        status_el = item.find("wp:status", ns)
        status = (status_el.text or "") if status_el is not None else ""
        if status in {"trash", "auto-draft", "inherit"}:
            continue

        slug_el = item.find("wp:post_name", ns)
        slug = (slug_el.text or "") if slug_el is not None else ""

        pid_el = item.find("wp:post_id", ns)
        post_id = (pid_el.text or "") if pid_el is not None else ""

        gmt_el = item.find("wp:post_date_gmt", ns)
        gmt = (gmt_el.text or "") if gmt_el is not None else ""
        local_el = item.find("wp:post_date", ns)
        local = (local_el.text or "") if local_el is not None else ""

        dt = parse_post_datetime(gmt, local, target_year)
        if dt.year != target_year:
            continue

        title_el = item.find("title")
        title = (title_el.text or "") if title_el is not None else ""

        if not title:
            title = f"Untitled Post {post_id}" if post_id else "Untitled Post"
        if not slug:
            slug = slugify(title) or (f"untitled-post-{post_id}" if post_id else f"untitled-post-{target_year}")

        # Keep slugs unique within the extracted year to avoid migration path collisions.
        base_slug = slug
        if slug in used_slugs:
            if post_id:
                slug = f"{base_slug}-{post_id}"
            else:
                suffix = 2
                while f"{base_slug}-{suffix}" in used_slugs:
                    suffix += 1
                slug = f"{base_slug}-{suffix}"
        used_slugs.add(slug)

        author_el = item.find("dc:creator", ns)
        author = (author_el.text or "") if author_el is not None else ""

        content_el = item.find("content:encoded", ns)
        html_content = (content_el.text or "") if content_el is not None else ""

        tags = []
        categories = []
        for cat in item.findall("category"):
            domain = cat.get("domain", "")
            nicename = cat.get("nicename", "")
            if domain == "post_tag" and nicename:
                tags.append(nicename)
            elif domain == "category" and nicename and nicename.lower() != "uncategorized":
                categories.append(nicename)

        images = extract_images_from_html(html_content)
        image_src_map = extract_image_src_map(html_content)
        hero_image = images[0] if images else ""

        converter = HTMLToMarkdownConverter()
        try:
            converter.feed(html_content)
            markdown_content = converter.get_markdown()
        except Exception:
            markdown_content = html_content

        desc_plain = re.sub(r"\s+", " ", markdown_content.replace("\n", " ")).strip()
        description = desc_plain[:150] + ("..." if len(desc_plain) > 150 else "")
        if not description:
            description = title

        posts.append(
            {
                "title": title,
                "date": to_iso(gmt, local, dt),
                "slug": slug,
                "description": description,
                "year": dt.year,
                "month": dt.month,
                "author": author,
                "status": status,
                "post_id": post_id,
                "tags": tags,
                "categories": categories,
                "image_list": images,
                "hero_image": hero_image,
                "image_src_map": image_src_map,
                "markdown_content": markdown_content,
            }
        )

    return posts


def save_post_body(repo_root, year, month, slug, markdown_content):
    output_dir = os.path.join(repo_root, "scripts", "tmp")
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, f"body-{year}-{month:02d}-{slug}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    return filepath


def apply_remote_fallback_if_missing_local(post, repo_root, uploads_root):
    src_dir = os.path.join(uploads_root, str(post["year"]), f"{int(post['month']):02d}")
    missing = [img for img in post["image_list"] if not os.path.exists(os.path.join(src_dir, img))]
    if not missing:
        return post

    updated_md = convert_linked_local_images_to_remote(post["markdown_content"])

    # Replace remaining local image links with original source URLs when available.
    image_src_map = post.get("image_src_map", {})
    for img in missing:
        src = image_src_map.get(img, "")
        if src:
            updated_md = updated_md.replace(f"(images/{img})", f"({src})")

    post["markdown_content"] = updated_md
    # Prevent migrate-post.ps1 from failing local image copy when source files are absent.
    post["image_list"] = []
    post["hero_image"] = ""
    post["remote_fallback"] = True
    post["missing_local_images"] = missing
    return post


def main():
    parser = argparse.ArgumentParser(description="Extract WordPress posts for a target year")
    parser.add_argument("year", type=int, help="Target year (e.g. 2015)")
    parser.add_argument(
        "--xml",
        default=r"C:\Dev\Alex\NewBlog\anythingaboutit.WordPress.2026-04-11.xml",
        help="Path to WordPress XML export",
    )
    parser.add_argument(
        "--repo-root",
        default=r"C:\Dev\Alex\blog\AnythingAboutITBlog",
        help="Path to Hugo repository root",
    )
    parser.add_argument(
        "--uploads-root",
        default=r"C:\Dev\Alex\NewBlog\wp-source\uploads",
        help="Path to WordPress uploads root",
    )
    args = parser.parse_args()

    print(f"Parsing WordPress XML export for {args.year} posts...")
    posts = parse_wordpress_xml(args.xml, args.year)

    if not posts:
        print("ERROR: No matching posts found.")
        return

    print(f"Found {len(posts)} posts")
    results = []
    fallback_count = 0

    for post in sorted(posts, key=lambda p: p["date"], reverse=True):
        post = apply_remote_fallback_if_missing_local(post, args.repo_root, args.uploads_root)
        if post.get("remote_fallback"):
            fallback_count += 1

        body_filepath = save_post_body(args.repo_root, post["year"], post["month"], post["slug"], post["markdown_content"])
        results.append(
            {
                "title": post["title"],
                "date": post["date"],
                "slug": post["slug"],
                "description": post["description"],
                "year": post["year"],
                "month": f"{post['month']:02d}",
                "author": post["author"],
                "status": post["status"],
                "post_id": post["post_id"],
                "tags": post["tags"],
                "categories": post["categories"],
                "image_list": post["image_list"],
                "hero_image": post["hero_image"],
                "body_file_path": body_filepath,
                "remote_fallback": post.get("remote_fallback", False),
                "missing_local_images": post.get("missing_local_images", []),
            }
        )

    output_json = os.path.join(args.repo_root, "scripts", f"extracted_{args.year}_posts.json")
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"[OK] Extracted {len(results)} posts -> {output_json}")
    print(f"[INFO] Remote fallback applied to {fallback_count} posts")


if __name__ == "__main__":
    main()
