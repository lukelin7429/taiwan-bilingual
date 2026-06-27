/* ============================================================
   motion.js · scroll-reveal engine for the Taiwan Bilingual Hub
   Pairs with motion.css (section 3) and the inline <head> guard
   that sets html.mtn before first paint.

   Why getBoundingClientRect instead of IntersectionObserver:
   tall data-driven grids (and headless preview) don't reliably
   fire IO for elements far down the page. A throttled gBCR pass
   on scroll/resize is dead simple and works everywhere.

   Stagger: elements that cross into view in the SAME pass get an
   incremental transition-delay (a row sweeps in). The delay is an
   inline style; once the element has revealed we clear it so it
   never lags later hover transitions.
   ============================================================ */
(function () {
  var root = document.documentElement;
  window.__mtn = 1; // tell the head-guard failsafe we're alive

  var reduce = window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) { root.classList.remove('mtn'); return; }

  // Must mirror the reveal selector list in motion.css §3.
  var SEL = '.card,.hub-card,.hub-school-card,.school-card,.fet-card,' +
    '.about-card,.story-card,.ce-card,.policy-card,.policy-feature,' +
    '.bllc-card,.bc-moe-card,.sdg-card,.sdg,.ccard,.cty-feat,.person,' +
    '.theme,.dom-card,.progcard,.partner,[data-mtn]';

  function start() {
    if (!root.classList.contains('mtn')) root.classList.add('mtn');
    var els = [].slice.call(document.querySelectorAll(SEL));
    if (!els.length) { root.classList.remove('mtn'); return; }

    var raf = 0;

    function reveal(el, i) {
      if (i) el.style.transitionDelay = (Math.min(i, 8) * 0.05) + 's';
      el.classList.add('mtn-in');
      el.addEventListener('transitionend', function clear(e) {
        if (e.propertyName === 'transform' || e.propertyName === 'opacity') {
          el.style.transitionDelay = '';        // don't lag future hovers
          el.removeEventListener('transitionend', clear);
        }
      });
    }

    function pass() {
      raf = 0;
      var vh = window.innerHeight || root.clientHeight;
      var batch = [], rest = [];
      for (var i = 0; i < els.length; i++) {
        var r = els[i].getBoundingClientRect();
        // skip hidden (display:none) nodes — they have no box
        if (r.width === 0 && r.height === 0) { rest.push(els[i]); continue; }
        if (r.top < vh * 0.90 && r.bottom > 0) batch.push(els[i]);
        else rest.push(els[i]);
      }
      batch.forEach(reveal);
      els = rest;
      if (!els.length) {
        window.removeEventListener('scroll', onScroll);
        window.removeEventListener('resize', onScroll);
      }
    }

    function onScroll() {
      if (!raf) raf = window.requestAnimationFrame(pass);
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    pass(); // reveal whatever is already in view (with stagger)
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
})();
