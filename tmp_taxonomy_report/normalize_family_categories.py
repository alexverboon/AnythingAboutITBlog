import json
import re
from pathlib import Path
from collections import Counter

ROOT = Path(r"C:\Dev\Alex\blog\AnythingAboutITBlog")
POST_DIR = ROOT / "content" / "post"
OUT_DIR = ROOT / "tmp_taxonomy_report"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_JSON = OUT_DIR / "family_category_normalization.json"

WINDOWS_VARIANTS = {
    "windows-7","windows7","windows-8","windows8","windows-10","windows10",
    "windows-11","windows11","widnows-10","widnows10","windows-8-1","windows81"
}
POWERSHELL_VARIANTS = {"powershell"}
WINPE_VARIANTS = {"winpe","windows-pe","windowspe"}
OFFICE_VARIANTS = {"office-365","office365","office-2010","office2010","office-2013","office2013","office-2016","office2016"}

CANONICAL_ORDER = ["Windows", "PowerShell", "WinPE", "Office"]


def strip_quotes(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and ((s[0] == s[-1] == '"') or (s[0] == s[-1] == "'")):
        return s[1:-1]
    return s


def parse_inline_list(v: str):
    t = v.strip()
    if not (t.startswith("[") and t.endswith("]")):
        return []
    inner = t[1:-1].strip()
    if not inner:
        return []
    out = []
    buf = []
    q = None
    esc = False
    for ch in inner:
        if esc:
            buf.append(ch)
            esc = False
            continue
        if ch == "\\" and q is not None:
            esc = True
            continue
        if q is not None:
            if ch == q:
                q = None
            else:
                buf.append(ch)
            continue
        if ch in ('"', "'"):
            q = ch
            continue
        if ch == ",":
            out.append("".join(buf).strip())
            buf = []
            continue
        buf.append(ch)
    out.append("".join(buf).strip())
    return [strip_quotes(x) for x in out if x.strip()]


def parse_yaml_list_field(fm_text: str, key: str):
    lines = fm_text.splitlines()
    key_re = re.compile(rf'^(?P<ind>\s*){re.escape(key)}\s*:\s*(?P<rest>.*)$')
    for i, line in enumerate(lines):
        m = key_re.match(line)
        if not m:
            continue
        ind = len(m.group('ind'))
        rest = m.group('rest').strip()
        if rest.startswith('['):
            return parse_inline_list(rest)
        if rest:
            return [strip_quotes(rest)]
        vals = []
        j = i + 1
        while j < len(lines):
            nl = lines[j]
            if not nl.strip():
                j += 1
                continue
            cur_ind = len(nl) - len(nl.lstrip(' '))
            st = nl.strip()
            if cur_ind <= ind:
                break
            if st.startswith('- '):
                vals.append(strip_quotes(st[2:].strip()))
                j += 1
                continue
            break
        return vals
    return []


def parse_scalar_field(fm_text: str, key: str):
    m = re.search(rf'(?m)^\s*{re.escape(key)}\s*:\s*(.+?)\s*$', fm_text)
    return strip_quotes(m.group(1)) if m else ''


def split_front_matter(text: str):
    m = re.match(r'^(\ufeff?---\r?\n)', text)
    if not m:
        return None
    start = m.end()
    m2 = re.search(r'(?m)^---\s*$', text[start:])
    if not m2:
        return None
    fm_end_start = start + m2.start()
    fm_end_line_end = start + m2.end()
    fm_text = text[start:fm_end_start]
    body = text[fm_end_line_end:]
    open_delim = text[:start]
    close_delim = text[fm_end_start:fm_end_line_end]
    return open_delim, fm_text, close_delim, body


def replace_categories_block(fm_text: str, new_categories, newline='\n'):
    lines = fm_text.splitlines(keepends=True)
    if lines:
        for ln in lines:
            if ln.endswith('\r\n'):
                newline = '\r\n'
                break
    key_re = re.compile(r'^(?P<ind>\s*)categories\s*:\s*(?P<rest>.*)$')

    def block_lines():
        out = [f"categories:{newline}"]
        for c in new_categories:
            out.append(f"  - {c}{newline}")
        return out

    for i, line in enumerate(lines):
        raw = line[:-2] if line.endswith('\r\n') else (line[:-1] if line.endswith('\n') else line)
        m = key_re.match(raw)
        if not m:
            continue
        ind = len(m.group('ind'))
        rest = m.group('rest').strip()
        j = i + 1
        if not rest:
            while j < len(lines):
                nraw = lines[j][:-2] if lines[j].endswith('\r\n') else (lines[j][:-1] if lines[j].endswith('\n') else lines[j])
                if not nraw.strip():
                    j += 1
                    continue
                cur_ind = len(nraw) - len(nraw.lstrip(' '))
                st = nraw.strip()
                if cur_ind > ind and st.startswith('- '):
                    j += 1
                    continue
                break
        new_lines = block_lines()
        lines[i:j] = new_lines
        return ''.join(lines)

    # categories not present; append at end of front matter
    if fm_text and not fm_text.endswith(('\n', '\r')):
        fm_text = fm_text + newline
    return fm_text + ''.join(block_lines())


def dedupe_case_insensitive(items):
    seen = set()
    out = []
    for x in items:
        k = x.strip().lower()
        if not k or k in seen:
            continue
        seen.add(k)
        out.append(x.strip())
    return out


files = sorted(POST_DIR.glob('**/index.md'))
changed = 0
changed_paths = []
added_counts = Counter({k: 0 for k in CANONICAL_ORDER})
removed_variant_counts = Counter()

validation_removed_windows_variants_in_categories = 0
validation_canonical_category_occurrences = Counter({k: 0 for k in CANONICAL_ORDER})

for path in files:
    text = path.read_text(encoding='utf-8', errors='ignore')
    parts = split_front_matter(text)
    if not parts:
        continue
    open_delim, fm_text, close_delim, body = parts

    categories = parse_yaml_list_field(fm_text, 'categories')
    tags = parse_yaml_list_field(fm_text, 'tags')
    title = parse_scalar_field(fm_text, 'title')
    slug = parse_scalar_field(fm_text, 'slug')

    combined = ' '.join([title, slug, ' '.join(tags), ' '.join(categories), body]).lower()

    windows_trigger = bool(re.search(r'\bwindows[\s\-_]*(7|8(?:\.1)?|10|11)\b|\bwin(7|8|10|11)\b', combined)) or any(c.lower() in WINDOWS_VARIANTS for c in categories)
    powershell_trigger = bool(re.search(r'\bpowershell\b', combined))
    winpe_trigger = bool(re.search(r'\bwinpe\b|\bwindows[\s\-]?pe\b', combined))
    office_trigger = bool(re.search(r'\boffice(?:[\s\-_]?(?:365|2010|2013|2016))\b|\bmicrosoft\s+office\b', combined)) or any(c.lower() in OFFICE_VARIANTS for c in categories)

    retained = []
    for c in categories:
        lc = c.strip().lower()
        if lc in WINDOWS_VARIANTS or lc in POWERSHELL_VARIANTS or lc in WINPE_VARIANTS or lc in OFFICE_VARIANTS:
            removed_variant_counts[lc] += 1
            continue
        retained.append(c.strip())

    new_categories = dedupe_case_insensitive(retained)
    lower_existing = {c.lower() for c in new_categories}

    for canon, trig in [("Windows", windows_trigger), ("PowerShell", powershell_trigger), ("WinPE", winpe_trigger), ("Office", office_trigger)]:
        if trig and canon.lower() not in lower_existing:
            new_categories.append(canon)
            lower_existing.add(canon.lower())
            added_counts[canon] += 1

    # validation counters over resulting categories
    for c in new_categories:
        if c.lower() in WINDOWS_VARIANTS:
            validation_removed_windows_variants_in_categories += 1
        for canon in CANONICAL_ORDER:
            if c.lower() == canon.lower():
                validation_canonical_category_occurrences[canon] += 1

    new_fm = replace_categories_block(fm_text, new_categories)
    new_text = open_delim + new_fm + close_delim + body

    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        changed += 1
        changed_paths.append(str(path.relative_to(ROOT)).replace('\\', '/'))

summary = {
    "files_scanned": len(files),
    "files_changed": changed,
    "added_canonical_counts": {k: int(added_counts[k]) for k in CANONICAL_ORDER},
    "removed_variant_counts": dict(sorted((k, int(v)) for k, v in removed_variant_counts.items())),
    "changed_files_sample": changed_paths[:25],
    "validation": {
        "windows_variant_occurrences_remaining_in_categories": int(validation_removed_windows_variants_in_categories),
        "canonical_category_occurrences": {k: int(validation_canonical_category_occurrences[k]) for k in CANONICAL_ORDER}
    }
}

OUT_JSON.write_text(json.dumps(summary, indent=2), encoding='utf-8')

print(f"Total files scanned: {summary['files_scanned']}")
print(f"Total files changed: {summary['files_changed']}")
print("Files changed per canonical category added:")
for k in CANONICAL_ORDER:
    print(f"  {k}: {summary['added_canonical_counts'][k]}")
print("Removed variant categories by variant value:")
if summary['removed_variant_counts']:
    for k, v in summary['removed_variant_counts'].items():
        print(f"  {k}: {v}")
else:
    print("  (none)")
print("Changed file paths (up to 25):")
if summary['changed_files_sample']:
    for p in summary['changed_files_sample']:
        print(f"  {p}")
else:
    print("  (none)")
print("Validation:")
print(f"  Remaining Windows variant occurrences in categories: {summary['validation']['windows_variant_occurrences_remaining_in_categories']}")
print("  Canonical category occurrences:")
for k in CANONICAL_ORDER:
    print(f"    {k}: {summary['validation']['canonical_category_occurrences'][k]}")
print(f"JSON summary saved: {OUT_JSON}")

