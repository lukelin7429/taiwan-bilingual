#!/usr/bin/env python3
import re
import glob

REPO = "/Users/hayashikisshou/Documents/Claude/repos/taiwan-bilingual"
INDEX = f"{REPO}/schools/taichung/index.html"
WIP = f"{REPO}/.session-notes/taichung-wip"

# --- Build (chinese_name, township_english) -> slug for regular schools ---
name_town_to_slug = {}
for path in sorted(glob.glob(f"{WIP}/genlist_Batch*.txt")):
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line.startswith("- slug:"):
                continue
            # - slug: <slug> | <chinese name> | <Township> <zh> | level: <level>
            parts = [p.strip() for p in line[len("- slug:"):].split("|")]
            slug = parts[0]
            cname = parts[1]
            township_full = parts[2]  # e.g. "Beitun District 北屯區"
            township_en = township_full.split(" ")[0] + " District" if "District" not in township_full else township_full.split("  ")[0]
            # township_full already like "Beitun District 北屯區" -> take English part before the Chinese chars
            m = re.match(r"^([A-Za-z' .-]+District)", township_full)
            township_en = m.group(1).strip() if m else township_full
            key = (cname, township_en)
            if key in name_town_to_slug and name_town_to_slug[key] != slug:
                print(f"WARNING: duplicate key {key} -> {name_town_to_slug[key]} vs {slug}")
            name_town_to_slug[key] = slug

print(f"Loaded {len(name_town_to_slug)} (name, township) -> slug pairs")

# --- Build chinese_name -> slug for universities (county-wide, no township match needed) ---
uni_name_to_slug = {}
with open(f"{WIP}/genlist_universities.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line.startswith("- slug:"):
            continue
        parts = [p.strip() for p in line[len("- slug:"):].split("|")]
        slug = parts[0]
        cname = parts[1]
        uni_name_to_slug[cname] = slug

print(f"Loaded {len(uni_name_to_slug)} university name -> slug pairs")

with open(INDEX, encoding="utf-8") as f:
    html = f.read()

# --- Split into town blocks so we can match (name, township) tuples ---
# Each town block starts with <div class="cs-town-head">...<h3>English Name <span class="zh">...</span></h3>...
# and the block's srow-empty rows follow until the next cs-town-head or cs-he block.

town_head_re = re.compile(r'<h3>([A-Za-z\' .-]+ District)\s*<span class="zh">')

matched = 0
unmatched = []

def replace_school_row(m, township_en):
    full_row = m.group(0)
    cname = m.group("nm")
    key = (cname, township_en)
    slug = name_town_to_slug.get(key)
    if slug is None:
        unmatched.append((cname, township_en))
        return full_row
    global matched
    matched += 1
    level = m.group("level")
    lvltag = m.group("lvltag")
    lvlcls = m.group("lvlcls")
    return (
        f'<a class="srow" data-level="{level}" href="/schools/{slug}/">\n'
        f'        <div class="body">\n'
        f'          <span class="lvl-tag {lvlcls}">{lvltag}</span>\n'
        f'          <div class="nm">{cname}</div>\n'
        f'        </div>\n'
        f'        <span class="badge badge-yp">Profile</span></a>'
    )

ROW_RE = re.compile(
    r'<div class="srow srow-empty" data-level="(?P<level>[a-z-]+)">\s*'
    r'<div class="body">\s*'
    r'<span class="lvl-tag (?P<lvlcls>[a-z-]+)">(?P<lvltag>[A-Z]+)</span>\s*'
    r'<div class="nm">(?P<nm>[^<]+)</div>\s*'
    r'</div>\s*'
    r'<span class="badge badge-soon">Coming soon</span>\s*'
    r'</div>'
)

# Process per-town-block (skip the university section, level == "university")
def process_block(block_text, township_en):
    if township_en is None:
        return block_text  # university block handled separately
    return ROW_RE.sub(lambda m: replace_school_row(m, township_en), block_text)

# Split html on cs-town-head boundaries, keeping track of which township each chunk belongs to
pieces = re.split(r'(<div class="cs-town-head">.*?</div>)', html)
# pieces alternates: [pre, head1, body1, head2, body2, ...]
out = [pieces[0]]
current_township = None
i = 1
while i < len(pieces):
    head = pieces[i]
    body = pieces[i + 1] if i + 1 < len(pieces) else ""
    m = town_head_re.search(head)
    current_township = m.group(1) if m else None
    out.append(head)
    out.append(process_block(body, current_township))
    i += 2

html_new = "".join(out)

# --- University rows: separate regex, match by Chinese name inside <div class="nm">Eng <span class="zh">CH</span></div> ---
UNI_ROW_RE = re.compile(
    r'<div class="srow srow-empty" data-level="university">\s*'
    r'<div class="body">\s*'
    r'<span class="lvl-tag lvl-university">UNI</span>\s*'
    r'<div class="nm">(?P<eng>[^<]+)<span class="zh">(?P<zh>[^<]+)</span></div>\s*'
    r'<div class="cs-town-sub">(?P<sub>[^<]+)</div>\s*'
    r'</div>\s*'
    r'<span class="badge badge-soon">Coming soon</span>\s*'
    r'</div>'
)

uni_matched = 0
uni_unmatched = []

def replace_uni_row(m):
    global uni_matched
    eng = m.group("eng")
    zh = m.group("zh")
    sub = m.group("sub")
    slug = uni_name_to_slug.get(zh)
    if slug is None:
        uni_unmatched.append(zh)
        return m.group(0)
    uni_matched += 1
    return (
        f'<a class="srow" data-level="university" href="/schools/{slug}/">\n'
        f'        <div class="body">\n'
        f'          <span class="lvl-tag lvl-university">UNI</span>\n'
        f'          <div class="nm">{eng}<span class="zh">{zh}</span></div>\n'
        f'          <div class="cs-town-sub">{sub}</div>\n'
        f'        </div>\n'
        f'        <span class="badge badge-yp">Profile</span></a>'
    )

html_new = UNI_ROW_RE.sub(replace_uni_row, html_new)

print(f"School rows matched: {matched}, unmatched: {len(unmatched)}")
if unmatched:
    for u in unmatched:
        print("  UNMATCHED:", u)
print(f"University rows matched: {uni_matched}, unmatched: {len(uni_unmatched)}")
if uni_unmatched:
    for u in uni_unmatched:
        print("  UNMATCHED UNI:", u)

with open(INDEX, "w", encoding="utf-8") as f:
    f.write(html_new)

print("Done. Wrote", INDEX)
