#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Taiwan Bilingual Hub — build the site-wide search index and wire the search
box into the shared Hub topbar.

Outputs:
  - /search.json   one flat index of every public page (incl. bespoke sub-sites,
                   so everything is findable from the search palette)
  - injects the search trigger button + assets into the 287 pages that carry
    the standard Hub topbar (`<nav class="topbar-nav">`)

Re-run after adding or renaming pages (idempotent):
    python3 scripts/build_search.py
"""
import os, re, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSS_LINK = '<link rel="stylesheet" href="/assets/css/search.css">'
JS_TAG   = '<script defer src="/assets/js/search.js"></script>'
BUTTON = (
    '\n    <button type="button" class="nav-search-btn" id="siteSearchBtn" '
    'aria-label="Search this site" title="Search (press /)">'
    '<svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"></circle>'
    '<line x1="21" y1="21" x2="16.5" y2="16.5"></line></svg>'
    '<span class="nav-search-label">Search</span></button>'
)

TAG_RE    = re.compile(r"<[^>]+>")
SCRIPT_RE = re.compile(r"<(script|style|svg)\b.*?</\1>", re.S | re.I)
BLOCK_RE  = re.compile(r"<(header|footer|nav)\b.*?</\1>", re.S | re.I)
WS_RE     = re.compile(r"\s+")
TITLE_RE  = re.compile(r"<title>(.*?)</title>", re.S | re.I)
DESC_RE   = re.compile(r'<meta[^>]+name=["\']description["\'][^>]*content=["\'](.*?)["\']', re.S | re.I)
BODY_RE   = re.compile(r"<body\b[^>]*>(.*?)</body>", re.S | re.I)
TOPNAV_RE = re.compile(r'(<nav class="topbar-nav".*?</nav>)', re.S)
CHROME_RE = re.compile(
    r'<button[^>]*class="(?:nav-search-btn|nav-toggle)"[^>]*>.*?</button>'
    r'|<a class="topbar-brand".*?</a>', re.S | re.I)

def clean(text, limit=300):
    text = html.unescape(WS_RE.sub(" ", text)).strip()
    return text[:limit].rstrip() + ("…" if len(text) > limit else "")

def strip_title(t):
    t = html.unescape(t).strip()
    t = re.split(r"\s+[—–]\s+Taiwan Bilingual Hub", t)[0]
    t = re.split(r"\s+·\s+臺灣雙語資源網", t)[0]
    return t.strip()

def url_for(rel):
    rel = rel.replace(os.sep, "/")
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[:-len("index.html")]
    return "/" + rel

def section_of(rel):
    rel = rel.replace(os.sep, "/")
    p = rel.split("/")
    top = p[0]
    M = {
        "counties": "Counties", "partners": "Partners", "resources": "Resources",
        "schools": "Schools", "get-started": "Get Started", "contact": "Contact",
        "edward-huang": "Edward Huang", "dom-jones": "Teacher Dom",
        "bilingual-2030": "Bilingual 2030", "taichung": "Taichung",
    }
    if rel == "index.html":
        return "Hub"
    if top == "pingtung" and len(p) > 1 and p[1] == "nanjung":
        return "南榮國中 Nanjung"
    if top == "chiayi" and len(p) > 1 and p[1] == "eerc":
        return "嘉義 EERC"
    if top in ("pingtung", "chiayi"):
        return top.capitalize()
    return M.get(top, top.replace("-", " ").title())

def text_of(raw):
    m = BODY_RE.search(raw)
    chunk = m.group(1) if m else raw
    chunk = SCRIPT_RE.sub(" ", chunk)
    chunk = CHROME_RE.sub(" ", chunk)
    chunk = BLOCK_RE.sub(" ", chunk)
    return TAG_RE.sub(" ", chunk)

# ---------- collect pages ----------
entries, injected = [], 0
for dp, dns, fns in os.walk(ROOT):
    dns[:] = [d for d in dns if not d.startswith(".")]
    for fn in fns:
        if not fn.endswith(".html"):
            continue
        full = os.path.join(dp, fn)
        rel = os.path.relpath(full, ROOT).replace(os.sep, "/")
        raw = open(full, encoding="utf-8").read()
        if 'http-equiv="refresh"' in raw:           # redirect stub
            continue
        mt = TITLE_RE.search(raw)
        title = strip_title(mt.group(1)) if mt else None
        if not title:
            continue
        md = DESC_RE.search(raw)
        desc = (html.unescape(md.group(1)) + " ") if md else ""
        entries.append({
            "title": title,
            "url": url_for(rel),
            "section": section_of(rel),
            "body": clean(desc + text_of(raw)),
        })
        # inject into standard Hub topbar pages
        if "id=\"siteSearchBtn\"" not in raw and TOPNAV_RE.search(raw):
            new = raw
            if CSS_LINK not in new and "</head>" in new:
                new = new.replace("</head>", "  " + CSS_LINK + "\n</head>", 1)
            new = TOPNAV_RE.sub(lambda m: m.group(1) + BUTTON, new, count=1)
            if JS_TAG not in new and "</body>" in new:
                new = new.replace("</body>", "  " + JS_TAG + "\n</body>", 1)
            if new != raw:
                open(full, "w", encoding="utf-8").write(new)
                injected += 1

# de-dup + sort + write
seen, uniq = set(), []
for e in sorted(entries, key=lambda e: e["url"]):
    if e["url"] in seen:
        continue
    seen.add(e["url"]); uniq.append(e)
json.dump(uniq, open(os.path.join(ROOT, "search.json"), "w"),
          ensure_ascii=False, separators=(",", ":"))
print("search.json: %d pages indexed" % len(uniq))
print("search box injected into %d Hub pages" % injected)
