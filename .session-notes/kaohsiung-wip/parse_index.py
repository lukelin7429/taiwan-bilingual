#!/usr/bin/env python3
import re
import json
import html as html_lib

REPO = "/Users/hayashikisshou/Documents/Claude/repos/taiwan-bilingual"
INDEX = f"{REPO}/schools/kaohsiung/index.html"
WIP = f"{REPO}/.session-notes/kaohsiung-wip"

with open(INDEX, encoding="utf-8") as f:
    html = f.read()

# --- Universities section ---
uni_block_m = re.search(r'<div class="cs-he-head">.*?</div>\s*<p class="note">.*?</p>\s*<div class="cs-list">(.*?)</div>\s*</div>\s*<div class="cs-town"', html, re.S)
universities = []
if uni_block_m:
    block = uni_block_m.group(1)
    for m in re.finditer(
        r'<div class="srow srow-empty" data-level="university">\s*'
        r'<div class="body">\s*'
        r'<span class="lvl-tag lvl-university">UNI</span>\s*'
        r'<div class="nm">(?P<eng>[^<]+)<span class="zh">(?P<zh>[^<]+)</span></div>\s*'
        r'<div class="cs-town-sub">(?P<sub>[^<]+)</div>',
        block,
    ):
        universities.append({"eng": m.group("eng").strip(), "zh": m.group("zh").strip(), "sub": m.group("sub").strip(),
                              "badge": "soon"})

# --- Town blocks ---
town_head_re = re.compile(
    r'<div class="cs-town-head"><span class="cs-zip">(?P<zip>\d+)</span>'
    r'<h3>(?P<eng>.+? District(?:\s*\([^)]*\))?)\s*<span class="zh">(?P<zh>[^<]+)</span></h3>'
    r'<span class="cs-count">(?P<count>\d+) schools</span></div>'
)

pieces = re.split(r'(<div class="cs-town-head">.*?</div>)', html)
by_town = []
i = 1
while i < len(pieces):
    head = pieces[i]
    body = pieces[i + 1] if i + 1 < len(pieces) else ""
    m = town_head_re.search(head)
    if not m:
        i += 2
        continue
    township_en = html_lib.unescape(m.group("eng"))
    township_zh = m.group("zh")
    zipc = m.group("zip")
    schools = []
    # match both empty (soon) rows and any already-linked (badge-full/official) rows, just in case
    for sm in re.finditer(
        r'<(?:div class="srow srow-empty"|a class="srow") data-level="(?P<level>[a-z-]+)"[^>]*>\s*'
        r'<div class="body">\s*'
        r'<span class="lvl-tag [a-z-]+">[A-Z]+</span>\s*'
        r'<div class="nm">(?P<nm>[^<]+)</div>\s*'
        r'</div>\s*'
        r'<span class="badge badge-(?P<badgetype>[a-z]+)">',
        body,
    ):
        schools.append({"name": sm.group("nm").strip(), "level": sm.group("level"), "badge": sm.group("badgetype")})
    by_town.append({"township_en": township_en, "township_zh": township_zh, "zip": zipc, "count_declared": int(m.group("count")), "schools": schools})
    i += 2

total_schools = sum(len(t["schools"]) for t in by_town)
print(f"Districts parsed: {len(by_town)}")
print(f"Total township schools parsed: {total_schools}")
print(f"Universities parsed: {len(universities)}")

# sanity check declared count vs parsed count
mismatches = [(t["township_en"], t["count_declared"], len(t["schools"])) for t in by_town if t["count_declared"] != len(t["schools"])]
if mismatches:
    print("MISMATCHES (declared vs parsed):")
    for mm in mismatches:
        print(" ", mm)
else:
    print("All district counts match declared counts.")

already_linked = [s["name"] for t in by_town for s in t["schools"] if s["badge"] != "soon"]
print(f"Already-linked (non-soon) rows: {already_linked}")

with open(f"{WIP}/by_town.json", "w", encoding="utf-8") as f:
    json.dump({"by_town": by_town, "universities": universities}, f, ensure_ascii=False, indent=2)

print("Wrote", f"{WIP}/by_town.json")
