/* ============================================================
   EERC — shared JS: mobile nav, scroll-reveal, Web Speech
   ============================================================ */

/* ── Mobile nav toggle ────────────────────────────────────── */
(function(){
  const btn = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.topbar-nav');
  if(!btn || !nav) return;
  btn.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open);
  });
  document.addEventListener('click', e => {
    if(!btn.contains(e.target) && !nav.contains(e.target)) {
      nav.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
    }
  });
})();

/* ── Scroll-reveal (getBoundingClientRect, no IntersectionObserver) ── */
(function(){
  const els = document.querySelectorAll('.rvl');
  if(!els.length) return;
  function check(){
    const vh = window.innerHeight;
    els.forEach(el => {
      if(el.classList.contains('revealed')) return;
      const r = el.getBoundingClientRect();
      if(r.top < vh * 0.92) el.classList.add('revealed');
    });
  }
  window.addEventListener('scroll', check, { passive: true });
  window.addEventListener('resize', check, { passive: true });
  check();
})();

/* ── Web Speech API speaker ───────────────────────────────── */
window.say = function(text, btn) {
  if(!window.speechSynthesis) return;
  window.speechSynthesis.cancel();
  const utt = new SpeechSynthesisUtterance(text);
  utt.lang = 'en-US';
  utt.rate = 0.92;
  if(btn) {
    btn.classList.add('speaking');
    utt.onend = () => btn.classList.remove('speaking');
    utt.onerror = () => btn.classList.remove('speaking');
  }
  window.speechSynthesis.speak(utt);
};
