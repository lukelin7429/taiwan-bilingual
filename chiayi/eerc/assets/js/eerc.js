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
    /* also mark the parent vocab-card if present */
    const card = btn.closest('.vocab-card');
    if(card) card.classList.add('speaking');
    btn.classList.add('speaking');
    const done = () => {
      btn.classList.remove('speaking');
      if(card) card.classList.remove('speaking');
    };
    utt.onend = done;
    utt.onerror = done;
  }
  window.speechSynthesis.speak(utt);
};

/* ── Ripple click effect on all cards ─────────────────────── */
(function(){
  function addRipple(el) {
    el.style.position = el.style.position || 'relative';
    el.style.overflow = 'hidden';
    el.addEventListener('click', function(e){
      const r = this.getBoundingClientRect();
      const rip = document.createElement('span');
      rip.className = 'eerc-ripple';
      rip.style.left = (e.clientX - r.left) + 'px';
      rip.style.top  = (e.clientY - r.top)  + 'px';
      this.appendChild(rip);
      rip.addEventListener('animationend', () => rip.remove());
    });
  }
  document.querySelectorAll(
    '.township-card, .highlight-card, .vocab-card, .resource-card, .tn-card, .fest-card, .ce-card'
  ).forEach(addRipple);
})();

/* ── Photo banner system ──────────────────────────────────── */
(function(){
  /* Map township slug → { url, credit, creditUrl } */
  const PHOTOS = {
    'alishan': {
      url: 'https://upload.wikimedia.org/wikipedia/commons/9/9f/2024-04-21_Alishan_Sakura_Trail_%28Upper_area%29.jpg',
      credit: 'Photo: Jaller94 / CC0 Public Domain'
    },
    'dongshi': {
      url: 'https://upload.wikimedia.org/wikipedia/commons/e/e5/%E6%9D%B1%E7%9F%B3%E8%9A%B5%E7%94%B0_Dongshi_Oyster_Farm_-_panoramio.jpg',
      credit: 'Photo: lienyuan lee / CC BY 3.0'
    },
    'budai': {
      url: 'https://upload.wikimedia.org/wikipedia/commons/7/77/%E5%98%89%E7%BE%A9%E5%B8%83%E8%A2%8B%E9%B9%BD%E5%B1%B1.JPG',
      credit: 'Photo: Pbdragonwang / CC BY-SA 3.0'
    },
    'meishan': {
      url: 'https://upload.wikimedia.org/wikipedia/commons/1/18/Sea_of_clouds_at_mt._A-Li_2.jpg',
      credit: 'Photo: Rasputinemark / CC BY-SA 4.0'
    },
    'fanlu': {
      url: 'https://upload.wikimedia.org/wikipedia/commons/0/0b/2004-10-24_Alishan_Forest_Railway_Chushan_line_near_Zhushan.jpg',
      credit: 'Photo: thinkcat / CC BY 2.0'
    },
    'zhuqi': {
      url: 'https://upload.wikimedia.org/wikipedia/commons/0/0b/2004-10-24_Alishan_Forest_Railway_Chushan_line_near_Zhushan.jpg',
      credit: 'Photo: thinkcat / CC BY 2.0'
    },
    'dapu': {
      url: 'https://upload.wikimedia.org/wikipedia/commons/d/d0/Sea_of_clouds_at_mt._A-Li_1.png',
      credit: 'Photo: Rasputinemark / CC BY-SA 4.0'
    }
  };

  /* Detect current township from URL path */
  const parts = window.location.pathname.split('/').filter(Boolean);
  const slug  = parts[parts.length - 1] || parts[parts.length - 2] || '';

  const data = PHOTOS[slug];
  if(!data) return;

  const banner = document.querySelector('.page-banner');
  if(!banner) return;

  /* Apply photo as background */
  banner.classList.add('has-photo');
  banner.style.backgroundImage = 'url("' + data.url + '")';

  /* Attribution */
  const attr = document.createElement('p');
  attr.className = 'photo-credit';
  attr.textContent = data.credit;
  banner.appendChild(attr);
})();

/* ── 3-D tilt on highlight cards (mouse move) ─────────────── */
(function(){
  document.querySelectorAll('.highlight-card').forEach(card => {
    card.addEventListener('mousemove', function(e){
      const r  = this.getBoundingClientRect();
      const cx = r.left + r.width  / 2;
      const cy = r.top  + r.height / 2;
      const dx = (e.clientX - cx) / (r.width  / 2);
      const dy = (e.clientY - cy) / (r.height / 2);
      this.style.transform = `translateY(-5px) rotateX(${-dy * 4}deg) rotateY(${dx * 4}deg)`;
    });
    card.addEventListener('mouseleave', function(){
      this.style.transform = '';
    });
  });
})();

/* ── Scroll-triggered stagger for grids ──────────────────── */
(function(){
  const grids = document.querySelectorAll(
    '.highlights-grid, .vocab-grid, .resource-grid, .township-grid'
  );
  grids.forEach(grid => {
    const children = Array.from(grid.children);
    children.forEach((child, i) => {
      child.style.transitionDelay = (i * 0.06) + 's';
    });
  });
})();
