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

/* חלונות קופצים לפי לוגיקה (עונה + הקשר העמוד). פעם ב-3 ימים לכל מבקר, לא מופיע על העמוד של ההצעה עצמה.
   עד מוצאי כיפור (21.9): דף ההיערכות לכיפור. עד 3.10: מדריך החגים לסוכות. אחר כך: להכין את הלב.
   בעמודי אחים (siblings/lev) תמיד להכין את הלב. אף פעם לא ב-30 השניות הראשונות; אחר כך 60% גלילה, 50 שניות, או כוונת יציאה במחשב.
   הטון: טיפ של שקמה קודם, ההצעה אחריו. */
(function(){
  var P = location.pathname, now = new Date();
  if(/thanks|privacy|terms|accessibility|404/.test(P)) return;
  var ML = 'https://assets.mailerlite.com/jsonp/2618157/forms/';
  var OFFERS = {
    kippur: {h:'עוגן אחד לילדים ביום כיפור',
      tip:'בחרו עוגן אחד או שניים שחשוב לכם לשמור עליהם. למשל: שנת הצהריים, ארוחה בשעה מוכרת או טקס השינה מהבית. לא חייבים לשמור על כל השגרה כדי לתת לילדים יציבות.',
      offer:'רוצים לסגור את זה מראש יחד עם מי שאיתכם בבית? הכנתי דף היערכות קצר: מי מוביל, מי נח ומה עושים כשהם צריכים דברים שונים.',
      form:'198613248576062729', btn:'שלחו לי את הדף', thanks:'thanks-kippur.html', skip:/kippur/},
    chagim: {h:'לקראת סוכות',
      tip:'לפעמים נכון לצאת לפני הקינוח. לפעמים אחד ההורים ירדים והשני יישאר. ולפעמים הבחירה המתאימה תהיה להגיע לזמן קצר או להתפצל.',
      offer:'כשזה קורה, זיהיתם מה המשפחה שלכם צריכה עכשיו ובחרתם בהתאם. עוד כלים כאלה, לשינה, לגבולות ולחלוקת תפקידים, מחכים במדריך ״חגים עם צמודים״.',
      link:'chagim.html', btn:'לכל הפרטים על המדריך', skip:/chagim/},
    lev: {h:'כשמגיע אח או אחות',
      tip:'האנרגיה שלכם משפיעה יותר מכל טכניקה, ולא צריך לעשות את זה מושלם. מה שעוזר הוא הכנה מוקדמת ותחושה שהלב פשוט גדל.',
      offer:'הכנתי מדריך קצר שלוקח אתכם מההיריון ועד השבועות הראשונים, עם המילים שאפשר להגיד ברגעים עצמם.',
      form:'197954875365000600', btn:'שלחו לי את המדריך', thanks:'thanks-lev.html', skip:/lev\.html/}
  };
  var id;
  if(/siblings|lev/.test(P)) id = 'lev';
  else if(now < new Date('2026-09-21T20:00:00+03:00')) id = 'kippur';
  else if(now < new Date('2026-10-03T23:59:00+03:00')) id = 'chagim';
  else id = 'lev';
  var o = OFFERS[id];
  if(o.skip.test(P)) return;
  var KEY = 'pop-' + id;
  try{ if(Date.now() - (+localStorage.getItem(KEY) || 0) < 3*864e5) return; }catch(e){}
  var shown = false;
  function ga(n, x){ if(typeof gtag === 'function') gtag('event', n, Object.assign({popup:id, page_path:P}, x||{})); }

  function open(trigger){
    if(shown) return; shown = true;
    try{ localStorage.setItem(KEY, String(Date.now())); }catch(e){}
    var w = document.createElement('div');
    w.className = 'kpop';
    var action = o.form
      ? '<form class="kpop-form" novalidate><label class="sr" for="kpop-email">כתובת מייל</label>' +
        '<input type="email" id="kpop-email" autocomplete="email" required placeholder="כתובת מייל">' +
        '<button type="submit">' + o.btn + '</button><p class="kpop-err" role="alert"></p>' +
        '<p class="kpop-note">מגיע מיד. אפשר להסיר את הכתובת בכל רגע. <a href="privacy.html">פרטיות</a></p></form>'
      : '<a class="kpop-cta" href="' + o.link + '">' + o.btn + '</a>';
    w.innerHTML = '<div class="kpop-bg" data-close></div>' +
      '<div class="kpop-card" role="dialog" aria-modal="true" aria-labelledby="kpop-h">' +
      '<button type="button" class="kpop-x" data-close aria-label="סגירה">×</button>' +
      '<div class="kpop-body"><div class="kpop-who"><img src="assets/shikma.jpg" alt="" width="52" height="52"><span><b>שקמה דגרי</b>הדרכת הורים לגיל הרך | התמחות בצמודים</span></div>' +
      '<h2 id="kpop-h">' + o.h + '</h2><p class="kpop-tip">' + o.tip + '</p><p class="kpop-offer">' + o.offer + '</p>' + action + '</div></div>';
    document.body.appendChild(w);
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ w.classList.add('show'); }); });
    ga('popup_view', {trigger: trigger});
    var prevFocus = document.activeElement;
    function close(){
      w.classList.remove('show'); ga('popup_close');
      document.removeEventListener('keydown', onKey);
      setTimeout(function(){ w.remove(); if(prevFocus && prevFocus.focus) prevFocus.focus(); }, 300);
    }
    function onKey(e){ if(e.key === 'Escape') close(); }
    document.addEventListener('keydown', onKey);
    w.querySelectorAll('[data-close]').forEach(function(el){ el.addEventListener('click', close); });
    var cta = w.querySelector('.kpop-cta');
    if(cta) cta.addEventListener('click', function(){ ga('popup_click'); });
    var f = w.querySelector('form');
    if(!f) return;
    var input = f.querySelector('input'), btn = f.querySelector('button'), err = f.querySelector('.kpop-err');
    setTimeout(function(){ if(window.innerWidth >= 640) input.focus(); }, 350);
    f.addEventListener('submit', function(e){
      e.preventDefault();
      var email = input.value.trim();
      if(!email || email.indexOf('@') < 1 || email.indexOf('.') < 0){ err.textContent = 'צריך כתובת מייל תקינה'; return; }
      err.textContent = ''; btn.disabled = true; btn.textContent = 'רגע, שולחת...';
      var done = false;
      function finish(){
        if(done) return; done = true;
        try{ localStorage.setItem(KEY, String(Date.now() + 60*864e5)); }catch(e){}
        ga('magnet_signup', {magnet:id});
        location.href = o.thanks;
      }
      fetch(ML + o.form + '/subscribe', {method:'POST', headers:{'Content-Type':'application/x-www-form-urlencoded'},
        body:'fields%5Bemail%5D=' + encodeURIComponent(email) + '&ml-submit=1&anticsrf=true'}).then(finish).catch(finish);
      setTimeout(finish, 6000);
    });
  }

  var t0 = Date.now(), DWELL = 30000;
  function ready(){ return Date.now() - t0 >= DWELL; }
  var timer = setTimeout(function(){ open('time'); }, 50000);
  function onScroll(){
    if(!ready()) return;
    var h = document.documentElement.scrollHeight - window.innerHeight;
    if(h > 0 && window.scrollY / h > .6){ window.removeEventListener('scroll', onScroll); clearTimeout(timer); open('scroll'); }
  }
  window.addEventListener('scroll', onScroll, {passive:true});
  if(window.matchMedia && window.matchMedia('(pointer:fine)').matches){
    document.addEventListener('mouseout', function(e){ if(ready() && !e.relatedTarget && e.clientY < 8){ clearTimeout(timer); open('exit'); } });
  }
})();
