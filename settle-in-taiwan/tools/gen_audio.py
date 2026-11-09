#!/usr/bin/env python3
"""Record every phrase, sign and dialogue line with Microsoft's Taiwan voices.

Each phrase and sign gets a female and a male voice; dialogue lines use the
voice of their speaker. Every recording is made at normal speed and at a slow
speed (the app's 0.5x setting plays the slow file, so it sounds natural).

Needs edge-tts with the patched WSS_URL (see README):
  PYTHONPATH=~/Developer/twrses-twhist-tools/tts \
    ~/.local/pipx/venvs/edge-tts/bin/python tools/gen_audio.py

Existing files are kept, so re-running only records what is new.
Output: audio/<hash>.mp3 and audio/index.json (item id -> voice -> speed -> file).
"""
import asyncio
import hashlib
import json
import os

import edge_tts

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "audio")
VOICES = {"F": "zh-TW-HsiaoChenNeural", "M": "zh-TW-YunJheNeural"}
RATES = {"n": "+0%", "s": "-45%"}
# Who speaks each dialogue role.
CAST = {"hello": {"A": "M", "B": "F"}, "store": {"A": "F", "B": "M"}, "food": {"A": "M", "B": "F"},
        "numbers": {"A": "M", "B": "F"}, "transit": {"A": "F", "B": "M"}, "campus": {"A": "M", "B": "F"},
        "health": {"A": "M", "B": "F"}, "home": {"A": "F", "B": "M"}, "customs": {"A": "M", "B": "F"},
        "places": {"A": "M", "B": "F"}, "classroom": {"A": "M", "B": "F"}}


def main():
    with open(os.path.join(ROOT, "content", "content.json"), encoding="utf-8") as f:
        c = json.load(f)
    jobs = []  # (item id, voice key, rate key, text)
    for u in c["units"]:
        for p in u["phrases"] + u["signs"]:
            for v in VOICES:
                jobs += [(p["id"], v, r, p["zh"]) for r in RATES]
        for line in u["dialogue"]["lines"]:
            v = CAST[u["id"]][line["who"]]
            jobs += [(line["id"], v, r, line["zh"]) for r in RATES]

    os.makedirs(OUT, exist_ok=True)
    index, todo = {}, []
    for item, v, r, text in jobs:
        name = hashlib.sha1(f"{VOICES[v]}|{RATES[r]}|{text}".encode()).hexdigest()[:12] + ".mp3"
        index.setdefault(item, {}).setdefault(v, {})[r] = name
        if not os.path.exists(os.path.join(OUT, name)):
            todo.append((text, VOICES[v], RATES[r], name))

    async def run():
        sem = asyncio.Semaphore(6)

        async def one(text, voice, rate, name):
            async with sem:
                for attempt in range(3):
                    try:
                        await edge_tts.Communicate(text, voice, rate=rate).save(os.path.join(OUT, name))
                        return
                    except Exception as e:  # noqa: BLE001
                        if attempt == 2:
                            print("FAILED", text, voice, rate, e)
                        await asyncio.sleep(2)

        await asyncio.gather(*(one(*t) for t in todo))

    print(f"{len(jobs)} recordings, {len(todo)} to record")
    asyncio.run(run())
    with open(os.path.join(OUT, "index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, separators=(",", ":"))
    used = {n for v in index.values() for s in v.values() for n in s.values()}
    for fn in os.listdir(OUT):
        if fn.endswith(".mp3") and fn not in used:
            os.remove(os.path.join(OUT, fn))
    missing = [n for n in used if not os.path.exists(os.path.join(OUT, n))]
    print(f"index: {len(index)} items, {len(missing)} missing files")


if __name__ == "__main__":
    main()
