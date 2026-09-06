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
