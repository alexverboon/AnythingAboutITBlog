import re
from pathlib import Path
from collections import defaultdict

root = Path(r'C:/Dev/Alex/blog/AnythingAboutITBlog')
files = sorted((root / 'content' / 'post').rglob('index.md'))

issue_counts = defaultdict(int)
issue_samples = defaultdict(list)

def add_issue(kind, path):
    issue_counts[kind] += 1
    if len(issue_samples[kind]) < 10:
        issue_samples[kind].append(str(path))

def norm(v):
    if v is None:
        return ''
    v = v.strip()
    if (len(v) >= 2 and ((v[0] == '"' and v[-1] == '"') or (v[0] == "'" and v[-1] == "'"))):
        v = v[1:-1].strip()
    return v

def scalar(lines, key):
    pat = re.compile(rf'^{re.escape(key)}:\s*(.*)$', re.I)
    for line in lines:
        m = pat.match(line)
        if m:
            return m.group(1)
    return None

def list_has_items(lines, key):
    key_pat = re.compile(rf'^{re.escape(key)}:\s*(.*)$', re.I)
    top_key_pat = re.compile(r'^[A-Za-z0-9_-]+\s*:')
    for i, line in enumerate(lines):
        m = key_pat.match(line)
        if not m:
            continue
        tail = m.group(1).strip()
        if tail:
            m2 = re.match(r'^\[(.*)\]$', tail)
            if m2:
                items = [norm(x) for x in m2.group(1).split(',') if norm(x)]
                return len(items) > 0
            return False
        c = 0
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            if top_key_pat.match(nxt):
                break
            if re.match(r'^\s*-\s+\S', nxt):
                c += 1
            j += 1
        return c > 0
    return None

for f in files:
    text = f.read_text(encoding='utf-8', errors='replace')
    lines = re.split(r'\r?\n', text)

    if not lines or lines[0].strip() != '---':
        add_issue('front_matter_missing_or_not_at_top', f)
        continue

    close_idx = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            close_idx = i
            break
    if close_idx < 0:
        add_issue('front_matter_unclosed', f)
        continue

    fm = lines[1:close_idx]

    title = norm(scalar(fm, 'title'))
    if not title:
        add_issue('title_missing_or_empty', f)

    date = norm(scalar(fm, 'date'))
    if not date:
        add_issue('date_missing', f)
    elif not re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$', date):
        add_issue('date_not_iso_utc', f)

    desc = norm(scalar(fm, 'description'))
    if not desc:
        add_issue('description_missing_or_empty', f)

    author = norm(scalar(fm, 'author'))
    if not author:
        add_issue('author_missing_or_empty', f)

    tags = list_has_items(fm, 'tags')
    if tags is None:
        add_issue('tags_missing', f)
    elif not tags:
        add_issue('tags_empty', f)

    cats = list_has_items(fm, 'categories')
    if cats is None:
        add_issue('categories_missing', f)
    elif not cats:
        add_issue('categories_empty', f)


total_issues = sum(issue_counts.values())
overall = 'PASS' if total_issues == 0 else 'FAIL'

print(f'TOTAL_FILES_SCANNED: {len(files)}')
print(f'OVERALL_SUMMARY: {overall} (total issues: {total_issues})')
print('ISSUE_COUNTS_START')
if not issue_counts:
    print('No issues found.')
else:
    for k in sorted(issue_counts):
        print(f'{k}: {issue_counts[k]}')
print('ISSUE_COUNTS_END')
print('ISSUE_SAMPLES_START')
if not issue_samples:
    print('No sample paths (no issues).')
else:
    for k in sorted(issue_samples):
        print(f'[{k}]')
        for p in issue_samples[k]:
            print(p)
print('ISSUE_SAMPLES_END')
