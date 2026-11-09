#!/usr/bin/env python3
"""Build content/content.json from tools/content_src.py.

Adds tone-marked pinyin and zhuyin to every character, and with --check
prints any syllable that differs from pypinyin's reading so it can be
proofread (most differences are tone changes of 一/不 or Taiwan readings).

Usage:  python3 tools/build_content.py [--check]
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
import content_src as src  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HAN = re.compile(r"[㐀-鿿]")

INITIALS = [("zh", "ㄓ"), ("ch", "ㄔ"), ("sh", "ㄕ"), ("b", "ㄅ"), ("p", "ㄆ"), ("m", "ㄇ"), ("f", "ㄈ"),
            ("d", "ㄉ"), ("t", "ㄊ"), ("n", "ㄋ"), ("l", "ㄌ"), ("g", "ㄍ"), ("k", "ㄎ"), ("h", "ㄏ"),
            ("j", "ㄐ"), ("q", "ㄑ"), ("x", "ㄒ"), ("r", "ㄖ"), ("z", "ㄗ"), ("c", "ㄘ"), ("s", "ㄙ")]
FINALS = {
    "a": "ㄚ", "o": "ㄛ", "e": "ㄜ", "ai": "ㄞ", "ei": "ㄟ", "ao": "ㄠ", "ou": "ㄡ", "an": "ㄢ", "en": "ㄣ",
    "ang": "ㄤ", "eng": "ㄥ", "er": "ㄦ", "ong": "ㄨㄥ", "i": "ㄧ", "ia": "ㄧㄚ", "ie": "ㄧㄝ", "iao": "ㄧㄠ",
    "iu": "ㄧㄡ", "ian": "ㄧㄢ", "in": "ㄧㄣ", "iang": "ㄧㄤ", "ing": "ㄧㄥ", "iong": "ㄩㄥ", "u": "ㄨ",
    "ua": "ㄨㄚ", "uo": "ㄨㄛ", "uai": "ㄨㄞ", "ui": "ㄨㄟ", "uan": "ㄨㄢ", "un": "ㄨㄣ", "uang": "ㄨㄤ",
    "v": "ㄩ", "ve": "ㄩㄝ", "van": "ㄩㄢ", "vn": "ㄩㄣ",
}
WHOLE = {"yi": "i", "ya": "ia", "yo": "io", "ye": "ie", "yao": "iao", "you": "iu", "yan": "ian", "yin": "in",
         "yang": "iang", "ying": "ing", "yong": "iong", "yu": "v", "yue": "ve", "yuan": "van", "yun": "vn",
         "wu": "u", "wa": "ua", "wo": "uo", "wai": "uai", "wei": "ui", "wan": "uan", "wen": "un",
         "wang": "uang", "weng": "ueng"}
ZH_TONE = {"1": "", "2": "ˊ", "3": "ˇ", "4": "ˋ", "5": ""}
MARKS = {"a": "āáǎà", "e": "ēéěè", "i": "īíǐì", "o": "ōóǒò", "u": "ūúǔù", "ü": "ǖǘǚǜ"}


def zhuyin(syl):
    base, tone = syl[:-1], syl[-1]
    if base in ("zhi", "chi", "shi", "ri", "zi", "ci", "si"):
        z = dict(INITIALS)[base[:-1]]
    elif base in WHOLE:
        z = "ㄨㄥ" if base == "weng" else FINALS[WHOLE[base]]
    else:
        ini = next(((p, b) for p, b in INITIALS if base.startswith(p)), ("", ""))
        fin = base[len(ini[0]):]
        if ini[0] in ("j", "q", "x") and fin.startswith("u"):
            fin = "v" + fin[1:]
        z = ini[1] + FINALS[fin]
    return ("˙" + z) if tone == "5" else z + ZH_TONE[tone]


def marked(syl):
    base, tone = syl[:-1].replace("v", "ü"), int(syl[-1])
    if tone == 5:
        return base
    for v in ("a", "e"):
        if v in base:
            return base.replace(v, MARKS[v][tone - 1], 1)
    if "ou" in base:
        return base.replace("o", MARKS["o"][tone - 1], 1)
    i = max(base.rfind(v) for v in "iouü")
    return base[:i] + MARKS[base[i]][tone - 1] + base[i + 1:]


def tokens(zh, py, where):
    syls = py.split()
    chars = HAN.findall(zh)
    if len(syls) != len(chars):
        sys.exit(f"{where}: {len(chars)} characters but {len(syls)} syllables in {zh!r}")
    out, it = [], iter(syls)
    for ch in zh:
        if HAN.match(ch):
            s = next(it)
            out.append({"c": ch, "p": marked(s), "z": zhuyin(s), "n": s})
        else:
            out.append({"c": ch})
    return out


def check(all_items):
    from pypinyin import Style, pinyin
    diffs = 0
    for where, toks in all_items:
        text = "".join(t["c"] for t in toks if "n" in t)
        ref = [r[0] for r in pinyin(text, style=Style.TONE3, neutral_tone_with_five=True)]
        mine = [t["n"] for t in toks if "n" in t]
        for ch, a, b in zip(text, mine, ref):
            if a != b:
                diffs += 1
                print(f"  {where:28} {ch}  mine={a:8} pypinyin={b}")
    print(f"{diffs} differences to review")


def main():
    units, review = [], []
    for u in src.UNITS:
        uid = u["id"]
        unit = {k: u[k] for k in ("id", "emoji", "color", "title", "zh", "intro", "write", "culture")}
        unit["hv"] = u.get("hv")
        unit["phrases"], unit["signs"] = [], []
        for kind in ("phrases", "signs"):
            for i, p in enumerate(u[kind]):
                t = tokens(p["zh"], p["py"], f"{uid}/{kind}/{i}")
                review.append((f"{uid}/{kind}/{i}", t))
                item = {"id": f"{uid}-{kind[0]}{i}", "zh": p["zh"], "t": t, "en": p["en"]}
                for k in ("note", "hv"):
                    if p.get(k):
                        item[k] = p[k]
                unit[kind].append(item)
        d = u["dialogue"]
        lines = []
        for i, (who, zh, py, en) in enumerate(d["lines"]):
            t = tokens(zh, py, f"{uid}/dialogue/{i}")
            review.append((f"{uid}/dialogue/{i}", t))
            lines.append({"id": f"{uid}-d{i}", "who": who, "zh": zh, "t": t, "en": en})
        unit["dialogue"] = {"title": d["title"], "cast": d["cast"], "lines": lines, "quiz": d["quiz"]}
        units.append(unit)
    out = {"units": units, "coming": src.COMING}
    with open(os.path.join(ROOT, "content", "content.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    n = sum(len(u["phrases"]) + len(u["signs"]) + len(u["dialogue"]["lines"]) for u in units)
    print(f"{len(units)} units, {n} items with audio")
    if "--check" in sys.argv:
        check(review)


if __name__ == "__main__":
    main()
