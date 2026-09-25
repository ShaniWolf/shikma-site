# -*- coding: utf-8 -*-
"""שלוש המתנות (אפיון שקמה ״עדכון לאחר יצירת מדריך הורות בדאבל״, 25.9.2026). טקסטים מילה במילה מהאפיון.
both-now.html, rush-hour.html (+ עמודי תודה) ו-quiz.html. checklist.html / omes.html הישנים מפנים לכתובות החדשות.
טפסים: שם פרטי, שם משפחה ומייל חובה, טלפון רשות, אישור דיוור חובה.
"""
import json
from common import *

ML = 'https://assets.mailerlite.com/jsonp/2618157/forms/%s/subscribe'
BTN_DOUBLE = '<a class="btn" href="double.html">להכיר את ״הורות בדאבל״</a>'
CONSENT_FILE = 'אני מאשרת לקבל משקמה תכנים, כלים ועדכונים. אפשר להסיר את ההרשמה בכל עת.'
BIO = '''  <div class="csec rv" style="background:var(--warm-soft);border-color:#EBD9CC">
    <div class="aut">
      <img src="assets/shikma.jpg" alt="שקמה דגרי" loading="lazy">
      <div class="tx">
        <h2 style="margin-top:0">נעים להכיר</h2>
        <p>אני שקמה דגרי, מדריכת הורים ויועצת שינה מוסמכת לגיל הרך, ואמא לצמודים בהפרש של שנה וחודש. מתוך החיים עם שני קטנטנים והעבודה עם משפחות יצרתי את שיטת „הורות בדאבל” — כדי לעזור להורים להבין מה כל ילד צריך ולדעת מה לעשות גם כששניהם צריכים אותם יחד.</p>
      </div>
    </div>
  </div>
'''


def fields(consent, btn):
    return '''      <label for="mf-name">שם פרטי</label>
      <input type="text" id="mf-name" name="name" autocomplete="given-name" required placeholder="שם פרטי">
      <label for="mf-last">שם משפחה</label>
      <input type="text" id="mf-last" name="last_name" autocomplete="family-name" required placeholder="שם משפחה">
      <label for="mf-email">כתובת מייל</label>
      <input type="email" id="mf-email" name="email" autocomplete="email" required placeholder="name@example.com">
      <label for="mf-phone">מספר טלפון (לא חובה)</label>
      <input type="tel" id="mf-phone" name="phone" autocomplete="tel" inputmode="tel" placeholder="050-0000000">
      <label class="chk"><input type="checkbox" id="mf-ok" required> %s</label>
      <button type="submit">%s</button>
      <p class="err" role="alert"></p>
      <p class="consent">פרטים ב<a href="privacy.html">מדיניות הפרטיות</a>.</p>
''' % (consent, btn)


SUBMIT_JS = '''<script>
window.imaleSubmit = function(f, form, magnet, done){
  var btn=f.querySelector('button[type=submit]'), err=f.querySelector('.err');
  var v=function(id){ var el=f.querySelector('#'+id); return el ? el.value.trim() : ''; };
  var name=v('mf-name'), last=v('mf-last'), email=v('mf-email'), phone=v('mf-phone');
  if(!name || !last){ err.textContent='צריך שם פרטי ושם משפחה'; return; }
  if(!email || email.indexOf('@')<1 || email.indexOf('.')<0){ err.textContent='צריך כתובת מייל תקינה'; return; }
  if(!f.querySelector('#mf-ok').checked){ err.textContent='צריך לאשר קבלת תכנים כדי להמשיך'; return; }
  err.textContent=''; btn.disabled=true; var label=btn.textContent; btn.textContent='רגע, שולחת...';
  var fin=false;
  function finish(){ if(fin) return; fin=true; btn.disabled=false; btn.textContent=label;
    if(typeof gtag==='function'){ gtag('event','magnet_signup',{magnet:magnet,page_path:location.pathname}); }
    done(); }
  var body='fields%5Bemail%5D='+encodeURIComponent(email)+'&fields%5Bname%5D='+encodeURIComponent(name)+'&fields%5Bfirst_name%5D='+encodeURIComponent(name)+'&fields%5Blast_name%5D='+encodeURIComponent(last)+(phone?'&fields%5Bphone%5D='+encodeURIComponent(phone):'')+'&ml-submit=1&anticsrf=true';
  fetch('https://assets.mailerlite.com/jsonp/2618157/forms/'+form+'/subscribe',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:body}).then(finish).catch(finish);
  setTimeout(finish, 6000);
};
document.addEventListener('click', function(e){
  var a=e.target.closest('a'); if(!a || typeof gtag!=='function') return;
  if((a.getAttribute('href')||'').indexOf('double.html')>-1){ gtag('event','click_double',{page_path:location.pathname}); }
});
</script>
'''


def finish_page(html, extra_js=''):
    return html + '</div>\n' + footer() + CLICK_JS.replace('</body>', SUBMIT_JS + extra_js + '</body>')


GIFTS = [
 dict(slug='both-now', old='checklist', form='199577369003951222', ga='checklist',
  pdf='assets/d/b36f3b5e2ea9d89a/checklist-shneihem.pdf', dl='מה עושים כששניהם צריכים אותי עכשיו - שקמה דגרי.pdf',
  title='מה עושים כששניהם צריכים אותי עכשיו? צ׳קליסט להורים לצמודים',
  desc='צ׳קליסט קצר שיעזור לך לדעת למי לגשת קודם, מה לומר לילד שמחכה ומה לעשות כששני הילדים צריכים אותך יחד.',
  crumb='מה עושים כששניהם צריכים אותי עכשיו?',
  kicker='צ׳קליסט קצר וללא עלות להורים לשני קטנטנים',
  h1='מה עושים כששניהם צריכים אותי עכשיו?',
  lead='שניהם בוכים. אחד מושך אותך אליו והשני כבר צורח מהצד. הצ׳קליסט יעזור לך לדעת למי לגשת קודם ומה לומר לילד שצריך לחכות.',
  cta='לקבלת הצ׳קליסט',
  s1=('למה הצ׳קליסט יכול לעזור?', ['אין כלל שאומר שתמיד ניגשים לתינוק, לבכור או למי שבכה ראשון. בכל פעם צריך לבדוק מחדש מי צריך אותך מיד, מי יכול לחכות רגע ואיך להראות גם לו שלא שכחת אותו.'], None),
  s2=('מה תמצאי בצ׳קליסט?', ['מה לבדוק קודם כששניהם צריכים אותך.', 'איך להחליט למי לגשת קודם.', 'מה לומר לילד שצריך לחכות.', 'איך לחזור אליו ולהראות לו שלא שכחת אותו.', 'דוגמה מהבית לרגע שבו הבטיחות משנה את סדר העדיפויות.', 'רעיון להכנה מראש כשהמצב חוזר שוב ושוב.']),
  submit='שלחו לי את הצ׳קליסט',
  after=('ומה אם אותם רגעים חוזרים שוב ושוב?', ['הצ׳קליסט יעזור לך לדעת מה לעשות ברגע עצמו. מדריך „הורות בדאבל” יעזור לך גם להבין מה עומד מאחורי ההתנהגות, מה אפשר להכין מראש ואיך להגיב בתוך גבולות, טנטרומים, קנאה ומריבות.']),
  dlbtn='להורדת הצ׳קליסט (PDF)'),
 dict(slug='rush-hour', old='omes', form='199577372267119857', ga='omes',
  pdf='assets/d/c7f508ddfe55c6b2/shaat-haomes.pdf', dl='שעת העומס בדאבל - שקמה דגרי.pdf',
  title='שעת העומס בדאבל מיני מדריך להורים לשני קטנטנים | שקמה דגרי',
  desc='מיני־מדריך שיעזור לך להבין למה אותה שעה מסתבכת שוב ושוב ומה אפשר להכין, לקצר או לשנות מראש בבית עם שני קטנטנים.',
  crumb='שעת העומס בדאבל',
  kicker='מיני־מדריך ללא עלות להורים לשני קטנטנים',
  h1='שעת העומס בדאבל',
  lead='מיני־מדריך שיעזור לך להבין למה אותה שעה מסתבכת שוב ושוב ומה אפשר לשנות כדי לעבור אותה עם יותר בהירות ופחות צעקות והתנגדויות.',
  cta='לקבלת המיני־מדריך',
  s1=('גם אצלכם יש שעה כזאת?', [], ['חוזרים מהמסגרות ושניהם רעבים.', 'בזמן ארוחת הערב אחד מסרב לשבת והשני כבר בוכה מעייפות.', 'בהשכבות שניהם רוצים דווקא אותך ואף אחד מהם לא מצליח לחכות.', 'את מנסה להכין אוכל, לקלח ולהגיע לסוף היום ולא יודעת מה לעשות קודם.']),
  s2=('מה תמצאי במיני־מדריך?', ['איך לבחור את השעה שחוזרת ומסתבכת אצלכם.', 'איך לבדוק מה כל ילד צריך דווקא בזמן הזה.', 'איך לזהות מה קורה רגע לפני שהכול מתחיל להסתבך.', 'מה אפשר להכין, להקדים, לקצר או להוריד מהשעה מראש.', 'איך לבנות סדר פשוט שלא תלוי בשעה מדויקת.', 'מה כדאי לשמור ועל מה אפשר לוותר ביום שאין בו כוחות.', 'דף קצר למילוי שיעזור לך לבחור שינוי אחד לשעת העומס הבאה.']),
  submit='שלחו לי את המיני־מדריך',
  after=('ומה קורה כשהכול משתנה ברגע?', ['עכשיו יש לך דרך לשנות שעה אחת שחוזרת אצלכם ולהכין מראש את מה שאפשר. אבל יהיו גם רגעים שלא יכולת להכין: אחד הילדים מתפרק בדיוק כשהשני צריך אותך, או שהצרכים משתנים באמצע.', 'בדיוק בשביל הרגעים האלה יצרתי את „הורות בדאבל” — כדי לעזור לך להבין מה כל ילד צריך ולדעת מה לעשות גם כשהכול קורה יחד.']),
  dlbtn='להורדת המיני־מדריך (PDF)'),
]


def cover(g, w=220):
    return '<div class="cv"><div class="polaroid tall"><img src="assets/covers/%s.png" alt="כריכת %s" width="%d" height="%d"></div></div>' % (g['old'].replace('omes', 'omes').replace('checklist', 'checklist'), esc(g['h1']), w, int(w * 1.416))


def gift_page(g):
    html = head(g['title'], g['desc'], g['slug'] + '.html', ld=[crumbs_ld((g['crumb'], SITE + g['slug'] + '.html'))], body_class='cpage')
    html += header() + '<div class="wrap" id="main">\n' + crumb(g['crumb'])
    html += '''
  <div class="hero">
    <div class="hero-cover">
      <div>
        <span class="kicker">%s</span>
        <h1>%s</h1>
        <p class="lead">%s</p>
        <p><a class="btn green" href="#get">%s</a></p>
      </div>
      %s
    </div>
  </div>
''' % (g['kicker'], g['h1'], g['lead'], g['cta'], cover(g))
    h, paras, items = g['s1']
    html += csec('two', h, p(*paras) + (ul(items) if items else ''))
    h, items = g['s2']
    html += csec('list', h, ul(items, cls='check') + '    <p><a class="btn green" href="#get">%s</a></p>\n' % g['cta'])
    html += '''  <div class="cnext rv" id="get">
    <h2>%s</h2>
    <form class="mform" id="mf" novalidate>
%s    </form>
  </div>
''' % (g['cta'], fields(CONSENT_FILE, g['submit']))
    html += BIO
    js = '''<script>
document.getElementById('mf').addEventListener('submit', function(e){ e.preventDefault();
  imaleSubmit(this, '%s', '%s', function(){ location.href='thanks-%s.html'; }); });
</script>
''' % (g['form'], g['ga'], g['slug'])
    write(g['slug'] + '.html', finish_page(html, js))


def thanks_page(g):
    html = head(g['h1'] + ' | שקמה דגרי', g['desc'], 'thanks-' + g['slug'] + '.html')
    html = html.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex">', 1)
    html += header() + '<div class="wrap" id="main">\n'
    html += '''  <div class="hero">
    <div class="hero-cover">
      <div>
        <h1>%s</h1>
        <p><a class="btn" href="%s" download="%s">%s</a></p>
      </div>
      %s
    </div>
  </div>
''' % (g['h1'], g['pdf'], g['dl'], g['dlbtn'], cover(g))
    h, paras = g['after']
    html += '  <div class="guide-intro rv">\n    <h2>%s</h2>\n%s    %s\n  </div>\n' % (h, p(*paras), BTN_DOUBLE)
    html += BIO
    dl = '''<script>
document.addEventListener('click', function(e){ var a=e.target.closest('a'); if(!a || typeof gtag!=='function') return;
  if((a.href||'').indexOf('.pdf')>-1){ gtag('event','guide_download',{guide:'%s',page_path:location.pathname}); } });
</script>
''' % g['ga']
    write('thanks-' + g['slug'] + '.html', finish_page(html, dl))


def redirect(old, new, title):
    write(old, '''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="0; url=%s">
<link rel="canonical" href="https://imale.co/%s">
<meta name="robots" content="noindex">
<title>%s | שקמה דגרי</title>
<script>location.replace("%s");</script>
</head>
<body><p><a href="%s">%s</a></p></body>
</html>
''' % (new, new, title, new, new, title))


for g in GIFTS:
    gift_page(g)
    thanks_page(g)
    redirect(g['old'] + '.html', g['slug'] + '.html', g['h1'])
    redirect('thanks-' + g['old'] + '.html', 'thanks-' + g['slug'] + '.html', g['h1'])


# ───────────────────────── quiz.html ─────────────────────────
Q = [
 ('באיזה רגע את מרגישה שהכל מתחיל להסתבך?', [('כששניהם קוראים לי או בוכים באותו רגע.', 'a'), ('כשצריך לעצור משהו, לצאת או לעבור לדבר הבא.', 'b'), ('כשמתחילה ביניהם חטיפה, מריבה או מכה.', 'c')]),
 ('איזו סיטואציה הכי מזכירה את הבית שלכם?', [('אמרתי שנגמר זמן המסך, ותוך רגע התחילו בכי וצעקות.', 'b'), ('אני מטפלת באחד, והשני מיד מתחיל לדרוש אותי או לעשות משהו שאסור.', 'a'), ('שניהם רוצים את אותו הדבר ואני מנסה להבין מי לקח למי ומי שיחק בו קודם.', 'c')]),
 ('מה הכי קשה לך לדעת ברגעים האלה?', [('מתי להתערב ואיך להגיב בלי לבחור צד.', 'c'), ('למי לגשת קודם ומה לעשות עם הילד שצריך לחכות.', 'a'), ('איך לשמור על הגבול בלי לצעוק או לוותר.', 'b')]),
 ('כשהבכי, ההתנגדות או המריבה מתחילים, מה את עושה בד"כ?', [('מסבירה שוב ושוב, ובסוף מרימה את הקול או מוותרת.', 'b'), ('מגיבה למי שבוכה חזק יותר ולא בטוחה אם בחרתי נכון.', 'a'), ('מנסה להבין מי התחיל ולהחליט מי צודק.', 'c')]),
 ('מה הכי מתיש אותך בסוף היום?', [('התחושה שכל היום הייתי צריכה לבחור מי מהם יקבל אותי קודם.', 'a'), ('אותם ויכוחים שחוזרים סביב מקלחת, יציאה מהבית, מסכים או אוכל.', 'b'), ('להפריד, לתווך ולפתור שוב ושוב את המריבות ביניהם.', 'c')]),
 ('איזו מחשבה עוברת לך בראש שוב ושוב?', [('“למה כל בקשה קטנה הופכת למאבק?”', 'b'), ('“איך אני אמורה להיות שם בשביל שניהם?”', 'a'), ('“למה הם לא מצליחים לשחק יחד בלי לריב?”', 'c')]),
 ('על מה את מרגישה הכי הרבה אשמה בסוף היום?', [('שאחד מהם שוב חיכה בזמן שטיפלתי בשני.', 'a'), ('שכעסתי על אחד מהם או דרשתי ממנו לוותר כדי שיהיה שקט.', 'c'), ('שצעקתי או ויתרתי על הגבול כי כבר לא היה לי כוח להתמודד עם ההתנגדות.', 'b')]),
 ('מה הכי היית רוצה לדעת לעשות אחרת?', [('איך להגיב למריבות, מכות וקנאה בלי לבחור צד.', 'c'), ('מה לעשות כששניהם צריכים אותי יחד.', 'a'), ('להציב גבול ולהישאר בו גם כשהילד בוכה או מתנגד.', 'b')]),
]
R = {
 'a': dict(big='הכי קשה לך כששניהם צריכים אותך יחד',
   desc=['אחד בוכה, השני מושך אותך אליו, ואת צריכה להחליט למי לגשת קודם כשברור לך ששניהם באמת צריכים אותך.', 'ברגעים האלה קל להגיב למי שבוכה חזק יותר, לנסות לעשות הכול יחד או להרגיש אשמה על הילד שנאלץ לחכות.'],
   tools=['בדקי אם אחד מהם נמצא בסכנה או זקוק לעזרה מיד.', 'גשי קודם לילד עם הצורך שלא יכול לחכות.', 'אמרי לילד שמחכה: "אני רואה שגם אתה צריך אותי. קודם אני עוזרת לאחיך ואז אני באה אליך".', 'חזרי אליו כפי שהבטחת: "חיכית לי. עכשיו אני איתך".'],
   tools_after=[],
   bridge=['הבחירה למי לגשת קודם היא רק חלק מהתמונה.', 'מדריך "הורות בדאבל" יעזור לך  להבין מה כל ילד צריך באמת ולדעת איך להגיב ברגעים האמיתיים של החיים עם שני קטנטנים - עם יותר בהירות ופחות צעקות, ניחושים ואשמה.']),
 'b': dict(big='הכי קשה לך כשהילדים מתנגדים לגבול',
   desc=['העומס אצלך מתחיל ברגעים שבהם צריך לעצור, לסיים משהו או לעבור לדבר הבא.', 'כיבוי מסך, יציאה מהבית, מקלחת או סיום משחק מתחילים בבקשה קטנה ותוך רגע מגיעים בכי, צעקות או טנטרום.', 'כשגם הילד השני זקוק לך, קשה עוד יותר להישאר ברורה. את עלולה להסביר שוב ושוב, להרים את הקול או לוותר רק כדי שהרגע ייגמר.'],
   tools=['ספרי לילד מראש מה עומד לקרות בצורה מוחשית.', 'כשהגיע הזמן, התקרבי אליו במקום לקרוא לו מהחדר השני.', 'אמרי את הגבול במשפט קצר.', 'הציעי בחירה בדרך, בלי להפוך את הגבול עצמו לבחירה.'],
   tools_after=[],
   bridge=['גבול אחד ברור יכול לעזור ברגע מסוים, אבל בבית עם צמודים הגבול כמעט אף פעם לא פוגש רק ילד אחד.', 'המדריך "הורות בדאבל" יעזור לך להבין מה עומד מאחורי ההתנגדות ולדעת מה לעשות גם כשהילד השני בוכה או זקוק לך.']),
 'c': dict(big='הכי קשה לך כשהם רבים ביניהם',
   desc=['העומס אצלך מתחיל בעיקר בין הילדים: חטיפות, מכות, קנאה ותחרות עלייך.', 'את מוצאת את עצמך בודקת מי התחיל, מבקשת מהבכור לוותר או מפרידה ביניהם שוב ושוב ולא בטוחה מתי להתערב ומה לומר בלי לבחור צד.'],
   tools=['עצרי פגיעה: "אני לא אתן לכם להרביץ".', 'תארי את מה שאת רואה בלי לבחור צד: "שניכם רוצים עכשיו את המשאית".', 'תני מילים למה שכל אחד רוצה.', 'רק אחר כך עזרי להם למצוא פתרון שמתאים לגילם.'],
   tools_after=[],
   bridge=['המריבה היא מה שרואים מבחוץ.', 'מתחתיה יכולים להיות תסכול, קנאה, קושי לחכות או רצון להרגיש שגם לי יש מקום ליד אמא.', 'המדריך "הורות בדאבל" יעזור לך לזהות מה כל ילד צריך ולדעת מתי להתערב ואיך לעצור פגיעה בלי לבחור צד.']),
 'd': dict(big='אצלך כל האתגרים מתחברים יחד',
   desc=['מהתשובות שלך לא עולה רגע אחד שבו תמיד הכי קשה לך, וזה הגיוני מאוד.', 'בבית עם שני ילדים קטנים דבר אחד מוביל מהר לדבר הבא: התנגדות למקלחת הופכת לבכי של שניהם, ומריבה על צעצוע הופכת לתחרות עלייך.'],
   tools_intro='בחרי סיטואציה אחת שחוזרת אצלכם ושאלי:',
   tools=['מה קרה רגע לפני?', 'מה כל ילד היה צריך ממני?', 'האם הייתי צריכה לעצור משהו, להציב גבול או לעזור לאחד מהם לחכות?', 'מה אני יכולה להכין מראש לפעם הבאה?'],
   tools_after=['אל תנסי לשנות הכול בבת אחת.', 'בחרי רגע אחד שחוזר כמעט בכל יום והתחילי ממנו.'],
   bridge=['זה בדיוק הרעיון של "הורות בדאבל":', 'לא לנסות לפתור כל בכי, התנגדות או מריבה בנפרד, אלא להבין מה כל ילד צריך ולדעת מה לעשות גם כשהכול קורה יחד.', 'במדריך תקבלי דרך ברורה שתוכלי לחזור אליה בכל פעם ששניהם צריכים אותך ואת לא בטוחה מה לעשות קודם.', 'כדי שתוכלי לפעול עם יותר בהירות ופחות צעקות, ניחושים ואשמה.']),
}
RESULT_NOTE = 'מדריך דיגיטלי להורים לשני ילדים קטנים לרגעים ששניהם צריכים אתכם יחד, עם כלים, דוגמאות ומשפטים שאפשר לקחת ישר הביתה.'


def result_html(k, r):
    tl = ('    <p>%s</p>\n' % r['tools_intro']) if r.get('tools_intro') else ''
    return '''  <div class="qz-step qz-res" data-step="res-%s" hidden>
    <p class="eyeb">התוצאה שלך</p>
    <h2>%s</h2>
%s    <h3>מה יכול לעזור לך כבר עכשיו?</h3>
%s%s%s    <div class="guide-intro" style="margin-top:22px">
%s      %s
      <p class="btn-note">%s</p>
    </div>
  </div>
''' % (k, r['big'], p(*r['desc']), tl, ul(r['tools'], cls='check'), p(*r['tools_after']) if r['tools_after'] else '',
       ''.join('      <p>%s</p>\n' % x for x in r['bridge']), BTN_DOUBLE, RESULT_NOTE)


qs = ''
for i, (q, opts) in enumerate(Q):
    qs += '''  <div class="qz-step" data-step="q%d" hidden>
    <p class="qz-prog">שאלה %d מתוך %d</p>
%s    <h2>%s</h2>
    <div class="qz-opts">
%s    </div>
  </div>
''' % (i, i + 1, len(Q), '    <p class="qz-hint">בחרי בכל שאלה את התשובה שהכי מזכירה את הבית שלכם בתקופה האחרונה.</p>\n' if i == 0 else '', q,
       ''.join('      <button type="button" class="qz-opt" data-cat="%s">%s</button>\n' % (c, t) for t, c in opts))

QTITLE = 'איפה הדאבל פוגש אותך? שאלון להורים לילדים צמודים | שקמה דגרי'
QDESC = 'שאלון קצר שיעזור לך לזהות מה יוצר אצלכם הכי הרבה עומס בהורות לשני קטנטנים ולקבל כלי ראשון שמתאים למה שקורה בבית.'
html = head(QTITLE, QDESC, 'quiz.html', ld=[crumbs_ld(('איפה הדאבל פוגש אותך?', SITE + 'quiz.html'))], body_class='cpage')
html += header() + '<div class="wrap" id="main">\n' + crumb('איפה הדאבל פוגש אותך?')
html += '''  <div class="qz" id="qz">
  <div class="qz-step" data-step="intro">
    <span class="kicker">שאלון קצר להורים לשני קטנטנים</span>
    <h1>איפה הדאבל פוגש אותך?</h1>
    <p class="lead">שאלון קצר שיעזור לך לזהות מה יוצר אצלכם הכי הרבה עומס ומה יכול לעזור לך כבר עכשיו.</p>
    <p class="lead">בסיום תקבלי תוצאה אישית וכלי אחד שתוכלי לנסות בבית.</p>
    <button type="button" class="btn" data-go="form">מתחילות בשאלון</button>
  </div>
  <div class="qz-step" data-step="form" hidden>
    <h2>לפני שמתחילות, איך לפנות אלייך?</h2>
    <form class="mform" id="mf" novalidate>
%s    </form>
  </div>
%s%s  </div>
''' % (fields('אני מאשרת לקבל משקמה תכנים, כלים ועדכונים במייל ובוואטסאפ. אפשר להסיר את ההרשמה בכל עת.', 'מתחילות בשאלון'),
       qs, ''.join(result_html(k, R[k]) for k in 'abcd'))
html += BIO
QJS = '''<script>
(function(){
  var root=document.getElementById('qz'), steps=root.querySelectorAll('.qz-step'), score={a:0,b:0,c:0}, qi=0, N=%d;
  function ga(n,x){ if(typeof gtag==='function') gtag('event',n,Object.assign({page_path:location.pathname},x||{})); }
  function show(name){ steps.forEach(function(s){ s.hidden = s.getAttribute('data-step')!==name; });
    root.scrollIntoView({behavior:'smooth',block:'start'}); }
  root.querySelector('[data-go=form]').addEventListener('click', function(){ show('form'); ga('quiz_start'); });
  document.getElementById('mf').addEventListener('submit', function(e){ e.preventDefault();
    imaleSubmit(this, '%s', 'quiz', function(){ show('q0'); }); });
  root.querySelectorAll('.qz-opt').forEach(function(b){ b.addEventListener('click', function(){
    score[b.getAttribute('data-cat')]++; qi++;
    if(qi<N){ show('q'+qi); return; }
    var k=['a','b','c'].sort(function(x,y){ return score[y]-score[x]; }), top=k[0];
    var res = (score[top]>=4 && score[top]-score[k[1]]>=2) ? top : 'd';
    show('res-'+res); ga('quiz_complete',{result:res});
  }); });
})();
</script>
''' % (len(Q), '199585225455436936')
write('quiz.html', finish_page(html, QJS))
