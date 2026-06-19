/* ============ KangLang · International Education photo slideshow ============ */
/* Each .slideshow on the page becomes an independent carousel:
   prev/next arrows, clickable dots, a live counter, swipe on touch,
   and ← / → keys when the slideshow is hovered or focused. */
(function(){
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

    root.querySelector('.slideshow__arrow--prev')?.addEventListener('click', () => go(i - 1));
    root.querySelector('.slideshow__arrow--next')?.addEventListener('click', () => go(i + 1));
    dots.forEach((d, k) => d.addEventListener('click', () => go(k)));

    /* keyboard when hovered / focused */
    let hot = false;
    root.addEventListener('mouseenter', () => hot = true);
    root.addEventListener('mouseleave', () => hot = false);
    root.setAttribute('tabindex', '0');
    root.addEventListener('focusin', () => hot = true);
    root.addEventListener('focusout', () => hot = false);
    document.addEventListener('keydown', (e) => {
      if(!hot) return;
      if(e.key === 'ArrowLeft'){ go(i - 1); }
      else if(e.key === 'ArrowRight'){ go(i + 1); }
    });

    /* swipe / drag */
    let x0 = null, dx = 0;
    const vp = root.querySelector('.slideshow__viewport');
    function start(x){ x0 = x; dx = 0; root.classList.add('is-dragging'); }
    function move(x){ if(x0 === null) return; dx = x - x0; }
    function end(){
      if(x0 === null) return;
      root.classList.remove('is-dragging');
      track.style.transform = 'translateX(' + (-i * 100) + '%)';
      if(Math.abs(dx) > 45){ go(dx < 0 ? i + 1 : i - 1); }
      x0 = null; dx = 0;
    }
    vp.addEventListener('touchstart', e => start(e.touches[0].clientX), {passive:true});
    vp.addEventListener('touchmove',  e => move(e.touches[0].clientX),  {passive:true});
    vp.addEventListener('touchend', end);

    go(0);
  }
  document.querySelectorAll('.slideshow').forEach(initSlideshow);
})();
