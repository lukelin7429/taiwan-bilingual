#!/usr/bin/env python3
"""Give every hub page's .pg-band banner its own colour (Changhua-style).

The light/shadow animation lives in assets/css/motion.css; each page just
declares its colour as --b1/--b2/--b3 on .pg-band. This script rewrites the
page's existing `.pg-band{background:linear-gradient(...);...}` rule into the
variable form, preserving padding. Idempotent: pages already carrying --b1 are
left alone.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# deep -> mid -> edge, all carry white text comfortably
PALETTE = {
    "bilingual-2030":  ("#1b2769", "#2f3fa0", "#4150c4"),  # indigo
    "counties":        ("#0c4f57", "#0e8a8f", "#16a7a0"),  # teal
    "partners":        ("#3b1361", "#6d2b9b", "#8a39bd"),  # violet
    "schools":         ("#114b2e", "#1f7a44", "#2f9457"),  # emerald
    # resources sub-sections (more specific paths first)
    "resources/word-of-the-day":  ("#9d174d", "#be185d", "#db2777"),  # rose
    "resources/basic-sentences":  ("#0c3f74", "#1769b0", "#2487d0"),  # sky
    "resources/bilingual-campus": ("#0a4f63", "#0e8aa0", "#15a8c0"),  # cyan
    "resources/gept-speaking":    ("#3a1d6b", "#5b34a8", "#7048c8"),  # purple
    "resources/one-minute":       ("#b45309", "#d97706", "#ea7317"),  # orange
    "resources/tutoring":         ("#0d5040", "#128a6a", "#17a37f"),  # teal-green
    "resources/booklets/basic":        ("#123a6b", "#1f5fa0", "#2a7bc0"),  # blue
    "resources/booklets/intermediate": ("#14502e", "#237a44", "#2f9457"),  # green
    "resources/booklets/advanced":     ("#6e1414", "#a82828", "#c23a3a"),  # red
    "resources/booklets/conversation": ("#3a1d6b", "#5b34a8", "#7048c8"),  # purple
    "resources/booklets/description":  ("#7a3a0a", "#c2680f", "#e0861a"),  # amber
    "resources/booklets/everyday":     ("#0c4f57", "#0e8a8f", "#16a7a0"),  # teal
    "resources/booklets":  ("#25305c", "#3f4f8a", "#5566a8"),  # slate-indigo (index)
    "resources":           ("#7a3a0a", "#c2680f", "#e0861a"),  # amber (hub index)
}
DEFAULT = ("#1b5c44", "#2f7d6f", "#3a7766")  # jade (unmapped fallback)

PG_RE = re.compile(r"\.pg-band\{[^}]*\}")
PAD_RE = re.compile(r"padding:([^;}]+)")


def colour_for(relpath):
    rel = relpath.replace(os.sep, "/")
    # longest matching key wins
    best = None
    for key in PALETTE:
        if ("/" + key + "/") in ("/" + rel) or ("/" + key) in ("/" + rel):
            if best is None or len(key) > len(best):
                best = key
    return PALETTE[best] if best else DEFAULT


def convert(path, relpath):
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    if "--b1:" in src and ".pg-band{" in src and "--b1" in src.split(".pg-band{",1)[1][:200]:
        return "skip"  # already migrated
    m = PG_RE.search(src)
    if not m:
        return "no-band"
    block = m.group(0)
    pad = PAD_RE.search(block)
    padding = pad.group(1).strip() if pad else "56px 0 58px"
    b1, b2, b3 = colour_for(relpath)
    new = (".pg-band{--b1:%s;--b2:%s;--b3:%s;color:#fff;padding:%s;"
           "position:relative;overflow:hidden;}" % (b1, b2, b3, padding))
    src = src[:m.start()] + new + src[m.end():]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(src)
    return "%s -> %s" % (relpath, (b1, b2, b3))


def main():
    changed = 0
    for dirpath, _, files in os.walk(ROOT):
        if "/.git" in dirpath:
            continue
        for fn in files:
            if not fn.endswith(".html"):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, ROOT)
            with open(path, encoding="utf-8") as fh:
                if "pg-band{" not in fh.read():
                    continue
            res = convert(path, rel)
            if res not in ("skip", "no-band"):
                changed += 1
                print(res)
            elif res == "skip":
                print("  (skip, already migrated) " + rel)
    print("\n%d pages recoloured." % changed)


if __name__ == "__main__":
    main()
