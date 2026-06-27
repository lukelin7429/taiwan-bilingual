#!/usr/bin/env python3
"""Idempotently wire the shared motion layer into hub pages.

For every hub page (one that links the shared /assets/css/main.css and is
not part of a self-contained sub-site) ensure three things exist:
  1. a <link> to /assets/css/motion.css   (hover + reveal styles)
  2. an inline <head> guard that sets html.mtn before first paint
     (flicker-free hide, with a no-JS / failed-JS failsafe)
  3. a <script src=/assets/js/motion.js>   (the reveal engine)

Re-running is safe: each piece is only added when its marker is absent.
Self-contained sub-sites (pingtung/nanjung has its own motion; chiayi &
taichung are embedded center/school sites) and the bespoke edward-huang
micro-site are skipped.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = ("pingtung/", "chiayi/", "taichung/", "edward-huang/", ".git/")

GUARD = ("<script>/*MTN-GUARD*/document.documentElement.classList.add('mtn');"
         "addEventListener('load',function(){setTimeout(function(){"
         "window.__mtn||document.documentElement.classList.remove('mtn')},1)})"
         "</script>")
CSS_LINK = '<link rel="stylesheet" href="/assets/css/motion.css">'
JS_TAG = '<script src="/assets/js/motion.js"></script>'

stats = {"css": 0, "guard": 0, "js": 0, "pages": 0, "skipped": 0}

for dirpath, _, files in os.walk(ROOT):
    for name in files:
        if not name.endswith(".html"):
            continue
        path = os.path.join(dirpath, name)
        rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
        if any(rel.startswith(d) or ("/" + d) in ("/" + rel) for d in SKIP_DIRS):
            continue
        html = open(path, encoding="utf-8").read()
        # hub page == links the shared main stylesheet
        if "assets/css/main.css" not in html:
            stats["skipped"] += 1
            continue
        orig = html
        # 1) motion.css link — insert right after the main.css link
        if "css/motion.css" not in html:
            html = re.sub(
                r'(<link[^>]+assets/css/main\.css"[^>]*>)',
                r"\1\n" + CSS_LINK, html, count=1)
            if CSS_LINK in html:
                stats["css"] += 1
        # 2) head guard — just before </head>
        if "/*MTN-GUARD*/" not in html:
            html = html.replace("</head>", GUARD + "\n</head>", 1)
            stats["guard"] += 1
        # 3) reveal engine — just before </body>
        if "assets/js/motion.js" not in html:
            html = html.replace("</body>", "  " + JS_TAG + "\n</body>", 1)
            stats["js"] += 1
        if html != orig:
            open(path, "w", encoding="utf-8").write(html)
            stats["pages"] += 1

print("pages changed : %d" % stats["pages"])
print("  + motion.css : %d" % stats["css"])
print("  + head guard : %d" % stats["guard"])
print("  + motion.js  : %d" % stats["js"])
print("non-hub skipped: %d" % stats["skipped"])
