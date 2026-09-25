"""משפך הדאבל (25.9.2026): כל טופס מתנה באתר נרשם גם לטופס האחד ״משפך הדאבל״ ב-MailerLite,
עם שני שדות: gift (מה ביקשה) ו-gift_next (המתנה הבאה שתקבל במייל 2).
האוטומציה האחת משתמשת בהם בקישורים: imale.co/g.html?k={$gift}.
עורך את ה-HTML החי; אידמפוטנטי (FUNNEL_FORM). בנוסף יוצר את g.html (הפניה לקובץ לפי המתנה)."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[2]
FORM = '199587489820706610'
# מתנה -> המתנה הבאה
NEXT = {'lev': 'checklist', 'checklist': 'rush', 'rush': 'checklist', 'quiz': 'checklist'}

def funnel_js(gift_expr, body_var='body'):
    return ("  /* FUNNEL_FORM */ var gk=%s, gn={lev:'checklist',checklist:'rush',rush:'checklist'}[gk.split('-')[0]]||'checklist';\n"
            "  fetch('https://assets.mailerlite.com/jsonp/2618157/forms/%s/subscribe',{method:'POST',keepalive:true,headers:{'Content-Type':'application/x-www-form-urlencoded'},"
            "body:%s+'&fields%%5Bgift%%5D='+encodeURIComponent(gk)+'&fields%%5Bgift_next%%5D='+encodeURIComponent(gn)}).catch(function(){});\n") % (gift_expr, FORM, body_var)

GIFT = {'both-now.html': "'checklist'", 'rush-hour.html': "'rush'", 'quiz.html': "(window.IMALE_GIFT||'quiz')"}
for name, expr in GIFT.items():
    p = ROOT / name; s = p.read_text(encoding='utf-8')
    if 'FUNNEL_FORM' in s: print('skip', name); continue
    s, n = re.subn(r"(\n)(  fetch\('https://assets\.mailerlite\.com/jsonp/2618157/forms/'\+form\+'/subscribe')", lambda m: m.group(1) + funnel_js(expr) + m.group(2), s, count=1)
    assert n == 1, name
    if name == 'quiz.html':
        # התוצאה נשמרת כ-gift (quiz-a וכו׳), כדי שהקישור במייל יפתח בדיוק אותה
        s, n1 = re.subn(r"(show\('res-'\+res\); ga\('quiz_complete',\{result:res\}\);)", r"\1 window.IMALE_GIFT='quiz-'+res;", s)
        # פתיחה ישירה של תוצאה מקישור: quiz.html#r=a
        s, n2 = re.subn(r"(\n\}\)\(\);\n</script>\n</body>)",
            "\n  var hm=(location.hash||'').match(/^#r=([abcd])$/);\n"
            "  if(hm){ cur=root.querySelector('[data-step=res-'+hm[1]+']'); show('res-'+hm[1]); open(); ga('quiz_from_email',{result:hm[1]}); }\\1", s)
        assert (n1, n2) == (1, 1), (n1, n2)
    p.write_text(s, encoding='utf-8'); print('patched', name)

p = ROOT / 'lev.html'; s = p.read_text(encoding='utf-8')
if 'FUNNEL_FORM' not in s:
    s, n = re.subn(r"(\n)(    fetch\(EP,)", lambda m: m.group(1) + '  ' + funnel_js("'lev'").replace('\n  ', '\n    ') + m.group(2), s, count=1)
    assert n == 1
    p.write_text(s, encoding='utf-8'); print('patched lev.html')

G = '''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>אמאל׳ה צמודים</title>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XQ1HEQR5HK"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-XQ1HEQR5HK');
var M = {
  'lev': 'assets/d/11103785b16fa692/lev-full.pdf',
  'checklist': 'assets/d/b36f3b5e2ea9d89a/checklist-shneihem.pdf',
  'rush': 'assets/d/c7f508ddfe55c6b2/shaat-haomes.pdf',
  'quiz': 'quiz.html',
  'quiz-a': 'quiz.html#r=a', 'quiz-b': 'quiz.html#r=b', 'quiz-c': 'quiz.html#r=c', 'quiz-d': 'quiz.html#r=d',
  'double': 'double.html'
};
var k = (new URLSearchParams(location.search).get('k') || '').trim();
var to = M[k] || 'index.html';
gtag('event', 'email_gift_open', {gift: k || 'none'});
setTimeout(function(){ location.replace(to); }, 300);
</script>
</head>
<body style="font-family:Rubik,Arial,sans-serif;text-align:center;padding:40px 16px;background:#FBF7F0;color:#3A3128">
<p>רגע, מעבירה אותך...</p>
<p><a href="index.html" id="go" style="color:#B4694E">אם לא עברת אוטומטית, לחצי כאן</a></p>
<script>document.getElementById('go').href = to;</script>
</body>
</html>
'''
(ROOT / 'g.html').write_text(G, encoding='utf-8'); print('wrote g.html')
