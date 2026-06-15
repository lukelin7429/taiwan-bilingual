/* Motion layer — nav-scroll shadow + number count-up. Reveal stays in main.js/CSS. */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // nav gains shadow once scrolled
  var nav = document.querySelector('.nav');
  function onScroll(){ if (nav) nav.classList.toggle('scrolled', window.scrollY > 12); }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  if (reduce) return;

  // count-up for .fact .fn (e.g. "3", "7×", "23")
  var nums = [].slice.call(document.querySelectorAll('.fact .fn'));
  function countUp(el){
    var m = el.textContent.trim().match(/^(\d+)(.*)$/);
    if (!m) return;
    var target = +m[1], suffix = m[2] || '', dur = 1200, t0 = null;
    function step(ts){
      if (!t0) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var e = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(e * target) + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if (nums.length){
    if ('IntersectionObserver' in window){
      var io = new IntersectionObserver(function (entries){
        entries.forEach(function (en){
          if (en.isIntersecting){ countUp(en.target); io.unobserve(en.target); }
        });
      }, { threshold: 0.5 });
      nums.forEach(function (n){ io.observe(n); });
    } else {
      // fallback: gBCR check on scroll (IO unreliable in some preview envs)
      var pending = nums.slice();
      var check = function (){
        var vh = window.innerHeight;
        pending = pending.filter(function (el){
          var r = el.getBoundingClientRect();
          if (r.top < vh * 0.85 && r.bottom > 0){ countUp(el); return false; }
          return true;
        });
        if (!pending.length) window.removeEventListener('scroll', check);
      };
      window.addEventListener('scroll', check, { passive: true });
      check();
    }
  }
})();
