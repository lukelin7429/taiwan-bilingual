/* NanJung JHS — language toggle, scroll reveal, mobile menu */
(function () {
  var KEY = 'njh-lang';
  var body = document.body;

  function setLang(lang) {
    if (lang !== 'en' && !document.querySelector('.lang-' + lang)) lang = 'en';
    body.classList.remove('lang-en', 'lang-ja', 'lang-ko');
    body.classList.add('lang-' + lang);
    document.documentElement.lang = lang;
    try { localStorage.setItem(KEY, lang); } catch (e) {}
    document.querySelectorAll('.lang-toggle button').forEach(function (b) {
      b.classList.toggle('on', b.dataset.lang === lang);
    });
  }

  var saved = 'en';
  try { saved = localStorage.getItem(KEY) || 'en'; } catch (e) {}
  setLang(saved);

  document.querySelectorAll('.lang-toggle button').forEach(function (b) {
    b.addEventListener('click', function () { setLang(b.dataset.lang); });
  });

  // mobile menu
  var nt = document.querySelector('.nav-toggle');
  var menu = document.querySelector('.menu');
  if (nt) nt.addEventListener('click', function () { menu.classList.toggle('open'); });
  if (menu) menu.querySelectorAll('a').forEach(function (a) {
    a.addEventListener('click', function () { menu.classList.remove('open'); });
  });

  // scroll reveal — getBoundingClientRect on load + scroll (reliable in preview),
  // plus a safety timer so content is NEVER stuck hidden.
  var els = [].slice.call(document.querySelectorAll('.rvl'));
  function show(el){ el.classList.add('in'); }
  function check(){
    var vh = window.innerHeight || document.documentElement.clientHeight;
    els.forEach(function(el){
      if (el.classList.contains('in')) return;
      var r = el.getBoundingClientRect();
      if (r.top < vh * 0.9 && r.bottom > 0) show(el);
    });
  }
  check();
  window.addEventListener('scroll', function(){ requestAnimationFrame(check); }, {passive:true});
  window.addEventListener('resize', check);
  // belt-and-braces: reveal everything still hidden after 1.6s
  setTimeout(function(){ els.forEach(show); }, 1600);
})();
