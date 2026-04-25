import re
from pathlib import Path
from collections import Counter
root = Path(r"C:/Dev/Alex/blog/AnythingAboutITBlog")
removed = {"windows-7","windows7","windows-8","windows8","windows-10","windows10","windows-11","windows11","widnows-10","widnows10","windows-8-1","windows81"}
canon = ["Windows","PowerShell","WinPE","Office"]

def fm(text):
    m = re.match(r"^---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|$)", text, re.S)
    return m.group(1) if m else None

def tags(fm_text):
    lines = fm_text.splitlines(); out=[]; i=0
    key = re.compile(r"^\s*tags\s*:\s*(.*?)\s*$", re.I)
    nextk = re.compile(r"^\s*[A-Za-z0-9_\-]+\s*:\s*")
    while i < len(lines):
        m = key.match(lines[i])
        if not m: i += 1; continue
        tail = m.group(1).strip()
        if tail:
            if tail.startswith('[') and tail.endswith(']'):
                inner = tail[1:-1].strip()
                if inner: out += [p.strip().strip('"\'') for p in inner.split(',') if p.strip()]
            else:
                out.append(tail.strip().strip('"\''))
            return out
        i += 1
        while i < len(lines):
            if nextk.match(lines[i]): return out
            bm = re.match(r"^\s*-\s*(.*?)\s*$", lines[i])
            if bm:
                v = bm.group(1).strip().strip('"\'')
                if v: out.append(v)
            elif lines[i].strip():
                return out
            i += 1
        return out
    return out

rc = Counter(); cc = Counter()
for p in sorted((root/"content/post").rglob("index.md")):
    try: raw = p.read_text(encoding="utf-8")
    except UnicodeDecodeError: raw = p.read_text(encoding="utf-8", errors="ignore")
    front = fm(raw)
    if not front: continue
    for t in tags(front):
        tl = t.lower().strip()
        if tl in removed: rc[tl] += 1
        for c in canon:
            if tl == c.lower(): cc[c] += 1
print("Removed Windows version-tag occurrences:")
if rc:
    [print(f"  {k}: {v}") for k,v in sorted(rc.items())]
else:
    print("  none")
print("Canonical tag occurrences:")
for c in canon:
    print(f"  {c}: {cc.get(c,0)}")
