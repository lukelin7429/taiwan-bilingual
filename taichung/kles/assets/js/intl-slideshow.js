/* ============ KangLang · International Education photo slideshow ============ */
/* Each .slideshow on the page becomes an independent carousel:
   - AUTO-ADVANCES every few seconds (autoplay)
   - prev/next arrows, clickable dots, a live counter, swipe on touch,
     and ← / → keys when the slideshow is hovered or focused
   Autoplay pauses politely: on hover, on focus, while touching, when the
   tab is hidden, when scrolled out of view, and for prefers-reduced-motion. */
(function(){
  const INTERVAL = 4500; // ms between slides

  function initSlideshow(root){
    const track  = root.querySelector('.slideshow__track');
    const slides = [...root.querySelectorAll('.slideshow__slide')];
    const dots   = [...root.querySelectorAll('.slideshow__dot')];
    const cur    = root.querySelector('.slideshow__cur');
    if(!track || slides.length === 0) return;
    let i = 0;
    const n = slides.length;

    function go(next){
      i = (next + n) % n;
      track.style.transform = 'translateX(' + (-i * 100) + '%)';
      dots.forEach((d, k) => d.classList.toggle('is-active', k === i));
      if(cur) cur.textContent = (i + 1);
      slides.forEach((s, k) => s.setAttribute('aria-hidden', k === i ? 'false' : 'true'));
    }

    /* ---- autoplay ---- */
    const reduced = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    const paused = { hover:false, focus:false, touch:false, hidden:false, offscreen:false };
    let timer = null;
    function canPlay(){ return !reduced && n > 1 && !Object.values(paused).some(Boolean); }
    function stop(){ if(timer){ clearTimeout(timer); timer = null; } }
    function play(){            // (re)start the countdown to the next slide
      stop();
      if(!canPlay()) return;
      timer = setTimeout(() => { go(i + 1); play(); }, INTERVAL);
    }
    function setPause(key, val){ paused[key] = val; if(canPlay()) play(); else stop(); }

    /* ---- manual controls (reset the timer so it waits a full beat after) ---- */
    function manual(next){ go(next); if(canPlay()) play(); }
    root.querySelector('.slideshow__arrow--prev')?.addEventListener('click', () => manual(i - 1));
    root.querySelector('.slideshow__arrow--next')?.addEventListener('click', () => manual(i + 1));
    dots.forEach((d, k) => d.addEventListener('click', () => manual(k)));

    /* keyboard when hovered / focused */
    root.setAttribute('tabindex', '0');
    root.addEventListener('mouseenter', () => setPause('hover', true));
    root.addEventListener('mouseleave', () => setPause('hover', false));
    root.addEventListener('focusin',  () => setPause('focus', true));
    root.addEventListener('focusout', () => setPause('focus', false));
    document.addEventListener('keydown', (e) => {
      if(!paused.hover && !paused.focus) return;   // only when this slideshow is "hot"
      if(e.key === 'ArrowLeft'){ manual(i - 1); }
      else if(e.key === 'ArrowRight'){ manual(i + 1); }
    });

    /* swipe / drag */
    let x0 = null, dx = 0;
    const vp = root.querySelector('.slideshow__viewport');
    function start(x){ x0 = x; dx = 0; root.classList.add('is-dragging'); setPause('touch', true); }
    function move(x){ if(x0 === null) return; dx = x - x0; }
    function end(){
      if(x0 === null) return;
      root.classList.remove('is-dragging');
      track.style.transform = 'translateX(' + (-i * 100) + '%)';
      if(Math.abs(dx) > 45){ go(dx < 0 ? i + 1 : i - 1); }
      x0 = null; dx = 0;
      setPause('touch', false);   // resumes autoplay (with a fresh beat)
    }
    vp.addEventListener('touchstart', e => start(e.touches[0].clientX), {passive:true});
    vp.addEventListener('touchmove',  e => move(e.touches[0].clientX),  {passive:true});
    vp.addEventListener('touchend', end);

    /* pause when the tab is hidden */
    document.addEventListener('visibilitychange', () => setPause('hidden', document.hidden));

    /* pause when scrolled out of view */
    if('IntersectionObserver' in window){
      const io = new IntersectionObserver((ents) => {
        ents.forEach(e => setPause('offscreen', !e.isIntersecting));
      }, { threshold: 0.35 });
      io.observe(root);
    }

    go(0);
    play();   // start auto-advancing
  }

  document.querySelectorAll('.slideshow').forEach(initSlideshow);
})();
