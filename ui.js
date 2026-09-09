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
