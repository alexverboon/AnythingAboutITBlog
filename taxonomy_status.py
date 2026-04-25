import json, re
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(r"C:/Dev/Alex/blog/AnythingAboutITBlog")
POST_DIR = ROOT / "content" / "post"
OUT_DIR = ROOT / "tmp_taxonomy_report"
OUT_FILE = OUT_DIR / "status.json"


def parse_simple_list(text):
    text = text.strip()
    if not text:
        return []
    if text.startswith('[') and text.endswith(']'):
        inner = text[1:-1].strip()
        if not inner:
            return []
        parts = re.split(r'\s*,\s*', inner)
        return [p.strip().strip('"\'') for p in parts if p.strip().strip('"\'')]
    return [text.strip().strip('"\'')]


def extract_front_matter(md_text):
    if not md_text.startswith('---'):
        return ''
    m = re.match(r'^---\s*\n(.*?)\n---\s*(?:\n|$)', md_text, flags=re.S)
    return m.group(1) if m else ''


def extract_taxonomy_from_fm(fm_text, key):
    values = []
    lines = fm_text.splitlines()
    i = 0
    key_pat = re.compile(rf'^\s*{re.escape(key)}\s*:\s*(.*?)\s*$')
    while i < len(lines):
        line = lines[i]
        m = key_pat.match(line)
        if not m:
            i += 1
            continue
        tail = m.group(1).strip()
        if tail:
            values.extend(parse_simple_list(tail))
        else:
            i += 1
            while i < len(lines):
                sub = lines[i]
                if re.match(r'^\s*[A-Za-z0-9_\-]+\s*:\s*', sub):
                    i -= 1
                    break
                bm = re.match(r'^\s*-\s*(.*?)\s*$', sub)
                if bm:
                    v = bm.group(1).strip().strip('"\'')
                    if v:
                        values.append(v)
                elif sub.strip():
                    break
                i += 1
        i += 1
    return values


def normalize(term):
    return re.sub(r'[\W_]+', '', term.lower(), flags=re.UNICODE)


files = sorted(POST_DIR.rglob('index.md')) if POST_DIR.exists() else []
tag_counter = Counter()
cat_counter = Counter()

for f in files:
    try:
        text = f.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        text = f.read_text(encoding='utf-8', errors='ignore')
    fm = extract_front_matter(text)
    if not fm:
        continue
    tags = extract_taxonomy_from_fm(fm, 'tags')
    cats = extract_taxonomy_from_fm(fm, 'categories')
    tag_counter.update([t for t in tags if t])
    cat_counter.update([c for c in cats if c])


def dup_groups(counter, tax_name):
    by_norm = defaultdict(list)
    for name, cnt in counter.items():
        n = normalize(name)
        if n:
            by_norm[n].append((name, cnt))
    groups = []
    for n, items in by_norm.items():
        unique_names = sorted({x[0] for x in items}, key=lambda s: s.lower())
        if len(unique_names) <= 1:
            continue
        items_sorted = sorted(items, key=lambda x: (-x[1], x[0].lower()))
        groups.append({
            'taxonomy': tax_name,
            'normalized': n,
            'preferred': items_sorted[0][0],
            'variants': [{'name': nm, 'count': cnt} for nm, cnt in sorted(items, key=lambda x: (-x[1], x[0].lower()))]
        })
    return sorted(groups, key=lambda g: (g['taxonomy'], g['normalized']))


top_tags = [{'name': n, 'count': c} for n, c in tag_counter.most_common(30)]
top_categories = [{'name': n, 'count': c} for n, c in cat_counter.most_common(30)]

duplicates = dup_groups(tag_counter, 'tags') + dup_groups(cat_counter, 'categories')

report = {
    'root': str(ROOT),
    'scanned_files': len(files),
    'unique_tags': len(tag_counter),
    'unique_categories': len(cat_counter),
    'top_tags': top_tags,
    'top_categories': top_categories,
    'high_confidence_duplicate_groups': duplicates,
}

OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_FILE.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')

print(f"Scanned files: {report['scanned_files']}")
print(f"Unique tags: {report['unique_tags']}")
print(f"Unique categories: {report['unique_categories']}")
print("Top tags (up to 30): " + ", ".join([f"{x['name']} ({x['count']})" for x in top_tags]) )
print("Top categories (up to 30): " + ", ".join([f"{x['name']} ({x['count']})" for x in top_categories]) )
print(f"High-confidence duplicate groups: {len(duplicates)}")
for g in duplicates[:20]:
    vars_txt = "; ".join([f"{v['name']} ({v['count']})" for v in g['variants']])
    print(f"- [{g['taxonomy']}] {g['preferred']} <= {vars_txt}")
print(f"Report written: {OUT_FILE}")
print(f"Report exists: {OUT_FILE.exists()}")
