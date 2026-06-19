/* KangLang Elementary — scroll reveal (fade / rise with staggered delay).
   getBoundingClientRect + scroll based (not IntersectionObserver/rAF) so it
   works in every environment and never leaves content stuck hidden. */
(function () {
  'use strict';
  if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var sel = [
    '.section-head', '.about-text', '.lineage', '.pillar', '.principal-card',
    '.life-card', '.life-cta', '.visit-grid > *', '.principal-portrait',
    '.prose-inner', '.commit', '.curriculum-card', '.playlist-wrap',
    '.stations-intro', '.station', '.history-table'
  ].join(',');

  function init() {
    var els = Array.prototype.slice.call(document.querySelectorAll(sel));
    if (!els.length) return;
    els.forEach(function (el) { el.classList.add('rvl'); });

    function reveal(el) {
      var sibs = Array.prototype.slice.call(el.parentNode.children).filter(function (n) {
        return n.classList.contains('rvl');
      });
      el.style.transitionDelay = (Math.max(0, sibs.indexOf(el)) * 80) + 'ms';
      el.classList.add('in');
    }
    var ticking = false;
    function check() {
      ticking = false;
      var vh = window.innerHeight || document.documentElement.clientHeight;
      var doc = document.documentElement;
      // at (or near) the bottom of the page, reveal everything left so no
      // element near the footer can stay stuck hidden.
      var atBottom = (window.scrollY || doc.scrollTop) + vh >= (doc.scrollHeight - 4);
      for (var i = els.length - 1; i >= 0; i--) {
        if (atBottom || els[i].getBoundingClientRect().top < vh * 0.92) { reveal(els[i]); els.splice(i, 1); }
      }
    }
    function onScroll() { if (!ticking) { ticking = true; setTimeout(check, 60); } }
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
    check();                                 // reveal anything already in view
    window.addEventListener('load', check);  // re-check after images/fonts settle
    setTimeout(check, 250);                   // safety net
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
