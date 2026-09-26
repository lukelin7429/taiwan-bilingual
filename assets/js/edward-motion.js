/* ============================================================
   Edward Huang section · motion layer
   ------------------------------------------------------------
   1. Scroll reveal: any element with [data-rv] fades/slides in
      once it enters the viewport. [data-rv-stagger] on a parent
      staggers its direct children.
   2. Lightbox: any <a data-lightbox href="big.jpg"> opens the
      image full-screen (Esc / click / arrows to close or browse
      within the same data-lightbox group).
   3. Count-up: [data-count="113"] animates from 0 when revealed.
   Respects prefers-reduced-motion; content is visible without JS
   (html.ejs is only added here, and CSS hides nothing without it).
   ============================================================ */
(function () {
  var root = document.documentElement;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  root.classList.add('ejs');

  /* ---------- 1. reveal ---------- */
  var groups = document.querySelectorAll('[data-rv-stagger]');
  for (var g = 0; g < groups.length; g++) {
    var kids = groups[g].children;
    for (var k = 0; k < kids.length; k++) {
      kids[k].setAttribute('data-rv', '');
      kids[k].style.transitionDelay = Math.min(k * 70, 560) + 'ms';
    }
  }
  var items = document.querySelectorAll('[data-rv]');
  function show(el) {
    el.classList.add('rv-in');
    // once revealed, drop the reveal hooks so each card's own :hover transform works again
    var delay = parseInt(el.style.transitionDelay, 10) || 0;
    setTimeout(function () {
      el.removeAttribute('data-rv');
      el.classList.remove('rv-in');
      el.style.transitionDelay = '';
    }, reduce ? 0 : delay + 800);
    var nums = el.matches('[data-count]') ? [el] : el.querySelectorAll('[data-count]');
    for (var i = 0; i < nums.length; i++) countUp(nums[i]);
  }
  if (reduce || !('IntersectionObserver' in window)) {
    for (var i = 0; i < items.length; i++) show(items[i]);
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { show(e.target); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    for (var j = 0; j < items.length; j++) io.observe(items[j]);
  }

  /* ---------- 3. count-up ---------- */
  function countUp(el) {
    if (el.__counted) return;
    el.__counted = true;
    var end = parseInt(el.getAttribute('data-count'), 10);
    if (reduce || isNaN(end)) { el.textContent = el.getAttribute('data-count'); return; }
    var t0 = null, dur = 1400;
    function step(ts) {
      if (!t0) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  /* ---------- 2. lightbox ---------- */
  var links = document.querySelectorAll('a[data-lightbox]');
  if (!links.length) return;
  var box = document.createElement('div');
  box.className = 'elb';
  box.setAttribute('role', 'dialog');
  box.setAttribute('aria-modal', 'true');
  box.setAttribute('aria-label', 'Photo viewer');
  box.innerHTML =
    '<button class="elb-x" type="button" aria-label="Close">×</button>' +
    '<button class="elb-nav prev" type="button" aria-label="Previous">‹</button>' +
    '<figure class="elb-fig"><img alt=""><figcaption></figcaption></figure>' +
    '<button class="elb-nav next" type="button" aria-label="Next">›</button>';
  document.body.appendChild(box);
  var img = box.querySelector('img'), cap = box.querySelector('figcaption');
  var set = [], idx = 0, lastFocus = null;

  function captionFor(a) {
    var lang = root.classList.contains('lang-zh') ? 'zh' : 'en';
    return a.getAttribute('data-cap-' + lang) || a.getAttribute('data-cap') || '';
  }
  function render() {
    var a = set[idx];
    img.src = a.getAttribute('href');
    img.alt = (a.querySelector('img') || {}).alt || '';
    cap.textContent = captionFor(a);
    box.classList.toggle('single', set.length < 2);
  }
  function open(a) {
    var name = a.getAttribute('data-lightbox');
    set = Array.prototype.filter.call(links, function (l) { return l.getAttribute('data-lightbox') === name; });
    idx = set.indexOf(a);
    lastFocus = document.activeElement;
    render();
    box.classList.add('on');
    root.classList.add('elb-lock');
    box.querySelector('.elb-x').focus();
  }
  function close() {
    box.classList.remove('on');
    root.classList.remove('elb-lock');
    if (lastFocus) lastFocus.focus();
  }
  function go(d) { idx = (idx + d + set.length) % set.length; render(); }

  for (var n = 0; n < links.length; n++) {
    links[n].addEventListener('click', function (e) { e.preventDefault(); open(this); });
  }
  box.addEventListener('click', function (e) {
    if (e.target.closest('.elb-nav.prev')) return go(-1);
    if (e.target.closest('.elb-nav.next')) return go(1);
    if (e.target === img) return;
    close();
  });
  document.addEventListener('keydown', function (e) {
    if (!box.classList.contains('on')) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') go(-1);
    else if (e.key === 'ArrowRight') go(1);
  });
})();
