/* ============ KangLang News · Text-to-Speech + Dialogue Play-All ============ */
(function(){
  let voices = [];
  function loadVoices(){ voices = (window.speechSynthesis ? speechSynthesis.getVoices() : []) || []; }
  loadVoices();
  if (typeof speechSynthesis !== 'undefined') speechSynthesis.onvoiceschanged = loadVoices;

  function pickVoice(){
    if(!voices.length) return null;
    return voices.find(v => /en[-_]US/i.test(v.lang) && /samantha|female|google us english|aria|jenny/i.test(v.name))
        || voices.find(v => /en[-_]US/i.test(v.lang))
        || voices.find(v => /^en/i.test(v.lang)) || voices[0];
  }

  function speak(text, btn){
    if(!('speechSynthesis' in window)) return;
    speechSynthesis.cancel();
    document.querySelectorAll('.speak.is-speaking').forEach(b => b.classList.remove('is-speaking'));
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'en-US'; u.rate = 0.85; u.pitch = 1.05;
    const v = pickVoice(); if(v) u.voice = v;
    if(btn){ btn.classList.add('is-speaking'); u.onend = () => btn.classList.remove('is-speaking'); u.onerror = () => btn.classList.remove('is-speaking'); }
    speechSynthesis.speak(u);
  }

  document.querySelectorAll('[data-speak]').forEach(b => {
    b.addEventListener('click', () => speak(b.dataset.speak, b));
  });

  /* Dialogue "Play All" */
  const playBtn = document.getElementById('playAll');
  if(playBtn){
    let playing = false;
    playBtn.addEventListener('click', () => {
      const lines = [...document.querySelectorAll('#dlg .line')];
      if(playing){ speechSynthesis.cancel(); playing=false; playBtn.textContent='▶ Play the whole conversation'; lines.forEach(l=>l.classList.remove('is-speaking')); return; }
      playing = true; playBtn.textContent='■ Stop';
      let i = 0;
      const next = () => {
        lines.forEach(l => l.classList.remove('is-speaking'));
        if(!playing || i >= lines.length){ playing=false; playBtn.textContent='▶ Play the whole conversation'; return; }
        const line = lines[i++];
        line.classList.add('is-speaking');
        line.scrollIntoView({behavior:'smooth', block:'center'});
        const u = new SpeechSynthesisUtterance(line.getAttribute('data-say'));
        u.lang='en-US'; u.rate=0.85; u.pitch=1.05;
        const v = pickVoice(); if(v) u.voice = v;
        u.onend = next; u.onerror = next;
        speechSynthesis.speak(u);
      };
      speechSynthesis.cancel();
      next();
    });
  }

  /* Scroll reveal (reuses .rvl from main.css) */
  if(!(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches)){
    const els = [...document.querySelectorAll('.news-card,.kw,.line,.hero-figure,.pullquote')];
    els.forEach(el => el.classList.add('rvl'));
    if('IntersectionObserver' in window && els.length){
      const io = new IntersectionObserver(en => en.forEach(e => {
        if(!e.isIntersecting) return;
        const sibs = [...e.target.parentNode.children].filter(n => n.classList.contains('rvl'));
        e.target.style.transitionDelay = (Math.max(0, sibs.indexOf(e.target)) * 70) + 'ms';
        e.target.classList.add('in'); io.unobserve(e.target);
      }), {threshold:0.12, rootMargin:'0px 0px -6% 0px'});
      els.forEach(el => io.observe(el));
    } else { els.forEach(el => el.classList.add('in')); }
  }
})();
