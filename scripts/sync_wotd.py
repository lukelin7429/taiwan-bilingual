#!/usr/bin/env python3
"""Sync Word of the Day data from the Changhua Bilingual Hub into this repo.
Run whenever Changhua updates its WOTD. Read-only on the Changhua side.
    python3 scripts/sync_wotd.py
"""
import json, os, shutil, sys
SRC = os.path.expanduser("~/Documents/Claude/repos/changhua-bilingual/assets/data/wotd.json")
DST = os.path.join(os.path.dirname(__file__), "..", "assets", "data", "wotd.json")
if not os.path.exists(SRC):
    sys.exit("Source not found: " + SRC)
src = json.load(open(SRC))
n = len(src.get("items", []))
shutil.copyfile(SRC, DST)
print(f"Synced {n} Word-of-the-Day entries → assets/data/wotd.json")
