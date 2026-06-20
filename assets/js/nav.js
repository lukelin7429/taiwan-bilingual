(function(){
  var btn = document.querySelector('.nav-toggle');
  var topbar = document.querySelector('.topbar');
  if(!btn || !topbar) return;

  btn.addEventListener('click', function(){
    var open = topbar.classList.toggle('nav-open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  });

  document.querySelectorAll('.topbar-nav a').forEach(function(a){
    a.addEventListener('click', function(){
      topbar.classList.remove('nav-open');
      btn.setAttribute('aria-expanded', 'false');
      btn.setAttribute('aria-label', 'Open menu');
    });
  });

  document.addEventListener('click', function(e){
    if(topbar.classList.contains('nav-open') && !topbar.contains(e.target)){
      topbar.classList.remove('nav-open');
      btn.setAttribute('aria-expanded', 'false');
      btn.setAttribute('aria-label', 'Open menu');
    }
  });
})();
