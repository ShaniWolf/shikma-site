"""Email capture on the purchase thank-you pages.
Replaces the manual WhatsApp delivery block with a one-field MailerLite form
(group רכישות + per-product group) and an inline confirmation. Idempotent."""
import os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

WA = 'https://wa.me/972528594469?text=%D7%94%D7%99%D7%99%20%D7%A9%D7%A7%D7%9E%D7%94%2C%20%D7%A8%D7%9B%D7%A9%D7%AA%D7%99%20%D7%9E%D7%93%D7%A8%D7%99%D7%9A%20%D7%95%D7%90%D7%A9%D7%9E%D7%97%20%D7%9C%D7%A7%D7%91%D7%9C%20%D7%90%D7%95%D7%AA%D7%95'

PAGES = {
    # page: (product key, product name, MailerLite form id)
    'thanks-tantrums.html': ('tantrums', 'כשהבית מתפוצץ', '198150224188802244'),
    'thanks-gvulot.html':   ('gvulot',   'גבולות מתוך חיבור', '198150249549661394'),
    'thanks-together.html': ('together', 'לגדול ביחד', '198150249900934414'),
    'thanks-chagim.html':   ('chagim',   'החגים עם צמודים', '198150250229138748'),
}

def form_block(key, name, fid, chagim=False):
    if chagim:
        label = 'רוצים שהמדריך יחכה לכם גם במייל?'
        btn = 'שלחו לי אותו למייל'
        note = 'הקישור להורדה יגיע למייל תוך דקות, וישאר שם גם כשהטלפון מתחלף.'
    else:
        label = 'לאן לשלוח את המדריך?'
        btn = 'שלחו לי את המדריך'
        note = 'הגישה ל״%s״ נפתחת לכתובת הזו ומגיעה למייל תוך דקות. אם היא לא הגיעה, בדקו בקידומי מכירות, ואם עדיין לא, <a href="%s" target="_blank" rel="noopener">כתבו לי בוואטסאפ</a> ואני פותחת ידנית.' % (name, WA)
    return '''    <form class="mform tform" id="mform" novalidate data-fid="%s" data-product="%s">
      <label for="mf-email">%s</label>
      <input type="email" id="mf-email" name="email" autocomplete="email" required placeholder="הכתובת שאיתה תפתחו את המדריך">
      <button type="submit" id="mf-btn">%s</button>
      <p class="err" id="mf-err" role="alert"></p>
    </form>
    <div class="mf-done" id="mf-done" hidden>
      <p class="lead">קיבלתי. ״%s״ בדרך ל<span id="mf-to"></span>.</p>
    </div>
    <p class="btn-note">%s</p>''' % (fid, key, label, btn, name, note)

JS = '''
<script>
(function(){
  var f=document.getElementById('mform'); if(!f) return;
  var btn=document.getElementById('mf-btn'), err=document.getElementById('mf-err'), done=document.getElementById('mf-done');
  var EP='https://assets.mailerlite.com/jsonp/2618157/forms/'+f.getAttribute('data-fid')+'/subscribe';
  var product=f.getAttribute('data-product');
  f.addEventListener('submit', function(e){
    e.preventDefault();
    var email=document.getElementById('mf-email').value.trim();
    if(!email || email.indexOf('@')<1 || email.indexOf('.')<0){ err.textContent='צריך כתובת מייל תקינה כדי לשלוח את המדריך'; return; }
    err.textContent=''; btn.disabled=true; btn.textContent='רגע, שולחת...';
    var fin=false;
    function finish(){
      if(fin) return; fin=true;
      if(typeof gtag==='function'){ gtag('event','purchase_email',{product:product,page_path:location.pathname}); }
      document.getElementById('mf-to').textContent=email;
      f.hidden=true; done.hidden=false;
    }
    var body='fields%5Bemail%5D='+encodeURIComponent(email)+'&ml-submit=1&anticsrf=true';
    fetch(EP,{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:body}).then(function(){ finish(); }).catch(function(){ finish(); });
    setTimeout(finish, 6000);
  });
})();
</script>
'''

for page, (key, name, fid) in PAGES.items():
    path = os.path.join(ROOT, page)
    s = open(path, encoding='utf-8').read()
    if 'id="mform"' in s:
        print('already', page); continue
    chagim = key == 'chagim'
    if chagim:
        # keep the PDF button; add the form after its line
        m = re.search(r'    <a class="btn" href="assets/d/[^"]+" download="[^"]+">להורדת המדריך \(PDF\)</a>\n', s)
        assert m, page
        s = s[:m.end()] + form_block(key, name, fid, chagim=True) + '\n' + s[m.end():]
    else:
        # replace the WhatsApp button + delivery note
        pat = re.compile(r'    <a class="btn" href="https://wa\.me/[^"]+" target="_blank" rel="noopener">שלחו לי את המדריך בוואטסאפ</a>\n    <p class="btn-note">.*?</p>\n', re.S)
        assert pat.search(s), page
        s = pat.sub(lambda m: form_block(key, name, fid) + '\n', s, count=1)
        s = re.sub(r'<p class="lead">הקובץ נפתח בטלפון ובמחשב, והוא שלכם לתמיד\.[^<]*</p>', '<p class="lead">הקובץ נפתח בטלפון ובמחשב, והוא שלכם לתמיד. השאירו כאן את הכתובת שאיתה תרצו לפתוח אותו.</p>', s, count=1)
    s = s.replace('\n</body>', JS + '\n</body>', 1)
    open(path, 'w', encoding='utf-8').write(s)
    print('patched', page)
