#!/usr/bin/env python3
import json
import re
import os
from pypinyin import pinyin, Style

REPO = "/Users/hayashikisshou/Documents/Claude/repos/taiwan-bilingual"
WIP = f"{REPO}/.session-notes/kaohsiung-wip"

data = json.load(open(f"{WIP}/by_town.json", encoding="utf-8"))
by_town = data["by_town"]
universities = data["universities"]

# --- polyphone corrections (standing checklist: 重、都、假、藏、量、少、率、長) ---
POLYPHONE_FIX = {
    "重": "chong",
    "都": "du",
    "假": "jia",
    "藏": "cang",
    "量": "liang",
    "少": "shao",
    "率": "lv",
    "長": "chang",
}

ADMIN_PREFIXES = ["高雄市立", "高雄市", "國立", "私立", "高雄縣立"]

VOC_KEYWORDS = ["高級工業", "高級工商", "高級商工", "高級農工", "高級家事商業", "職業學校", "高級海事"]


def strip_prefix(name):
    for p in ADMIN_PREFIXES:
        if name.startswith(p):
            return name[len(p):]
    return name


SUFFIXES = [
    "高級家事商業職業學校", "高級商工職業學校", "高級工商職業學校", "高級農工職業學校",
    "高級海事水產職業學校", "高級工業職業學校", "高級商業職業學校",
    "高級中等學校", "高級中學",
    "國民中小學", "國中小", "國民小學", "國民中學", "國小", "國中",
]


def strip_suffix(name):
    # returns (base, suffix_type) — longest suffix first so compound vocational
    # names don't leave a giant untranslated tail
    for suf in SUFFIXES:
        if name.endswith(suf):
            return name[: -len(suf)], suf
    return name, None


def to_pinyin(text):
    # Site convention: syllables within one Chinese name are concatenated with
    # NO separator (e.g. 成功 -> "chenggong", not "cheng-gong"). Hyphens are
    # reserved for joining a township/meaning qualifier to the base, and for
    # the trailing level-tag suffix.
    parts = []
    for ch in text:
        if not re.match(r"[一-鿿]", ch):
            continue
        if ch in POLYPHONE_FIX:
            parts.append(POLYPHONE_FIX[ch])
        else:
            py = pinyin(ch, style=Style.NORMAL, heteronym=False)
            parts.append(py[0][0] if py and py[0] else "")
    return "".join(p for p in parts if p)


def base_slug_for(name, level):
    is_voc = any(k in name for k in VOC_KEYWORDS)
    stripped = strip_prefix(name)
    base, suf = strip_suffix(stripped)
    if not base:
        return None, "EMPTY_BASE_AFTER_STRIP"
    py = to_pinyin(base)
    if not py:
        return None, "EMPTY_PINYIN"
    if is_voc:
        tag = "vs"
    elif level == "elementary":
        tag = "es"
    elif level == "junior-high":
        tag = "jh"
    elif level == "senior-high":
        tag = "hs"
    else:
        tag = level
    return f"{py}-{tag}", None


# --- collect all (township, name, level) rows ---
rows = []
for t in by_town:
    for s in t["schools"]:
        rows.append({"township_en": t["township_en"], "township_zh": t["township_zh"], "name": s["name"], "level": s["level"]})

# --- cross-township name collisions (need county-prefix disambiguation) ---
from collections import defaultdict
name_towns = defaultdict(set)
for r in rows:
    name_towns[r["name"]].add(r["township_en"])
cross_collisions = {n for n, towns in name_towns.items() if len(towns) > 1}

# --- existing repo slugs, for global collision check ---
existing_slugs = set(os.listdir(f"{REPO}/schools"))

# --- manual overrides for known special cases ---
MANUAL_SLUGS = {
    ("高雄市立高雄高級中學", "senior-high"): "xiongzhong-hs",       # flagship general HS, known as 雄中
    ("高雄市立高雄高級商業職業學校", "senior-high"): "kaoshang-vs",  # known as 高商
    ("高雄市立高雄高級工業職業學校", "senior-high"): "kaogong-vs",   # known as 高工 (gongye-vs taken by Taichung)
    ("國立高雄師範大學附屬高級中學", "senior-high"): "nknu-fushu-hs",
    ("六龜高級中學附屬國民中學", "junior-high"): "liougui-fushu-jh",
    ("國立高科實驗高級中等學校", "senior-high"): "gaoke-hs",   # combined JH+SH, one page
    ("國立高科實驗高級中等學校", "junior-high"): "gaoke-hs",
    ("巴楠花部落中小學", "junior-high"): "banahua-jhes",       # combined JH+ES, one page
    ("巴楠花部落中小學", "elementary"): "banahua-jhes",
    ("翠屏國民中小學", "junior-high"): "cuiping-jhes",         # K-9, single row but combined name
    # same-pinyin different-character collisions (not caught by identical-name check)
    ("右昌國小", "elementary"): "youchang-es",                  # Nanzih — keep plain, older/primary place name
    ("油廠國小", "elementary"): "youchang-refinery-es",         # Nanzih — same pinyin as 右昌, disambiguated by meaning (oil refinery)
    ("烏林國小", "elementary"): "renwu-wulin-es",                # Renwu — same pinyin as 五林 (Ciaotou), disambiguated by township
    ("五林國小", "elementary"): "ciaotou-wulin-es",              # Ciaotou — same pinyin as 烏林 (Renwu), disambiguated by township
    ("福安國小", "elementary"): "meinong-fuan-es",               # Meinong — same pinyin as 復安 (Alian), disambiguated by township
    ("復安國小", "elementary"): "alian-fuan-es",                 # Alian — same pinyin as 福安 (Meinong), disambiguated by township
    ("姑山國小", "elementary"): "dashu-gushan-es",               # Dashu — same pinyin as 鼓山 (Gushan District's own-name school), disambiguated by township
}

# township Chinese name -> pinyin qualifier (strip trailing 區), for disambiguating
# cross-township same-name schools with a REAL township-name qualifier (matching
# the pypinyin/hanyu-pinyin style already used site-wide), not the district's own
# English tongyong-pinyin name (e.g. "Cianjhen") which would be inconsistent.
township_pinyin = {}
for t in by_town:
    tzh = t["township_zh"]
    base = tzh[:-1] if tzh.endswith("區") else tzh
    township_pinyin[t["township_en"]] = to_pinyin(base)

results = []
issues = []

for r in rows:
    key = (r["name"], r["level"])
    if key in MANUAL_SLUGS:
        slug = MANUAL_SLUGS[key]
    else:
        slug, err = base_slug_for(r["name"], r["level"])
        if err:
            issues.append((r["township_en"], r["name"], r["level"], err))
            slug = f"UNRESOLVED__{r['name']}"
        elif r["name"] in cross_collisions:
            tq = township_pinyin.get(r["township_en"], "")
            base_py = slug.rsplit("-", 1)[0]  # strip the -es/-jh/-hs tag
            tag = slug.rsplit("-", 1)[1]
            if tq and tq == base_py:
                # school name already matches its own district's name — no need
                # to double it (avoids Taichung-style "gushan-gushan" redundancy)
                pass
            else:
                slug = f"{tq}-{base_py}-{tag}"
    r["slug"] = slug
    results.append(r)

# --- second pass: any candidate slug that collides with an EXISTING repo slug
# (i.e. another county already built a same-named/same-pinyin school) gets the
# flat "ks-" county-code prefix, per the standing cross-county-collision
# convention (kl- for Keelung, hc- for Hsinchu County, tc- for Taichung, etc.) ---
for r in results:
    if r["slug"] in MANUAL_SLUGS.values():
        continue  # manual overrides are already final/deliberate
    if r["slug"] in existing_slugs:
        r["slug"] = f"ks-{r['slug']}"

# --- final collision check: against existing repo + within this batch ---
slug_first_seen = {}
for r in results:
    slug = r["slug"]
    if slug in existing_slugs:
        issues.append((r["township_en"], r["name"], r["level"], f"COLLIDES_WITH_EXISTING_REPO_SLUG:{slug}"))
    if slug in slug_first_seen and slug_first_seen[slug] != r["name"]:
        issues.append((r["township_en"], r["name"], r["level"], f"INTERNAL_SLUG_COLLISION_WITH:{slug_first_seen[slug]}->{slug}"))
    slug_first_seen.setdefault(slug, r["name"])

print(f"Total rows: {len(results)}")
print(f"Cross-township collisions found: {len(cross_collisions)} -> {sorted(cross_collisions)}")
print(f"Issues: {len(issues)}")
for i in issues:
    print(" ISSUE:", i)

with open(f"{WIP}/slugs.json", "w", encoding="utf-8") as f:
    json.dump({"rows": results, "universities": universities}, f, ensure_ascii=False, indent=2)

print("Wrote", f"{WIP}/slugs.json")
