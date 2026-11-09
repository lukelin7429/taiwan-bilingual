// Settle In Taiwan: everyday Chinese for newcomers. Hash router + one view per tab.
const DEDICATION = 'Made for Ngoc, with a warm welcome from My Culture Connect.';
const TABS = [
  ['learn', 'Learn'], ['listen', 'Listen'], ['speak', 'Speak'],
  ['read', 'Read'], ['write', 'Write'], ['culture', 'Culture'],
];
const SKILLS = ['learn', 'listen', 'speak', 'read', 'write'];

const $view = document.getElementById('view');
const $title = document.getElementById('title');
const $back = document.getElementById('back');
let DATA, AUDIO;
let cleanup = null; // stops whatever the current view is playing or recording

// ---------- storage ----------
function load(key, fallback) {
  try { return JSON.parse(localStorage.getItem(key)) ?? fallback; } catch { return fallback; }
}
function save(key, value) {
  try { localStorage.setItem(key, JSON.stringify(value)); } catch { /* private mode */ }
}
const settings = Object.assign({ voice: 'F', speed: '1', script: 'pinyin' }, load('sit-settings', {}));
const progress = load('sit-progress', {});

function prog(uid) {
  progress[uid] ??= { learn: [], listen: 0, speak: [], read: [], write: [] };
  return progress[uid];
}
function mark(uid, skill, id) {
  const p = prog(uid);
  if (!p[skill].includes(id)) { p[skill].push(id); save('sit-progress', progress); }
}
function unitPercent(u) {
  const p = progress[u.id];
  if (!p) return 0;
  const n = u.phrases.length;
  const parts = [
    p.learn.length / n,
    p.listen,
    p.speak.length / n,
    p.read.length / n,
    p.write.length / u.write.length,
  ];
  return Math.round(100 * parts.reduce((a, b) => a + Math.min(1, b), 0) / SKILLS.length);
}

// ---------- helpers ----------
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const shuffle = (a) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };

function rubyHTML(tokens, show = settings.script) {
  return tokens.map((t) => {
    if (!t.p || show === 'none') return esc(t.c);
    return `<ruby>${esc(t.c)}<rt>${esc(show === 'zhuyin' ? t.z : t.p)}</rt></ruby>`;
  }).join('');
}
const pinyinLine = (tokens) => tokens.filter((t) => t.p).map((t) => t.p).join(' ');

// ---------- audio ----------
const player = new Audio();
player.preservesPitch = true;
let playingBtn = null;

function audioFile(id, voice = settings.voice) {
  const v = AUDIO[id];
  if (!v) return null;
  const set = v[voice] || Object.values(v)[0];
  return settings.speed === '0.5' ? set.s : set.n;
}
function play(id, btn, voice) {
  const file = audioFile(id, voice);
  if (!file) return Promise.resolve();
  if (playingBtn) playingBtn.classList.remove('playing');
  player.src = `audio/${file}`;
  player.playbackRate = settings.speed === '0.75' ? 0.75 : 1;
  playingBtn = btn || null;
  if (btn) btn.classList.add('playing');
  return new Promise((resolve) => {
    const done = () => { if (btn) btn.classList.remove('playing'); player.onended = player.onerror = null; resolve(); };
    player.onended = done; player.onerror = done;
    player.play().catch(done);
  });
}
function stopAudio() { player.pause(); player.onended?.(); }

function speedControl() {
  const opts = [['0.5', '0.5×'], ['0.75', '0.75×'], ['1', '1×']];
  return `<span class="label">Speed</span><span class="seg" data-speed>${opts.map(([v, l]) =>
    `<button class="${settings.speed === v ? 'on' : ''}" data-v="${v}">${l}</button>`).join('')}</span>`;
}
function bindSpeed(root) {
  root.querySelectorAll('[data-speed] button').forEach((b) => b.onclick = () => {
    settings.speed = b.dataset.v; save('sit-settings', settings);
    root.querySelectorAll('[data-speed] button').forEach((x) => x.classList.toggle('on', x === b));
  });
}

// ---------- router ----------
async function boot() {
  const [c, a] = await Promise.all([
    fetch('content/content.json').then((r) => r.json()),
    fetch('audio/index.json').then((r) => r.json()),
  ]);
  DATA = c; AUDIO = a;
  applyScriptClass();
  window.addEventListener('hashchange', route);
  route();
  if ('serviceWorker' in navigator) navigator.serviceWorker.register('sw.js').catch(() => {});
}
function applyScriptClass() {
  document.body.classList.toggle('script-zhuyin', settings.script === 'zhuyin');
}
function setUnitColor(color) {
  document.documentElement.style.setProperty('--unit', color || 'var(--brand)');
  document.querySelector('meta[name=theme-color]').content = color || '#2f5d4f';
}

function route() {
  stopAudio();
  cleanup?.();
  cleanup = null;
  const [, a, b, c] = location.hash.split('/');
  window.scrollTo(0, 0);
  if (a === 'u' && DATA.units.find((u) => u.id === b)) return unitView(DATA.units.find((u) => u.id === b), c || 'learn');
  if (a === 'settings') return settingsView();
  homeView();
}
// ---------- home ----------
function homeView() {
  setUnitColor(null);
  $title.textContent = 'Settle In Taiwan';
  $back.hidden = true;
  $view.innerHTML = `
    <section class="hero">
      <p class="hi">歡迎來台灣！</p>
      <h2>Welcome to Taiwan!</h2>
      <p>Everyday Chinese for your first months here. Each unit has phrases to listen to, say, read, and write, with real Taiwanese voices.</p>
      <p class="muted dedication">${esc(DEDICATION)}</p>
    </section>
    <div class="units">
      ${DATA.units.map((u) => {
        const pct = unitPercent(u);
        return `<a class="unit-card" style="--c:${u.color}" href="#/u/${u.id}">
          <div class="emoji">${u.emoji}</div>
          <h3>${esc(u.title)}</h3>
          <div class="zh">${esc(u.zh)}</div>
          <div class="bar"><i style="width:${pct}%"></i></div>
          <div class="pct">${pct}% done</div>
        </a>`;
      }).join('')}
    </div>
    <p class="section-title">Coming soon</p>
    <div class="units">
      ${DATA.coming.map(([e, t]) => `<div class="unit-card soon"><div class="emoji">${e}</div><h3>${esc(t)}</h3></div>`).join('')}
    </div>
    <p class="footer">Tip: add this app to your home screen to use it offline.</p>`;
}

// ---------- settings ----------
function settingsView() {
  setUnitColor(null);
  $title.textContent = 'Settings';
  $back.hidden = false; $back.href = '#/';
  const seg = (key, opts) => `<span class="seg" data-key="${key}">${opts.map(([v, l]) =>
    `<button class="${settings[key] === v ? 'on' : ''}" data-v="${v}">${l}</button>`).join('')}</span>`;
  $view.innerHTML = `
    <div class="setting"><h3>Voice</h3>${seg('voice', [['F', 'Female'], ['M', 'Male']])}
      <p>Two natural Taiwanese voices. Dialogues always use the voice of each speaker.</p></div>
    <div class="setting"><h3>Speed</h3>${seg('speed', [['0.5', '0.5×'], ['0.75', '0.75×'], ['1', '1×']])}
      <p>0.5× is a separate slow recording, so it still sounds natural.</p></div>
    <div class="setting"><h3>Pronunciation guide</h3>${seg('script', [['pinyin', 'Pinyin'], ['zhuyin', 'Zhuyin ㄅㄆㄇ'], ['none', 'Off']])}
      <p>Pinyin is the easiest to start with. Zhuyin is what Taiwanese children learn at school.</p></div>
    <div class="card" style="margin-top:8px"><div class="row"><button class="play" id="test">▶</button>
      <div class="grow"><p class="phrase">${rubyHTML(DATA.units[0].phrases[0].t)}</p><p class="en">Test the voice</p></div></div></div>
    <div class="setting" style="margin-top:28px"><h3>Progress</h3>
      <button class="btn" id="reset">Reset my progress</button></div>`;
  $view.querySelectorAll('.seg').forEach((s) => s.querySelectorAll('button').forEach((b) => b.onclick = () => {
    settings[s.dataset.key] = b.dataset.v; save('sit-settings', settings);
    s.querySelectorAll('button').forEach((x) => x.classList.toggle('on', x === b));
    applyScriptClass();
    if (s.dataset.key === 'script') $view.querySelector('.phrase').innerHTML = rubyHTML(DATA.units[0].phrases[0].t);
  }));
  $view.querySelector('#test').onclick = (e) => play(DATA.units[0].phrases[0].id, e.currentTarget);
  $view.querySelector('#reset').onclick = () => {
    if (!confirm('Erase all progress on this phone?')) return;
    Object.keys(progress).forEach((k) => delete progress[k]); save('sit-progress', progress);
    location.hash = '#/';
  };
}

// ---------- unit ----------
function unitView(u, tab) {
  setUnitColor(u.color);
  $title.textContent = `${u.emoji} ${u.title}`;
  $back.hidden = false; $back.href = '#/';
  $view.innerHTML = `<nav class="tabs">${TABS.map(([k, l]) =>
    `<a href="#/u/${u.id}/${k}" class="${k === tab ? 'on' : ''}">${l}</a>`).join('')}</nav><div id="pane"></div>`;
  const pane = $view.querySelector('#pane');
  ({ learn, listen, speak, read, write, culture })[tab]?.(u, pane);
  $view.querySelector('.tabs a.on')?.scrollIntoView({ inline: 'center', block: 'nearest' });
}

function phraseCard(p, uid) {
  const tips = [
    p.note ? `<p class="tip">${esc(p.note)}</p>` : '',
    p.hv ? `<p class="tip hv"><b>🇻🇳 </b>${esc(p.hv)}</p>` : '',
  ].join('');
  return `<div class="card"><div class="row">
    <div class="grow"><p class="phrase">${rubyHTML(p.t)}</p><p class="en">${esc(p.en)}</p></div>
    <button class="play" data-play="${p.id}" data-uid="${uid}" aria-label="Play">▶</button>
  </div>${tips}</div>`;
}

function learn(u, pane) {
  pane.innerHTML = `<p class="intro">${esc(u.intro)}</p>
    ${u.hv ? `<p class="tip hv" style="margin-bottom:14px"><b>🇻🇳 </b>${esc(u.hv)}</p>` : ''}
    <div class="toolbar">${speedControl()}<button class="btn" id="all">▶ Play all</button></div>
    <div class="cards-2">${u.phrases.map((p) => phraseCard(p, u.id)).join('')}</div>`;
  bindSpeed(pane);
  pane.querySelectorAll('[data-play]').forEach((b) => b.onclick = () => {
    play(b.dataset.play, b); mark(u.id, 'learn', b.dataset.play);
  });
  let stop = false;
  cleanup = () => { stop = true; };
  pane.querySelector('#all').onclick = async (e) => {
    const btn = e.currentTarget;
    if (btn.dataset.on) { stop = true; stopAudio(); return; }
    stop = false; btn.dataset.on = '1'; btn.textContent = '■ Stop';
    for (const p of u.phrases) {
      if (stop) break;
      const b = pane.querySelector(`[data-play="${p.id}"]`);
      b.closest('.card').scrollIntoView({ block: 'center', behavior: 'smooth' });
      await play(p.id, b); mark(u.id, 'learn', p.id);
      await new Promise((r) => setTimeout(r, 700));
    }
    delete btn.dataset.on; btn.textContent = '▶ Play all';
  };
}

function listen(u, pane) {
  const d = u.dialogue;
  pane.innerHTML = `
    <h2 style="margin:0 0 4px;font-size:23px">${esc(d.title)}</h2>
    <p class="cast">A: ${esc(d.cast.A)}<br>B: ${esc(d.cast.B)}</p>
    <div class="toolbar">${speedControl()}
      <button class="btn primary" id="playall">▶ Play the dialogue</button>
      <button class="btn" id="hide">Hide the words</button></div>
    <div id="dlg">${d.lines.map((l) => `<div class="line ${l.who}">
      <div class="who">${l.who}</div>
      <div class="bubble" data-id="${l.id}"><p class="phrase">${rubyHTML(l.t)}</p><p class="en">${esc(l.en)}</p></div></div>`).join('')}</div>
    <h2 style="margin:26px 0 8px;font-size:23px">Quiz</h2>
    <p class="muted" style="margin:0 0 10px;font-size:18px">Listen first, then answer.</p>
    <div id="quiz"></div>
    <h2 style="margin:30px 0 8px;font-size:23px">What did you hear?</h2>
    <div id="drill"></div>`;
  bindSpeed(pane);
  const dlg = pane.querySelector('#dlg');
  let stop = false;
  cleanup = () => { stop = true; };
  pane.querySelectorAll('.bubble').forEach((b) => b.onclick = () => play(b.dataset.id, b));
  pane.querySelector('#hide').onclick = (e) => {
    dlg.classList.toggle('hidden-text');
    e.currentTarget.textContent = dlg.classList.contains('hidden-text') ? 'Show the words' : 'Hide the words';
  };
  pane.querySelector('#playall').onclick = async (e) => {
    const btn = e.currentTarget;
    if (btn.dataset.on) { stop = true; stopAudio(); return; }
    stop = false; btn.dataset.on = '1'; btn.textContent = '■ Stop';
    for (const l of d.lines) {
      if (stop) break;
      const b = dlg.querySelector(`[data-id="${l.id}"]`);
      b.classList.add('now'); b.scrollIntoView({ block: 'center', behavior: 'smooth' });
      await play(l.id); b.classList.remove('now');
      await new Promise((r) => setTimeout(r, 500));
    }
    delete btn.dataset.on; btn.textContent = '▶ Play the dialogue';
  };

  // Dialogue quiz
  const quiz = pane.querySelector('#quiz');
  let qi = 0, right = 0;
  const showQ = () => {
    if (qi >= d.quiz.length) {
      const score = right / d.quiz.length;
      const p = prog(u.id); p.listen = Math.max(p.listen, score); save('sit-progress', progress);
      quiz.innerHTML = `<div class="card"><p class="score">${right} / ${d.quiz.length}</p>
        <p>${score === 1 ? 'Perfect! 太棒了！' : 'Listen again and try once more.'}</p>
        <button class="btn" id="again">Try again</button></div>`;
      quiz.querySelector('#again').onclick = () => { qi = 0; right = 0; showQ(); };
      return;
    }
    const q = d.quiz[qi];
    const opts = shuffle([q.a, ...q.wrong]);
    quiz.innerHTML = `<div class="card"><p class="counter" style="text-align:left">Question ${qi + 1} of ${d.quiz.length}</p>
      <p class="q">${esc(q.q)}</p><div class="choices">${opts.map((o) => `<button class="choice">${esc(o)}</button>`).join('')}</div></div>`;
    quiz.querySelectorAll('.choice').forEach((b) => b.onclick = () => {
      const ok = b.textContent === q.a;
      if (ok) right++;
      quiz.querySelectorAll('.choice').forEach((x) => { x.disabled = true; if (x.textContent === q.a) x.classList.add('right'); });
      if (!ok) b.classList.add('wrong');
      setTimeout(() => { qi++; showQ(); }, 1100);
    });
  };
  showQ();

  // Phrase drill: hear a phrase, pick its meaning.
  const drill = pane.querySelector('#drill');
  const nextDrill = () => {
    const pick = shuffle(u.phrases).slice(0, 4);
    const target = pick[0];
    drill.innerHTML = `<div class="card"><div class="row"><button class="play" id="dp">▶</button>
      <p class="grow" style="margin:0">Tap to listen, then choose the meaning.</p></div>
      <div class="choices">${shuffle(pick).map((p) => `<button class="choice" data-id="${p.id}">${esc(p.en)}</button>`).join('')}</div></div>`;
    const dp = drill.querySelector('#dp');
    dp.onclick = () => play(target.id, dp);
    drill.querySelectorAll('.choice').forEach((b) => b.onclick = () => {
      drill.querySelectorAll('.choice').forEach((x) => { x.disabled = true; if (x.dataset.id === target.id) x.classList.add('right'); });
      if (b.dataset.id !== target.id) b.classList.add('wrong');
      const card = drill.querySelector('.card');
      card.insertAdjacentHTML('beforeend', `<p class="phrase" style="margin-top:12px">${rubyHTML(target.t)}</p>
        <div class="btns"><button class="btn primary" id="nx">Next ›</button></div>`);
      card.querySelector('#nx').onclick = nextDrill;
    });
  };
  nextDrill();
}

// ---------- speak ----------
const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition;

function compare(target, heard) {
  // Longest common subsequence over Chinese characters: which target characters were heard.
  const a = [...target.replace(/[^㐀-鿿]/g, '')];
  const b = [...heard.replace(/[^㐀-鿿]/g, '')];
  const dp = Array.from({ length: a.length + 1 }, () => new Array(b.length + 1).fill(0));
  for (let i = a.length - 1; i >= 0; i--) for (let j = b.length - 1; j >= 0; j--) {
    dp[i][j] = a[i] === b[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
  }
  const hit = new Array(a.length).fill(false);
  for (let i = 0, j = 0; i < a.length && j < b.length;) {
    if (a[i] === b[j]) { hit[i] = true; i++; j++; } else if (dp[i + 1][j] >= dp[i][j + 1]) i++; else j++;
  }
  return { chars: a, hit, score: a.length ? Math.round(100 * hit.filter(Boolean).length / a.length) : 0 };
}

function speak(u, pane) {
  let i = 0, recorder = null, chunks = [], myURL = null, stream = null;
  cleanup = () => { recorder?.state === 'recording' && recorder.stop(); stream?.getTracks().forEach((t) => t.stop()); };
  const canRecord = !!(navigator.mediaDevices?.getUserMedia && window.MediaRecorder);

  const render = () => {
    const p = u.phrases[i];
    if (myURL) { URL.revokeObjectURL(myURL); myURL = null; }
    pane.innerHTML = `
      <div class="toolbar">${speedControl()}</div>
      <div class="card big">
        <p class="counter">${i + 1} / ${u.phrases.length}</p>
        <p class="phrase">${rubyHTML(p.t)}</p>
        <p class="en">${esc(p.en)}</p>
        <div class="btns">
          <button class="btn primary" id="model">▶ Listen</button>
          ${canRecord ? '<button class="btn" id="rec">● Record me</button><button class="btn" id="mine" disabled>▶ My voice</button>' : ''}
        </div>
        ${Recognition ? '<div class="btns"><button class="btn" id="check">🎙 Check my pronunciation</button></div>' : ''}
        <div class="result" id="result"></div>
      </div>
      <div class="btns"><button class="btn" id="prev" ${i === 0 ? 'disabled' : ''}>‹ Back</button>
        <button class="btn" id="next" ${i === u.phrases.length - 1 ? 'disabled' : ''}>Next ›</button></div>
      <p class="muted" style="font-size:17px;margin-top:18px">Listen, record yourself, then play both and compare.
      ${Recognition ? 'The pronunciation check uses your phone\'s speech recognition, so treat the score as a friendly guide.' : ''}</p>`;
    bindSpeed(pane);
    const $r = pane.querySelector('#result');
    pane.querySelector('#model').onclick = (e) => play(p.id, e.currentTarget);
    pane.querySelector('#prev').onclick = () => { i--; render(); };
    pane.querySelector('#next').onclick = () => { i++; render(); };

    const rec = pane.querySelector('#rec');
    const mine = pane.querySelector('#mine');
    if (rec) rec.onclick = async () => {
      if (recorder?.state === 'recording') { recorder.stop(); return; }
      try {
        stream ??= await navigator.mediaDevices.getUserMedia({ audio: true });
      } catch {
        $r.innerHTML = '<p class="muted">Please allow the microphone to record yourself.</p>'; return;
      }
      chunks = [];
      recorder = new MediaRecorder(stream);
      recorder.ondataavailable = (e) => chunks.push(e.data);
      recorder.onstop = () => {
        rec.classList.remove('rec'); rec.textContent = '● Record again';
        if (myURL) URL.revokeObjectURL(myURL);
        myURL = URL.createObjectURL(new Blob(chunks, { type: recorder.mimeType }));
        mine.disabled = false;
        mark(u.id, 'speak', p.id);
      };
      recorder.start();
      rec.classList.add('rec'); rec.textContent = '■ Stop';
    };
    if (mine) mine.onclick = () => {
      if (!myURL) return;
      stopAudio();
      player.src = myURL; player.playbackRate = 1; player.play().catch(() => {});
    };

    const check = pane.querySelector('#check');
    if (check) check.onclick = () => {
      const r = new Recognition();
      r.lang = 'zh-TW'; r.interimResults = false; r.maxAlternatives = 3;
      check.disabled = true; check.textContent = '🎙 Listening… speak now';
      r.onresult = (e) => {
        const alts = [...e.results[0]].map((x) => x.transcript);
        const best = alts.map((h) => ({ h, ...compare(p.zh, h) })).sort((a, b) => b.score - a.score)[0];
        const msg = best.score >= 90 ? 'Excellent! 很好！' : best.score >= 60 ? 'Good! Try once more for the missing parts.' : 'Listen again and try once more.';
        $r.innerHTML = `<p class="zh">${best.chars.map((c, k) => `<span class="${best.hit[k] ? 'hit' : 'miss'}">${c}</span>`).join('')}</p>
          <p><span class="score">${best.score}%</span> · ${msg}</p><p class="muted" style="font-size:17px">I heard: ${esc(best.h)}</p>`;
        if (best.score >= 60) mark(u.id, 'speak', p.id);
      };
      r.onerror = (e) => {
        $r.innerHTML = `<p class="muted">${e.error === 'not-allowed' ? 'Please allow the microphone.' : 'I didn\'t catch that. Try again.'}</p>`;
      };
      r.onend = () => { check.disabled = false; check.textContent = '🎙 Check my pronunciation'; };
      r.start();
    };
  };
  render();
}

// ---------- read ----------
const SIGN_COLORS = { 男: 'blue', 女: 'red', 禁止吸菸: 'red', 出口: '', 入口: '', 推: 'blue', 拉: 'blue', 廁所: 'blue', 營業中: '', 休息中: 'red', 只收現金: 'amber', 排隊: 'amber' };

function read(u, pane) {
  const p = prog(u.id);
  let deck = shuffle(u.phrases.filter((x) => !p.read.includes(x.id)));
  if (!deck.length) deck = shuffle(u.phrases);
  let step = 0;
  pane.innerHTML = `<p class="intro">Read the characters first. Tap to see the pronunciation, then the meaning.</p>
    <div id="card"></div>
    <h2 style="margin:28px 0 6px;font-size:23px">Signs you will see</h2>
    <p class="muted" style="margin:0 0 12px;font-size:18px">Tap a sign to hear it and see what it means.</p>
    <div class="signs">${u.signs.map((s) => `<button class="sign ${SIGN_COLORS[s.zh] ?? ''}" data-id="${s.id}">
      <span class="zh">${esc(s.zh)}</span><span class="reveal"></span></button>`).join('')}</div>`;
  pane.querySelectorAll('.sign').forEach((b) => b.onclick = () => {
    const s = u.signs.find((x) => x.id === b.dataset.id);
    b.querySelector('.reveal').textContent = `${pinyinLine(s.t)} · ${s.en}`;
    play(s.id);
  });
  const box = pane.querySelector('#card');
  const render = () => {
    if (!deck.length) {
      box.innerHTML = `<div class="card flash"><p class="score">All done! 🎉</p>
        <p>You can read all ${u.phrases.length} phrases in this unit.</p>
        <div class="btns"><button class="btn primary" id="again">Practice again</button></div></div>`;
      box.querySelector('#again').onclick = () => { deck = shuffle(u.phrases); step = 0; render(); };
      return;
    }
    const c = deck[0];
    box.innerHTML = `<div class="card flash">
      <p class="counter">${deck.length} left</p>
      <p class="phrase">${step >= 1 ? rubyHTML(c.t, settings.script === 'none' ? 'pinyin' : settings.script) : esc(c.zh)}</p>
      <p class="en" style="min-height:30px">${step >= 2 ? esc(c.en) : ''}</p>
      <div class="btns">${step < 2
        ? `<button class="btn primary" id="show">${step === 0 ? 'Show pronunciation' : 'Show meaning'}</button>`
        : '<button class="btn" id="again">↺ Again later</button><button class="btn primary" id="got">✓ I knew it</button>'}</div></div>`;
    const show = box.querySelector('#show');
    if (show) show.onclick = () => { step++; if (step === 1) play(c.id); render(); };
    const got = box.querySelector('#got');
    if (got) got.onclick = () => { mark(u.id, 'read', c.id); deck.shift(); step = 0; render(); };
    const again = box.querySelector('#again');
    if (again) again.onclick = () => { deck.push(deck.shift()); step = 0; render(); };
  };
  render();
}

// ---------- write ----------
function write(u, pane) {
  const p = prog(u.id);
  let current = u.write[0];
  let writer = null;
  const findReading = (ch) => {
    for (const unit of DATA.units) for (const x of [...unit.phrases, ...unit.signs]) {
      const t = x.t.find((k) => k.c === ch);
      if (t) return { t, example: x };
    }
    return null;
  };
  pane.innerHTML = `<p class="intro">Watch the stroke order, then write each character with your finger.</p>
    <div class="chars">${u.write.map((ch) => `<button data-ch="${ch}" class="${p.write.includes(ch) ? 'done' : ''}">${ch}</button>`).join('')}</div>
    <div class="pad-wrap"><div class="grid-pad" id="pad"></div></div>
    <div class="write-info" id="info"></div>
    <div class="status" id="status"></div>
    <div class="btns"><button class="btn" id="anim">▶ Watch strokes</button><button class="btn primary" id="practice">✍️ Write it</button></div>`;
  const $pad = pane.querySelector('#pad'), $info = pane.querySelector('#info'), $status = pane.querySelector('#status');
  const size = Math.min(280, window.innerWidth - 64);
  $pad.style.width = $pad.style.height = `${size}px`;

  const select = (ch) => {
    current = ch;
    pane.querySelectorAll('.chars button').forEach((b) => b.classList.toggle('on', b.dataset.ch === ch));
    $pad.innerHTML = ''; $status.textContent = '';
    writer = HanziWriter.create($pad, ch, {
      width: size, height: size, padding: 14, showOutline: true, strokeColor: '#1d2422',
      radicalColor: null, outlineColor: '#dddddd', drawingWidth: 22, strokeAnimationSpeed: 1, delayBetweenStrokes: 250,
      charDataLoader: (c, onLoad, onError) => fetch(`vendor/hanzi/${c}.json`).then((r) => r.json()).then(onLoad).catch(onError),
    });
    const r = findReading(ch);
    $info.innerHTML = r ? `<span class="p">${esc(settings.script === 'zhuyin' ? r.t.z : r.t.p)}</span>
      <div class="zh" style="font-size:22px">${esc(r.example.zh)} <span class="muted" style="font-family:var(--en);font-size:18px">${esc(r.example.en)}</span></div>` : '';
    if (r) play(r.example.id);
  };
  pane.querySelectorAll('.chars button').forEach((b) => b.onclick = () => select(b.dataset.ch));
  pane.querySelector('#anim').onclick = () => { $status.textContent = ''; writer.cancelQuiz(); writer.showCharacter(); writer.animateCharacter(); };
  pane.querySelector('#practice').onclick = () => {
    $status.textContent = 'Write the strokes in order.';
    writer.hideCharacter();
    writer.quiz({
      showHintAfterMisses: 2,
      onMistake: () => { $status.innerHTML = '<span style="color:var(--bad)">Not quite. Try that stroke again.</span>'; },
      onCorrectStroke: (d) => { $status.textContent = `${d.strokeNum + 1} / ${d.strokeNum + 1 + d.strokesRemaining}`; },
      onComplete: (d) => {
        $status.innerHTML = `<span style="color:var(--good);font-weight:700">${d.totalMistakes === 0 ? 'Perfect! 寫得很好！' : 'Done! 很好！'}</span>`;
        mark(u.id, 'write', current);
        pane.querySelector(`[data-ch="${current}"]`).classList.add('done');
      },
    });
  };
  select(current);
}

// ---------- culture ----------
function culture(u, pane) {
  pane.innerHTML = u.culture.map(([h, t]) => `<div class="card culture"><h3>${esc(h)}</h3><p>${esc(t)}</p></div>`).join('');
}

boot();
