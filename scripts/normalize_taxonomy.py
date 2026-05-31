#!/usr/bin/env python3
import argparse
import re
from pathlib import Path
from typing import Dict, List, Tuple

import yaml

ROOT = Path(r"c:\Dev\Alex\blog\AnythingAboutITBlog")
POST_ROOT = ROOT / "content" / "post"

TARGET_KEYS = {"categories", "category", "tags", "tag"}

CATEGORY_ORDER = [
    "Security",
    "Azure",
    "M365",
    "ConfigMgr",
    "Intune",
    "PowerShell",
    "Windows",
    "Tips-Tools",
]

CATEGORY_KEYWORDS = {
    "Security": [
        "security",
        "defender",
        "atp",
        "xdr",
        "sentinel",
        "threat",
        "siem",
        "hunting",
        "incident",
        "malware",
    ],
    "Azure": [
        "azure",
        "arm",
        "log analytics",
        "kusto",
        "kql",
        "resource graph",
        "subscription",
        "tenant",
    ],
    "M365": [
        "m365",
        "microsoft 365",
        "office 365",
        "exchange",
        "sharepoint",
        "teams",
        "onenote",
        "outlook",
    ],
    "ConfigMgr": [
        "configmgr",
        "configuration manager",
        "sccm",
        "cmtrace",
        "task sequence",
        "distribution point",
    ],
    "Intune": [
        "intune",
        "endpoint manager",
        "autopilot",
        "mdm",
    ],
    "PowerShell": [
        "powershell",
        "pwsh",
        "script",
        "scripting",
    ],
    "Windows": [
        "windows",
        "driver",
        "wsus",
        "group policy",
        "gpo",
        "registry",
        "server",
        "vista",
        "xp",
    ],
    "Tips-Tools": [
        "tip",
        "tips",
        "tooltip",
        "readtip",
        "tool",
        "tools",
        "utility",
        "utilities",
    ],
}

CANONICAL_TAG_MAP = {
    "powershell": "PowerShell",
    "pwsh": "PowerShell",
    "configmgr": "ConfigMgr",
    "configuration manager": "ConfigMgr",
    "sccm": "ConfigMgr",
    "azuread": "Azure AD",
    "azure ad": "Azure AD",
    "azure-active-directory": "Azure AD",
    "azure active directory": "Azure AD",
    "entra": "Entra ID",
    "entraid": "Entra ID",
    "entra id": "Entra ID",
    "defender-atp": "Defender for Endpoint",
    "defender atp": "Defender for Endpoint",
    "defenderforendpoint": "Defender for Endpoint",
    "defender for endpoint": "Defender for Endpoint",
    "microsoft defender for endpoint": "Defender for Endpoint",
    "mde": "Defender for Endpoint",
    "office-365": "Microsoft 365",
    "office 365": "Microsoft 365",
    "m365": "Microsoft 365",
    "microsoft 365": "Microsoft 365",
    "intune": "Intune",
    "microsoft intune": "Intune",
    "log-analytics": "Log Analytics",
    "log analytics": "Log Analytics",
    "kql": "KQL",
    "kusto": "KQL",
    "group-policy": "Group Policy",
    "group policy": "Group Policy",
    "gpo": "Group Policy",
    "active-directory": "Active Directory",
    "active directory": "Active Directory",
    "windows": "Windows",
    "security": "Security",
    "azure": "Azure",
    "sentinel": "Microsoft Sentinel",
    "microsoft sentinel": "Microsoft Sentinel",
    "driver-store": "Driver Store",
    "driverstore": "Driver Store",
}

GENERIC_TAGS = {
    "tip",
    "tips",
    "readtip",
    "tool",
    "tools",
    "how-to",
    "blog",
    "post",
    "article",
    "microsoft",
}


def yaml_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def normalize_token(value: str) -> str:
    s = str(value).strip()
    s = re.sub(r"\s+", " ", s)
    s = s.replace("_", "-")
    s = re.sub(r"-+", "-", s)
    return s


def to_list(value) -> List[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [normalize_token(v) for v in value if str(v).strip()]
    return [normalize_token(value)] if str(value).strip() else []


def canonicalize_tag(token: str) -> str:
    raw = normalize_token(token)
    key = raw.lower()
    if key in CANONICAL_TAG_MAP:
        return CANONICAL_TAG_MAP[key]

    if raw.isupper() and len(raw) <= 5:
        return raw

    words = re.split(r"([\s\-/])", raw)
    out = []
    for w in words:
        if w in {" ", "-", "/"}:
            out.append(w)
            continue
        if not w:
            continue
        if len(w) <= 4 and w.isalpha() and w.upper() in {"AD", "DNS", "KQL", "API", "WMI", "WSUS"}:
            out.append(w.upper())
        else:
            out.append(w[0].upper() + w[1:].lower())
    return "".join(out)


def score_bucket(bucket: str, corpus: str, tokens_lower: List[str]) -> int:
    score = 0
    for kw in CATEGORY_KEYWORDS[bucket]:
        kw_l = kw.lower()
        if kw_l in tokens_lower:
            score += 4
        if kw_l in corpus:
            score += 2
    return score


def choose_category(title: str, slug: str, categories: List[str], tags: List[str]) -> str:
    token_pool = [normalize_token(x).lower() for x in (categories + tags)]
    corpus = " ".join([title or "", slug or "", " ".join(token_pool)]).lower()

    # Direct bucket hit from existing taxonomy first.
    direct_map = {
        "security": "Security",
        "windows": "Windows",
        "azure": "Azure",
        "office": "M365",
        "m365": "M365",
        "microsoft 365": "M365",
        "configmgr": "ConfigMgr",
        "configuration manager": "ConfigMgr",
        "sccm": "ConfigMgr",
        "intune": "Intune",
        "powershell": "PowerShell",
        "tip": "Tips-Tools",
        "tips": "Tips-Tools",
        "tool": "Tips-Tools",
        "tools": "Tips-Tools",
    }
    for t in token_pool:
        if t in direct_map:
            return direct_map[t]

    best = "Windows"
    best_score = -1
    for bucket in CATEGORY_ORDER:
        s = score_bucket(bucket, corpus, token_pool)
        if s > best_score:
            best = bucket
            best_score = s
    return best


def choose_tags(title: str, slug: str, category: str, categories: List[str], tags: List[str]) -> List[str]:
    source_tags = to_list(tags)
    source_categories = to_list(categories)

    candidates: List[Tuple[str, int]] = []
    corpus = f"{title or ''} {slug or ''}".lower()

    seen = set()
    for raw in source_tags + source_categories:
        c = canonicalize_tag(raw)
        c_l = c.lower()
        if not c_l or c_l in seen:
            continue
        seen.add(c_l)

        if c_l in GENERIC_TAGS:
            continue
        if c_l == category.lower():
            continue

        score = 0
        raw_l = normalize_token(raw).lower()
        if raw in source_tags:
            score += 3
        else:
            score += 1
        if raw_l in corpus or c_l in corpus:
            score += 3
        if len(c) >= 6:
            score += 1
        if c in {"Windows", "Security", "Azure"} and category == c:
            score -= 2

        candidates.append((c, score))

    candidates.sort(key=lambda x: (-x[1], x[0].lower()))
    selected = [c for c, _ in candidates[:2]]

    if not selected:
        fallback = "Tools" if category == "Tips-Tools" else category
        selected = [fallback]

    return selected[:2]


def strip_taxonomy_blocks(frontmatter_lines: List[str]) -> Tuple[List[str], int]:
    kept: List[str] = []
    insert_at = -1
    i = 0
    while i < len(frontmatter_lines):
        line = frontmatter_lines[i]
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):", line)
        if m and m.group(1).lower() in TARGET_KEYS:
            if insert_at == -1:
                insert_at = len(kept)
            i += 1
            while i < len(frontmatter_lines):
                next_line = frontmatter_lines[i]
                next_key = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):", next_line)
                if next_key:
                    break
                i += 1
            continue
        kept.append(line)
        i += 1

    if insert_at == -1:
        insert_at = len(kept)
    return kept, insert_at


def build_taxonomy_block(category: str, tags: List[str]) -> List[str]:
    lines = ["categories:", f"  - {yaml_quote(category)}", "tags:"]
    for t in tags:
        lines.append(f"  - {yaml_quote(t)}")
    return lines


def parse_frontmatter(content: str):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", content, flags=re.DOTALL)
    if not m:
        return None
    return m.group(1), m.group(2)


def strip_inline_quotes(value: str) -> str:
    s = value.strip()
    if len(s) >= 2 and ((s[0] == "'" and s[-1] == "'") or (s[0] == '"' and s[-1] == '"')):
        return s[1:-1]
    return s


def extract_meta_and_taxonomy(fm_text: str, fallback_slug: str) -> Tuple[str, str, List[str], List[str]]:
    lines = fm_text.splitlines()
    title = ""
    slug = fallback_slug
    categories: List[str] = []
    tags: List[str] = []

    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if not m:
            i += 1
            continue

        key = m.group(1).lower()
        rest = m.group(2).strip()

        if key == "title" and rest:
            title = strip_inline_quotes(rest)
        elif key == "slug" and rest:
            slug = strip_inline_quotes(rest)

        if key in TARGET_KEYS:
            collector = categories if key in {"categories", "category"} else tags

            if rest:
                if rest.startswith("["):
                    try:
                        parsed = yaml.safe_load(rest)
                        if isinstance(parsed, list):
                            collector.extend([normalize_token(x) for x in parsed if str(x).strip()])
                        elif parsed is not None:
                            collector.append(normalize_token(parsed))
                    except Exception:
                        collector.append(normalize_token(strip_inline_quotes(rest)))
                else:
                    collector.append(normalize_token(strip_inline_quotes(rest)))

            i += 1
            while i < len(lines):
                nxt = lines[i]
                nxt_key = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):", nxt)
                if nxt_key:
                    break
                item_match = re.match(r"^\s*-\s*(.+?)\s*$", nxt)
                if item_match:
                    collector.append(normalize_token(strip_inline_quotes(item_match.group(1))))
                i += 1
            continue

        i += 1

    return title, slug, categories, tags


def normalize_file(path: Path, apply: bool) -> Dict[str, int]:
    original = path.read_text(encoding="utf-8")
    parsed = parse_frontmatter(original)
    if not parsed:
        return {"changed": 0, "viol_cat": 0, "viol_tag": 0, "both": 0, "skipped": 1}

    fm_text, body = parsed
    title, slug, categories, tags = extract_meta_and_taxonomy(fm_text, path.parent.name)

    cat_count = len(categories)
    tag_count = len(tags)

    new_category = choose_category(title, slug, categories, tags)
    new_tags = choose_tags(title, slug, new_category, categories, tags)

    fm_lines = fm_text.splitlines()
    kept, insert_at = strip_taxonomy_blocks(fm_lines)
    block = build_taxonomy_block(new_category, new_tags)

    new_fm_lines = kept[:insert_at] + block + kept[insert_at:]
    new_content = "---\n" + "\n".join(new_fm_lines).rstrip() + "\n---\n" + body.lstrip("\n")

    changed = int(new_content != original)
    if apply and changed:
        path.write_text(new_content, encoding="utf-8")

    return {
        "changed": changed,
        "viol_cat": int(cat_count > 1),
        "viol_tag": int(tag_count > 2),
        "both": int(cat_count > 1 and tag_count > 2),
        "skipped": 0,
    }


def compliance_check(files: List[Path]) -> Dict[str, int]:
    result = {
        "total": 0,
        "cat0": 0,
        "cat1": 0,
        "cat2": 0,
        "cat3": 0,
        "cat4p": 0,
        "tag0": 0,
        "tag1": 0,
        "tag2": 0,
        "tag3": 0,
        "tag4": 0,
        "tag5": 0,
        "tag6": 0,
        "tag7p": 0,
        "viol_cat": 0,
        "viol_tag": 0,
        "both": 0,
        "parse_errors": 0,
    }

    for path in files:
        content = path.read_text(encoding="utf-8")
        parsed = parse_frontmatter(content)
        if not parsed:
            result["parse_errors"] += 1
            continue
        fm_text, _ = parsed
        _, _, categories, tags = extract_meta_and_taxonomy(fm_text, path.parent.name)

        c = len(categories)
        t = len(tags)
        result["total"] += 1

        if c == 0:
            result["cat0"] += 1
        elif c == 1:
            result["cat1"] += 1
        elif c == 2:
            result["cat2"] += 1
        elif c == 3:
            result["cat3"] += 1
        else:
            result["cat4p"] += 1

        if t == 0:
            result["tag0"] += 1
        elif t == 1:
            result["tag1"] += 1
        elif t == 2:
            result["tag2"] += 1
        elif t == 3:
            result["tag3"] += 1
        elif t == 4:
            result["tag4"] += 1
        elif t == 5:
            result["tag5"] += 1
        elif t == 6:
            result["tag6"] += 1
        else:
            result["tag7p"] += 1

        if c > 1:
            result["viol_cat"] += 1
        if t > 2:
            result["viol_tag"] += 1
        if c > 1 and t > 2:
            result["both"] += 1

    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize blog post taxonomy.")
    parser.add_argument("--apply", action="store_true", help="Write changes to files.")
    args = parser.parse_args()

    files = sorted(POST_ROOT.glob("**/index.md"))
    files = [p for p in files if "_migration-template" not in p.as_posix()]

    before = compliance_check(files)

    changed = 0
    skipped = 0
    for path in files:
        s = normalize_file(path, apply=args.apply)
        changed += s["changed"]
        skipped += s["skipped"]

    after = compliance_check(files)

    print(f"total_files={len(files)}")
    print(f"changed_files={changed}")
    print(f"skipped_files={skipped}")
    print("before=" + str(before))
    print("after=" + str(after))


if __name__ == "__main__":
    main()
