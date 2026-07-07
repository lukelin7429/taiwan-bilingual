#!/usr/bin/env python3
"""Backfill self-referencing <link rel="canonical"> into every content page.

Why: without an explicit canonical, tracking-param'd or otherwise duplicate
copies of a URL confuse Google about which version to index. A self-referencing
canonical on the clean URL tells Google "this is the original."
Mirrors changhua-bilingual/scripts/add_canonical.py.

Idempotent. Run from anywhere:  python3 scripts/add_canonical.py [--apply]
Without --apply it does a dry run (lists what it would change, touches nothing).
"""

import re
import sys
from pathlib import Path

SITE = "https://taiwan-bilingual.org"
ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = {"scripts", "assets", ".claude", ".session-notes", ".git"}

VIEWPORT_RX = re.compile(r'(<meta\s+name=["\']viewport["\'][^>]*>)', re.I)
HEAD_RX = re.compile(r'(<head[^>]*>)', re.I)
CANONICAL_RX = re.compile(r'rel=["\']canonical["\']', re.I)


def canonical_url(relpath: str) -> str:
    p = relpath.replace("\\", "/").lstrip("./").lstrip("/")
    if p == "index.html":
        return SITE + "/"
    if p.endswith("/index.html"):
        return SITE + "/" + p[: -len("index.html")]
    return SITE + "/" + p


def insert_canonical(html: str, url: str):
    if CANONICAL_RX.search(html):
        return html, False
    tag = f'\n  <link rel="canonical" href="{url}">'
    m = VIEWPORT_RX.search(html)
    if m:
        i = m.end()
        return html[:i] + tag + html[i:], True
    m = HEAD_RX.search(html)
    if m:
        i = m.end()
        return html[:i] + tag + html[i:], True
    return html, False


def main():
    apply = "--apply" in sys.argv
    changed = skipped_have = skipped_nohead = skipped_excluded = 0
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT)
        parts = set(rel.parts)
        if parts & SKIP_DIRS:
            skipped_excluded += 1
            continue
        html = path.read_text(encoding="utf-8")
        if CANONICAL_RX.search(html):
            skipped_have += 1
            continue
        url = canonical_url(str(rel))
        new_html, ok = insert_canonical(html, url)
        if not ok:
            skipped_nohead += 1
            continue
        changed += 1
        if apply:
            path.write_text(new_html, encoding="utf-8")
        else:
            print(f"  + {rel}  ->  {url}")

    verb = "Inserted" if apply else "Would insert"
    print(
        f"\n{verb} canonical in {changed} files.  "
        f"already-had={skipped_have}  no-head(fragment)={skipped_nohead}  "
        f"excluded={skipped_excluded}"
    )
    if not apply:
        print("Dry run. Re-run with --apply to write changes.")


if __name__ == "__main__":
    main()
