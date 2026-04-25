import json
import re
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(r"C:/Dev/Alex/blog/AnythingAboutITBlog")
POST_DIR = ROOT / "content" / "post"
OUT_DIR = ROOT / "tmp_taxonomy_report"
OUT_FILE = OUT_DIR / "family_tag_normalization.json"

REMOVED_WINDOWS = {
    "windows-7", "windows7", "windows-8", "windows8", "windows-10", "windows10",
    "windows-11", "windows11", "widnows-10", "widnows10", "windows-8-1", "windows81",
}
REMOVED_POWERSHELL = {"powershell"}
REMOVED_WINPE = {"winpe", "windows-pe", "windowspe"}
REMOVED_OFFICE = {
    "office-365", "office365", "office-2010", "office2010", "office-2013", "office2013", "office-2016", "office2016"
}
REMOVED_ALL = REMOVED_WINDOWS | REMOVED_POWERSHELL | REMOVED_WINPE | REMOVED_OFFICE

CANONICAL_ORDER = ["Windows", "PowerShell", "WinPE", "Office"]


def split_front_matter(text: str):
    if not text.startswith("---"):
        return None
    m = re.match(r"^---\s*\r?\n(.*?)\r?\n---\s*(\r?\n|$)", text, flags=re.S)
    if not m:
        return None
    fm = m.group(1)
    body = text[m.end():]
    return fm, body


def parse_tags_from_fm_lines(lines):
    tags = []
    start = None
    end = None
    style = None
    key_indent = ""

    i = 0
    key_re = re.compile(r"^(\s*)tags\s*:\s*(.*?)\s*$", re.I)
    keyline_re = re.compile(r"^\s*[A-Za-z0-9_\-]+\s*:\s*")

    while i < len(lines):
        m = key_re.match(lines[i])
        if not m:
            i += 1
            continue

        key_indent = m.group(1)
        tail = m.group(2).strip()
        start = i

        if tail:
            style = "inline"
            if tail.startswith("[") and tail.endswith("]"):
                inner = tail[1:-1].strip()
                if inner:
                    parts = [p.strip() for p in inner.split(",")]
                    tags = [p.strip("\"'") for p in parts if p.strip("\"' ")]
                else:
                    tags = []
            else:
                tags = [tail.strip("\"'")]
            end = i + 1
            return tags, start, end, style, key_indent

        style = "block"
        i += 1
        while i < len(lines):
            line = lines[i]
            if keyline_re.match(line):
                break
            bm = re.match(r"^\s*-\s*(.*?)\s*$", line)
            if bm:
                v = bm.group(1).strip().strip("\"'")
                if v:
                    tags.append(v)
            elif line.strip():
                # Non-empty unknown line in tags block; stop conservatively
                break
            i += 1
        end = i
        return tags, start, end, style, key_indent

    return None, None, None, None, None


def dedupe_case_insensitive(seq):
    out = []
    seen = set()
    for x in seq:
        k = x.lower()
        if k in seen:
            continue
        seen.add(k)
        out.append(x)
    return out


def slug_from_path(p: Path):
    try:
        return p.parent.name
    except Exception:
        return ""


def indicates_windows(text):
    t = text.lower()
    if "windows" not in t and not re.search(r"\b(win\s?7|win\s?8|win\s?10|win\s?11)\b", t):
        return False
    return bool(re.search(r"\bwindows\s*(7|8(?:\.1)?|10|11)?\b|\bwin\s?(7|8|10|11)\b", t))


def indicates_powershell(text):
    return "powershell" in text.lower()


def indicates_winpe(text):
    t = text.lower()
    return ("winpe" in t) or ("windows pe" in t)


def indicates_office(text):
    t = text.lower()
    return bool(re.search(r"\bmicrosoft\s+office\b|\boffice\s*365\b|\boffice-365\b|\boffice365\b|\boffice\b", t))


def build_tags_block(tags, key_indent=""):
    lines = [f"{key_indent}tags:"]
    item_indent = key_indent + "  "
    for t in tags:
        lines.append(f"{item_indent}- {t}")
    return lines


files = sorted(POST_DIR.rglob("index.md")) if POST_DIR.exists() else []
changed = []
added_counts = Counter()
removed_variant_counts = Counter()

for f in files:
    try:
        raw = f.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        raw = f.read_text(encoding="utf-8", errors="ignore")

    split = split_front_matter(raw)
    if not split:
        continue

    fm, body = split
    fm_lines = fm.splitlines()

    tags, start, end, style, key_indent = parse_tags_from_fm_lines(fm_lines)
    if start is None:
        # No tags field: still may need to add based on content signals
        tags = []
        start = len(fm_lines)
        end = len(fm_lines)
        key_indent = ""

    orig_tags = list(tags)

    title_m = re.search(r"^\s*title\s*:\s*(.*?)\s*$", fm, flags=re.I | re.M)
    title = title_m.group(1).strip().strip('"\'') if title_m else ""

    # Use whole front matter+body+slug+existing tags/categories for detection scope
    detection_text = "\n".join([
        title,
        slug_from_path(f),
        fm,
        body,
        " ".join(orig_tags),
    ])

    want_windows = indicates_windows(detection_text)
    want_powershell = indicates_powershell(detection_text)
    want_winpe = indicates_winpe(detection_text)
    want_office = indicates_office(detection_text)

    retained = []
    for t in orig_tags:
        tl = t.lower().strip()
        if tl in REMOVED_ALL:
            removed_variant_counts[tl] += 1
            continue
        retained.append(t)

    retained = dedupe_case_insensitive(retained)

    to_add = []
    if want_windows:
        to_add.append("Windows")
    if want_powershell:
        to_add.append("PowerShell")
    if want_winpe:
        to_add.append("WinPE")
    if want_office:
        to_add.append("Office")

    existing_lower = {t.lower() for t in retained}
    for c in CANONICAL_ORDER:
        if c in to_add and c.lower() not in existing_lower:
            retained.append(c)
            existing_lower.add(c.lower())
            added_counts[c] += 1

    new_tags = retained

    if [t.lower() for t in new_tags] == [t.lower() for t in orig_tags] and len(new_tags) == len(orig_tags):
        continue

    new_fm_lines = fm_lines[:start] + build_tags_block(new_tags, key_indent=key_indent) + fm_lines[end:]
    new_fm = "\n".join(new_fm_lines)
    new_raw = f"---\n{new_fm}\n---\n{body}"

    if new_raw != raw:
        f.write_text(new_raw, encoding="utf-8")
        changed.append(str(f.relative_to(ROOT)).replace("\\", "/"))

# Save summary
OUT_DIR.mkdir(parents=True, exist_ok=True)
summary = {
    "root": str(ROOT),
    "scanned_files": len(files),
    "changed_files": len(changed),
    "added_canonical_counts": {k: int(added_counts.get(k, 0)) for k in CANONICAL_ORDER},
    "removed_variant_counts": dict(sorted((k, int(v)) for k, v in removed_variant_counts.items())),
    "changed_files_sample": changed[:25],
}
OUT_FILE.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

print(f"Total files scanned: {summary['scanned_files']}")
print(f"Total files changed: {summary['changed_files']}")
print("Added canonical tags:")
for k in CANONICAL_ORDER:
    print(f"  {k}: {summary['added_canonical_counts'][k]}")
print("Removed variant tags by value:")
if summary["removed_variant_counts"]:
    for k, v in summary["removed_variant_counts"].items():
        print(f"  {k}: {v}")
else:
    print("  (none)")
print("Changed file paths (up to 25):")
for p in summary["changed_files_sample"]:
    print(f"  {p}")
print(f"Summary JSON: {OUT_FILE}")
