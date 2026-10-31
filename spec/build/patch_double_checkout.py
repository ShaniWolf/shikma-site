# -*- coding: utf-8 -*-
"""31.10: שדה מייל לפני המעבר לתשלום ב-double.html (שני אישרה).

במקום כפתור שמקפיץ ישר לישראכרט, טופס קצר (שם פרטי, שם משפחה, מייל, אישור תכנים) ואז ״להמשיך לתשלום״.
הפרטים נשמרים ב-MailerLite בקבוצה ״התחילו רכישה: הורות בדאבל״ (טופס 202841816552179432) ורק אז עוברים
לדף התשלום. ככה יודעים מי התחילה לקנות גם כשישראכרט לא מחזיר אותה לאתר, ואפשר להצליב עם התראת המכירה.
קישור התשלום יושב ב-data-pay, כך ש-patch_price_full.py עדיין מחליף אותו. אידמפוטנטי."""
import pathlib, re
P = pathlib.Path(__file__).resolve().parents[2] / 'double.html'
FORM = '202841816552179432'
h = P.read_text(encoding='utf-8')
if 'class="mform buyform"' in h:
    print('already there'); raise SystemExit

BTN = re.compile(r'    <a class="btn" href="(https://pay360\.isracard\.co\.il/CustomerPayment/GenericURL\?SaleId=[0-9a-f-]+)">אני רוצה את המדריך</a>\n')
def form(pay, i):
    return '''    <form class="mform buyform" novalidate data-pay="%s">
      <label for="b%d-name">שם פרטי</label>
      <input type="text" id="b%d-name" name="name" autocomplete="given-name" required placeholder="שם פרטי">
      <label for="b%d-last">שם משפחה</label>
      <input type="text" id="b%d-last" name="last_name" autocomplete="family-name" required placeholder="שם משפחה">
      <label for="b%d-email">כתובת מייל</label>
      <input type="email" id="b%d-email" name="email" autocomplete="email" required placeholder="name@example.com">
      <label class="chk"><input type="checkbox" id="b%d-ok" required> אני מאשרת לקבל משקמה תכנים, כלים ועדכונים. אפשר להסיר את ההרשמה בכל עת.</label>
      <button type="submit">להמשיך לתשלום</button>
      <p class="err" role="alert"></p>
    </form>
''' % ((pay,) + (i,) * 7)

n = [0]
def rep(m):
    n[0] += 1
    return form(m.group(1), n[0])
h = BTN.sub(rep, h)
assert n[0] == 2, n

JS = '''
<script>
(function(){
  var FORM='%s';
  function go(f){
    var v=function(k){ var el=f.querySelector('[name="'+k+'"]'); return el ? el.value.trim() : ''; };
    var name=v('name'), last=v('last_name'), email=v('email');
    var err=f.querySelector('.err'), btn=f.querySelector('button[type=submit]');
    if(!name || !last){ err.textContent='צריך שם פרטי ושם משפחה'; return; }
    if(!email || email.indexOf('@')<1 || email.indexOf('.')<0){ err.textContent='צריך כתובת מייל תקינה'; return; }
    if(!f.querySelector('input[type=checkbox]').checked){ err.textContent='צריך לאשר קבלת תכנים כדי להמשיך'; return; }
    err.textContent=''; btn.disabled=true; btn.textContent='רגע, עוברים לתשלום...';
    var body='fields%%5Bemail%%5D='+encodeURIComponent(email)+'&fields%%5Bname%%5D='+encodeURIComponent(name)+'&fields%%5Bfirst_name%%5D='+encodeURIComponent(name)+'&fields%%5Blast_name%%5D='+encodeURIComponent(last)+'&ml-submit=1&anticsrf=true';
    try{ fetch('https://assets.mailerlite.com/jsonp/2618157/forms/'+FORM+'/subscribe',{method:'POST',keepalive:true,headers:{'Content-Type':'application/x-www-form-urlencoded'},body:body}).catch(function(){}); }catch(e){}
    try{ localStorage.setItem('imale_buy_email', email); }catch(e){}
    if(typeof gtag==='function'){ gtag('event','click_payment',{product:(document.title.split('|')[0]||'').trim(),page_path:location.pathname}); }
    setTimeout(function(){ location.href=f.getAttribute('data-pay'); }, 400);
  }
  var fs=document.querySelectorAll('form.buyform');
  for(var i=0;i<fs.length;i++){ (function(f){ f.addEventListener('submit', function(e){ e.preventDefault(); go(f); }); })(fs[i]); }
})();
</script>
</body>''' % FORM
assert h.count('</body>') == 1
h = h.replace('</body>', JS, 1)
P.write_text(h, encoding='utf-8')
print('ok: 2 forms')
