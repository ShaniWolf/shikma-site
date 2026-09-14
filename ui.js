document.documentElement.classList.add('js');
(function(){
  var els = document.querySelectorAll('.rv');
  if(!els.length) return;
  if(!('IntersectionObserver' in window)){
    els.forEach(function(el){ el.classList.add('in'); });
    return;
  }
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(en){
      if(en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target); }
    });
  }, {rootMargin:'0px 0px -40px 0px', threshold:.12});
  els.forEach(function(el){ io.observe(el); });
})();

(function(){
  var ok = false;
  try{ ok = !!localStorage.getItem('ck-ok'); }catch(e){}
  if(ok) return;
  var bar = document.createElement('div');
  bar.className = 'cookiebar';
  bar.setAttribute('role','region');
  bar.setAttribute('aria-label','הודעת עוגיות');
  bar.innerHTML = '<p>האתר משתמש בעוגיות למדידה ולשיפור החוויה. <a href="privacy.html">למדיניות הפרטיות</a></p><button type="button">אישור</button>';
  bar.querySelector('button').addEventListener('click', function(){
    try{ localStorage.setItem('ck-ok','1'); }catch(e){}
    bar.classList.remove('show');
    setTimeout(function(){ bar.remove(); }, 450);
  });
  document.body.appendChild(bar);
  requestAnimationFrame(function(){ requestAnimationFrame(function(){ bar.classList.add('show'); }); });
})();

/* קרוסלת המלצות: גלילה ידנית, חצים, נקודות, החלפה אוטומטית שנעצרת בריחוף/מגע */
(function(){
  var cars = document.querySelectorAll('[data-carousel]');
  if(!cars.length) return;
  cars.forEach(function(car){
    var track = car.querySelector('.car-track'), slides = Array.prototype.slice.call(track.children);
    var prev = car.querySelector('.prev'), next = car.querySelector('.next'), dots = car.querySelector('.car-dots');
    var timer, paused = false, pages = 1, page = 0;
    function perView(){ return window.innerWidth >= 640 ? 2 : 1; }
    function build(){
      pages = Math.max(1, Math.ceil(slides.length / perView()));
      dots.innerHTML = '';
      for(var i = 0; i < pages; i++){
        var b = document.createElement('button'); b.type = 'button'; b.setAttribute('role','tab');
        b.setAttribute('aria-label', 'המלצות ' + (i + 1)); b.dataset.i = i;
        b.addEventListener('click', function(){ go(+this.dataset.i, true); });
        dots.appendChild(b);
      }
      sync();
    }
    function slideW(){ return slides[0].getBoundingClientRect().width + 16; }
    function go(n, user){
      page = (n + pages) % pages;
      var x = page * perView() * slideW();
      track.scrollTo({left: -x, behavior: 'smooth'});
      if(user) restart();
    }
    function sync(){
      var cur = Math.round(Math.abs(track.scrollLeft) / (perView() * slideW()));
      page = Math.min(pages - 1, Math.max(0, cur));
      Array.prototype.forEach.call(dots.children, function(d, i){ d.setAttribute('aria-selected', i === page ? 'true' : 'false'); });
    }
    function tick(){ if(!paused && !document.hidden) go(page + 1); }
    function restart(){ clearInterval(timer); timer = setInterval(tick, 6500); }
    prev.addEventListener('click', function(){ go(page - 1, true); });
    next.addEventListener('click', function(){ go(page + 1, true); });
    track.addEventListener('scroll', function(){ clearTimeout(track._t); track._t = setTimeout(sync, 80); });
    ['mouseenter','focusin','touchstart','pointerdown'].forEach(function(ev){ car.addEventListener(ev, function(){ paused = true; }, {passive:true}); });
    ['mouseleave','focusout','touchend'].forEach(function(ev){ car.addEventListener(ev, function(){ paused = false; }, {passive:true}); });
    window.addEventListener('resize', function(){ clearTimeout(car._r); car._r = setTimeout(build, 150); });
    build();
    if(!window.matchMedia || !window.matchMedia('(prefers-reduced-motion: reduce)').matches) restart();
  });
})();

/* חלון קופץ עונתי: דף ההיערכות ליום כיפור. נכבה מעצמו אחרי החג.
   נפתח אחרי גלילה של 45% או 25 שניות בעמוד, או בכוונת יציאה במחשב. פעם ב-3 ימים לכל מבקר. */
(function(){
  var END = new Date('2026-09-21T20:00:00+03:00');
  var EP = 'https://assets.mailerlite.com/jsonp/2618157/forms/198613248576062729/subscribe';
  var KEY = 'kp-pop';
  if(new Date() > END) return;
  var p = location.pathname;
  if(/kippur|thanks|privacy|terms|accessibility|404|lev\.html/.test(p)) return;
  try{
    var last = +localStorage.getItem(KEY) || 0;
    if(Date.now() - last < 3*864e5) return;
  }catch(e){}
  var shown = false;
  function ga(n, x){ if(typeof gtag === 'function') gtag('event', n, Object.assign({popup:'kippur', page_path:p}, x||{})); }
  function mark(){ try{ localStorage.setItem(KEY, String(Date.now())); }catch(e){} }

  function open(trigger){
    if(shown) return; shown = true; mark();
    var w = document.createElement('div');
    w.className = 'kpop';
    w.innerHTML =
      '<div class="kpop-bg" data-close></div>' +
      '<div class="kpop-card" role="dialog" aria-modal="true" aria-labelledby="kpop-h">' +
        '<button type="button" class="kpop-x" data-close aria-label="סגירה">×</button>' +
        '<div class="kpop-cover"><img src="assets/covers/kippur.png" alt="" width="120" height="170"></div>' +
        '<div class="kpop-body">' +
          '<p class="kpop-eyeb">דף היערכות קצר להורים לצמודים</p>' +
          '<h2 id="kpop-h">מי עושה מה ביום כיפור?</h2>' +
          '<p>חמש דקות של תיאום מראש יכולות למנוע את הרגע שבו שניכם כבר עייפים, שני הילדים צריכים אתכם ואף אחד לא יודע מה עושים עכשיו.</p>' +
          '<form class="kpop-form" novalidate>' +
            '<label class="sr" for="kpop-email">כתובת מייל</label>' +
            '<input type="email" id="kpop-email" autocomplete="email" required placeholder="כתובת מייל">' +
            '<button type="submit">שלחו לי את הדף</button>' +
            '<p class="kpop-err" role="alert"></p>' +
            '<p class="kpop-note">הדף מגיע מיד. אפשר להסיר את הכתובת בכל רגע. <a href="privacy.html">פרטיות</a></p>' +
          '</form>' +
        '</div>' +
      '</div>';
    document.body.appendChild(w);
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ w.classList.add('show'); }); });
    ga('popup_view', {trigger: trigger});
    var prevFocus = document.activeElement;
    var input = w.querySelector('input');
    setTimeout(function(){ if(window.innerWidth >= 640) input.focus(); }, 350);

    function close(){
      w.classList.remove('show'); ga('popup_close');
      document.removeEventListener('keydown', onKey);
      setTimeout(function(){ w.remove(); if(prevFocus && prevFocus.focus) prevFocus.focus(); }, 300);
    }
    function onKey(e){ if(e.key === 'Escape') close(); }
    document.addEventListener('keydown', onKey);
    w.querySelectorAll('[data-close]').forEach(function(el){ el.addEventListener('click', close); });

    var f = w.querySelector('form'), btn = f.querySelector('button'), err = f.querySelector('.kpop-err');
    f.addEventListener('submit', function(e){
      e.preventDefault();
      var email = input.value.trim();
      if(!email || email.indexOf('@') < 1 || email.indexOf('.') < 0){ err.textContent = 'צריך כתובת מייל תקינה כדי לשלוח את הדף'; return; }
      err.textContent = ''; btn.disabled = true; btn.textContent = 'רגע, שולחת...';
      var done = false;
      function finish(){
        if(done) return; done = true;
        try{ localStorage.setItem(KEY, String(Date.now() + 30*864e5)); }catch(e){}
        ga('magnet_signup', {magnet:'kippur'});
        location.href = 'thanks-kippur.html';
      }
      fetch(EP, {method:'POST', headers:{'Content-Type':'application/x-www-form-urlencoded'},
        body:'fields%5Bemail%5D=' + encodeURIComponent(email) + '&ml-submit=1&anticsrf=true'}).then(finish).catch(finish);
      setTimeout(finish, 6000);
    });
  }

  var timer = setTimeout(function(){ open('time'); }, 25000);
  function onScroll(){
    var h = document.documentElement.scrollHeight - window.innerHeight;
    if(h > 0 && window.scrollY / h > .45){ window.removeEventListener('scroll', onScroll); clearTimeout(timer); open('scroll'); }
  }
  window.addEventListener('scroll', onScroll, {passive:true});
  if(window.matchMedia && window.matchMedia('(pointer:fine)').matches){
    document.addEventListener('mouseout', function(e){
      if(!e.relatedTarget && e.clientY < 8){ clearTimeout(timer); open('exit'); }
    });
  }
})();
