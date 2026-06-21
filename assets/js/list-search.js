/* Reusable per-page list filter.
   Put on any listing page:
     <input type="search" data-search=".scard"
            data-search-group=".shelf-row"   (optional: hide groups with no matches)
            data-search-scope="#shelves"      (optional: limit to a container; default = whole doc)
            data-search-empty="#ls-empty">    (optional: element to show when nothing matches)
   Cards are matched on their visible text; add data-search-text="extra keywords"
   to a card to make it findable by words not shown on screen. */
(function () {
  function init(input) {
    var itemSel = input.getAttribute('data-search') || '.scard,.card';
    var scopeSel = input.getAttribute('data-search-scope');
    var scope = (scopeSel && document.querySelector(scopeSel)) || document;
    var groupSel = input.getAttribute('data-search-group');
    var emptySel = input.getAttribute('data-search-empty');
    var emptyEl = emptySel ? document.querySelector(emptySel) : null;

    function run() {
      var q = input.value.trim().toLowerCase();
      var items = scope.querySelectorAll(itemSel);
      var shown = 0;
      Array.prototype.forEach.call(items, function (it) {
        var hay = (it.getAttribute('data-search-text') || it.textContent || '').toLowerCase();
        var hit = !q || hay.indexOf(q) !== -1;
        it.style.display = hit ? '' : 'none';
        if (hit) shown++;
      });
      if (groupSel) {
        Array.prototype.forEach.call(scope.querySelectorAll(groupSel), function (g) {
          var any = Array.prototype.some.call(g.querySelectorAll(itemSel), function (it) {
            return it.style.display !== 'none';
          });
          g.style.display = any ? '' : 'none';
        });
      }
      if (emptyEl) emptyEl.hidden = shown !== 0;
    }

    input.addEventListener('input', run);
    input.addEventListener('search', run);
  }

  function boot() {
    Array.prototype.forEach.call(document.querySelectorAll('input[data-search]'), init);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
