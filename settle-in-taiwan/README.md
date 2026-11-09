# Settle In Taiwan · 台灣生活中文

A phone web app (PWA) for newcomers to Taiwan: everyday Chinese with Taiwan readings,
real Taiwanese voices, and practice in listening, speaking, reading, and writing.
Made for Ngoc (Ming Chuan University), from My Culture Connect. Interface in English.

## What each unit has

- **Learn**: phrases with pinyin or zhuyin, English, usage notes, Sino-Vietnamese links; play one or all
- **Listen**: a short dialogue (two voices), a comprehension quiz, and a "what did you hear?" drill
- **Speak**: listen, record yourself, play both back; optional speech-recognition check (zh-TW)
- **Read**: flashcards (characters first, then pronunciation, then meaning) and real-life signs
- **Write**: stroke-order animation and finger tracing with Hanzi Writer
- **Culture**: short tips about daily life in Taiwan

Settings: female/male voice, speed 0.5× / 0.75× / 1×, pinyin / zhuyin / off.
Progress is stored only in the browser (localStorage). Works offline after the first visit.

## Editing content

All lessons are in `tools/content_src.py`. Pinyin is written by hand, one numbered syllable
per character, with Taiwan readings (微 wéi, 識 shì, 息 xí) and the tone changes of 一/不.

```bash
python3 tools/build_content.py --check
```

rebuilds `content/content.json` and lists every syllable that differs from pypinyin, for proofreading.

Then record the new audio (only new items are recorded):

```bash
PYTHONPATH=$HOME/Developer/twrses-twhist-tools/tts ~/.local/pipx/venvs/edge-tts/bin/python tools/gen_audio.py
```

Voices: zh-TW-HsiaoChenNeural (female) and zh-TW-YunJheNeural (male), each at normal and slow (-45%) speed.
edge-tts needs the patched WSS_URL copy (see vault memory edge-tts-403-fix).

After changing files, bump `VERSION` in `sw.js` so installed phones pick up the update.

## Preview

```bash
python3 -m http.server 4310
```

## Credits

- Stroke data and animation: [Hanzi Writer](https://hanziwriter.org) (MIT) with data from Make Me a Hanzi (Arphic Public License), in `vendor/`
