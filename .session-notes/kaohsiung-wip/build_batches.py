#!/usr/bin/env python3
import json

REPO = "/Users/hayashikisshou/Documents/Claude/repos/taiwan-bilingual"
WIP = f"{REPO}/.session-notes/kaohsiung-wip"

slugs_data = json.load(open(f"{WIP}/slugs.json", encoding="utf-8"))
rows = slugs_data["rows"]
universities = slugs_data["universities"]

by_district = {}
for r in rows:
    by_district.setdefault(r["township_en"], []).append(r)

TARGET = 20
MAX_SINGLE = 24  # districts at or under this size stay whole

districts = sorted(by_district.items(), key=lambda kv: -len(kv[1]))

batches = []  # list of lists of rows

# Step 1: split oversized districts into sub-batches of ~TARGET each
standalone = []
small = []
for name, schools in districts:
    if len(schools) > MAX_SINGLE:
        # split into chunks of ~TARGET
        n_chunks = max(2, round(len(schools) / TARGET))
        chunk_size = -(-len(schools) // n_chunks)  # ceil
        for i in range(0, len(schools), chunk_size):
            standalone.append(schools[i:i + chunk_size])
    elif len(schools) >= 14:
        standalone.append(schools)
    else:
        small.append((name, schools))

# Step 2: greedily combine small districts into batches close to TARGET
small.sort(key=lambda kv: -len(kv[1]))
combined = []
cur = []
cur_size = 0
for name, schools in small:
    if cur_size + len(schools) > TARGET + 4 and cur:
        combined.append(cur)
        cur = []
        cur_size = 0
    cur.extend(schools)
    cur_size += len(schools)
if cur:
    combined.append(cur)

batches = standalone + combined

print(f"Total batches: {len(batches)}")
for i, b in enumerate(batches, 1):
    towns = sorted(set(r["township_en"] for r in b))
    print(f"Batch{i:02d}: {len(b)} schools — {', '.join(towns)}")

total = sum(len(b) for b in batches)
print("Total schools across batches:", total, "(expected 348)")

# --- write genlist files ---
for i, b in enumerate(batches, 1):
    lines = [f"=== Batch{i:02d} ==="]
    for r in b:
        lines.append(f"- slug: {r['slug']} | {r['name']} | {r['township_en']} {r['township_zh']} | level: {r['level']}")
    with open(f"{WIP}/genlist_Batch{i:02d}.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

# --- universities genlist ---
lines = ["=== Universities ==="]
for u in universities:
    lines.append(f"- slug: {u['slug']} | {u['zh']} | {u['sub']}")
with open(f"{WIP}/genlist_universities.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

with open(f"{WIP}/batch_plan.json", "w", encoding="utf-8") as f:
    json.dump({"n_batches": len(batches), "batches": [[r["slug"] for r in b] for b in batches]}, f, ensure_ascii=False, indent=2)

print("Wrote genlist files + batch_plan.json")
