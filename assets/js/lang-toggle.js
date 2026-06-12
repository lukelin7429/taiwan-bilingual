/* ============================================================
   Edward Huang section · full EN <-> ZH language switch
   ------------------------------------------------------------
   Scope: only the Edward Huang pages use this. The <html> element
   carries class "lang-en" or "lang-zh"; CSS hides the other side.
   Choice persists in localStorage("edward-lang") across subpages.
   The button label always offers the OTHER language.
   ============================================================ */
(function () {
  var KEY = 'edward-lang';
  var root = document.documentElement;

  function apply(lang) {
    root.classList.remove('lang-en', 'lang-zh');
    root.classList.add(lang === 'zh' ? 'lang-zh' : 'lang-en');
    root.setAttribute('lang', lang === 'zh' ? 'zh-Hant' : 'en');
    // every toggle button shows the language you'd switch TO
    var btns = document.querySelectorAll('[data-lang-toggle]');
    for (var i = 0; i < btns.length; i++) {
      btns[i].innerHTML = lang === 'zh'
        ? '<span class="globe">🌐</span> English'
        : '<span class="globe">🌐</span> 中文';
      btns[i].setAttribute('aria-label',
        lang === 'zh' ? 'Switch to English' : '切換為中文');
    }
  }

  function current() {
    return root.classList.contains('lang-zh') ? 'zh' : 'en';
  }

  document.addEventListener('click', function (e) {
    var btn = e.target.closest('[data-lang-toggle]');
    if (!btn) return;
    var next = current() === 'zh' ? 'en' : 'zh';
    try { localStorage.setItem(KEY, next); } catch (err) {}
    apply(next);
  });

  // sync button labels on load (class was set pre-paint by the head script)
  document.addEventListener('DOMContentLoaded', function () {
    apply(current());
  });
})();
