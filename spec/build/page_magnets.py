# -*- coding: utf-8 -*-
"""Two free magnets for the ״הורות בדאבל״ funnel (25.9.2026):
checklist.html / thanks-checklist.html and omes.html / thanks-omes.html.
Each form posts to its own MailerLite form (groups: הרשמה מהאתר + the magnet's group).
"""
from common import *

MAGNETS = [
 dict(
  slug='checklist', form='199577369003951222',
  pdf='assets/d/b36f3b5e2ea9d89a/checklist-shneihem.pdf', dl='מה עושים כששניהם צריכים אותי עכשיו - שקמה דגרי.pdf',
  crumb='צ׳קליסט: כששניהם צריכים אותי',
  title='מה עושים כששניהם צריכים אותי עכשיו? צ׳קליסט להורים לצמודים | שקמה דגרי',
  desc='צ׳קליסט קצר מאת שקמה דגרי: למי ניגשים קודם כששני הילדים בוכים באותו רגע, ומה אומרים לילד שצריך לחכות. בחינם, מיד למייל.',
  kicker='צ׳קליסט קצר · 3 צעדים לרגע האמת',
  h1='״מה עושים כששניהם צריכים אותי עכשיו?״',
  lead='שניהם בוכים. אחד מושך אותך אליו, והשני כבר צורח מהצד. צ׳קליסט קצר שיעזור לך להבין למי לגשת קודם, ומה לומר לילד שצריך לחכות.',
  cover_alt='כריכת הצ׳קליסט מה עושים כששניהם צריכים אותי עכשיו',
  why_h='למה כל כך קשה להחליט?',
  why=['אין כלל שאומר שתמיד ניגשים לתינוק, לבכור או למי שבכה ראשון.', 'בכל פעם בודקים מחדש: מי צריך אותי מיד, מי יכול לחכות רגע, ואיך אני מראה גם לו שלא שכחתי אותו.'],
  learn=[('קודם כול: יש סכנה?', 'עוצרים את הסכנה ושומרים על הילדים. רק אחר כך ממשיכים.'),
         ('מי צריך עזרה מיד?', 'מי נפגע, מי זקוק לעזרה גופנית, ומי לא מצליח לעצור את עצמו.'),
         ('משפט אחד לילד שמחכה', 'לא צריך הסבר ארוך. ״אני רואה שגם אתה צריך אותי״ יכול להספיק.'),
         ('חוזרת אליו', 'כשהתפנית, חוזרים. כך הוא לומד שכשאת אומרת שתחזרי, את חוזרת.'),
         ('דוגמאות מהבית', 'מה עושים כשהבכור מטפס על השולחן באמצע ההאכלה, ומה עושים כשזה חוזר כל יום.')],
  btn='שלחו לי את הצ׳קליסט', get_h='הצ׳קליסט אצלכם תוך רגע',
  t_h1='הצ׳קליסט אצלכם', t_lead='אפשר לקרוא אותו עכשיו בדקה, ולחזור אליו ברגע האמת.',
  t_start='מהעמוד ״שניהם צריכים אותך, מה עושים עכשיו?״. ארבעה צעדים קצרים לפי הסדר, ואחריהם שתי דוגמאות מהבית.',
  ga='checklist',
 ),
 dict(
  slug='omes', form='199577372267119857',
  pdf='assets/d/c7f508ddfe55c6b2/shaat-haomes.pdf', dl='שעת העומס בדאבל - שקמה דגרי.pdf',
  crumb='שעת העומס בדאבל',
  title='שעת העומס בדאבל: מיני מדריך להורים לצמודים | שקמה דגרי',
  desc='מיני מדריך מאת שקמה דגרי: למה אותה שעה עם שני קטנטנים מסתבכת שוב ושוב, ומה אפשר לשנות כדי לעבור אותה עם יותר בהירות. בחינם, מיד למייל.',
  kicker='מיני מדריך · עם דף עבודה קצר',
  h1='שעת העומס בדאבל',
  lead='כמעט בכל בית עם שני קטנטנים יש שעה כזאת. החזרה מהמסגרות, ארוחת הערב, ההשכבות. מיני מדריך שיעזור לך להבין למה דווקא היא מסתבכת שוב ושוב, ומה אפשר לשנות.',
  cover_alt='כריכת המיני מדריך שעת העומס בדאבל',
  why_h='גם אצלכם יש שעה כזאת?',
  why=['אצל אחת היא מתחילה כשחוזרים מהמסגרות ושניהם רעבים.', 'אצל אחרת זו ארוחת הערב, כשאחד מסרב לשבת והשני כבר בוכה מעייפות.', 'ולפעמים אלה ההשכבות, כששניהם רוצים דווקא אותך ואף אחד מהם לא מצליח לחכות.'],
  learn=[('לא תמיד שניהם צריכים את אותו הדבר', 'אחד רעב והשני צריך כמה דקות של קרבה. איך מבחינים בזה בתוך הרעש.'),
         ('לחפש את הרגע שלפני', 'מה קורה רגע לפני שהכול מתפרק, ומה אפשר להקדים, לקצר או להוריד מראש.'),
         ('סדר קבוע, לא יום מושלם', 'סדר שחוזר על עצמו עוזר לכם ולילדים לדעת מה קורה עכשיו ומה יבוא אחר כך.'),
         ('דף עבודה: שעת העומס שלנו', 'שש שאלות קצרות לסמן ולהשלים, רק מה שמתאים לבית שלכם עכשיו.'),
         ('ביום שאין בו כוחות', 'על מה שומרים ועל מה מוותרים. ערב פשוט יותר הוא לא ערב שנכשל.')],
  btn='שלחו לי את המיני מדריך', get_h='המיני מדריך אצלכם תוך רגע',
  t_h1='״שעת העומס בדאבל״ אצלכם', t_lead='אין צורך לקרוא הכול עכשיו. מספיק לבחור שעה אחת שחוזרת אצלכם.',
  t_start='מדף העבודה ״שעת העומס שלנו״: מסמנים מתי הכי קשה, מה כל ילד צריך בשעה הזאת, ובוחרים דבר אחד להכין מראש.',
  ga='omes',
 ),
]

FORM_JS = '''<script>
document.querySelectorAll('form.mform[data-magnet]').forEach(function(f){
  var btn=f.querySelector('button'), err=f.querySelector('.err');
  f.addEventListener('submit', function(e){
    e.preventDefault();
    var email=f.querySelector('input[type=email]').value.trim();
    var nameEl=f.querySelector('input[type=text]'), name=nameEl?nameEl.value.trim():'';
    if(!email || email.indexOf('@')<1 || email.indexOf('.')<0){ err.textContent='צריך כתובת מייל תקינה כדי לשלוח את הקובץ'; return; }
    err.textContent=''; btn.disabled=true; btn.textContent='רגע, שולחת...';
    var done=false;
    function finish(){
      if(done) return; done=true;
      if(typeof gtag==='function'){ gtag('event','magnet_signup',{magnet:'%(ga)s',page_path:location.pathname}); }
      location.href='thanks-%(slug)s.html';
    }
    var body='fields%%5Bemail%%5D='+encodeURIComponent(email)+(name?'&fields%%5Bname%%5D='+encodeURIComponent(name)+'&fields%%5Bfirst_name%%5D='+encodeURIComponent(name.split(' ')[0]):'')+'&ml-submit=1&anticsrf=true';
    fetch('https://assets.mailerlite.com/jsonp/2618157/forms/%(form)s/subscribe',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:body}).then(finish).catch(finish);
    setTimeout(finish, 6000);
  });
});
</script>
'''

DL_JS = '''<script>
document.addEventListener('click', function(e){
  var a=e.target.closest('a'); if(!a || typeof gtag!=='function') return;
  if((a.href||'').indexOf('.pdf')>-1){ gtag('event','guide_download',{guide:'%s',page_path:location.pathname}); }
});
</script>
'''


def cover(m, w=220):
    return '<div class="cv"><div class="polaroid tall"><img src="assets/covers/%s.png" alt="%s" width="%d" height="%d"></div></div>' % (m['slug'], esc(m['cover_alt']), w, int(w * 1.416))


def landing(m):
    html = head(m['title'], m['desc'], m['slug'] + '.html', ld=[crumbs_ld((m['crumb'], SITE + m['slug'] + '.html'))], body_class='cpage')
    html += header()
    html += '<div class="wrap" id="main">\n' + crumb(m['crumb'])
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
''' % (m['kicker'], m['h1'], m['lead'], m['btn'], cover(m))
    html += csec('two', m['why_h'], p(*m['why']))
    html += '  <h2 style="margin-top:34px">מה יש בפנים?</h2>\n' + learn(m['learn'])
    html += '''
  <div class="cnext rv" id="get">
    <h2>%(get_h)s</h2>
    <p>משאירים מייל ומקבלים את הקובץ מיד.</p>
    <form class="mform" data-magnet id="mf" novalidate>
      <label for="mf-name">איך לפנות אליכם? (לא חובה)</label>
      <input type="text" id="mf-name" name="name" autocomplete="given-name" placeholder="שם פרטי">
      <label for="mf-email">כתובת מייל</label>
      <input type="email" id="mf-email" name="email" autocomplete="email" required placeholder="name@example.com">
      <button type="submit">%(btn)s</button>
      <p class="err" role="alert"></p>
      <p class="consent">הקובץ מגיע מיד לעמוד ההורדה. אשלח גם תכנים וכלים להורים לצמודים מדי פעם, ואפשר להסיר את הכתובת בלחיצה אחת בכל הודעה. פרטים ב<a href="privacy.html">מדיניות הפרטיות</a>.</p>
    </form>
  </div>
''' % m
    html += bio_box()
    html += readmore([
      ('double.html', 'two', 'הורות בדאבל', 'המדריך המלא: איך מבינים מה כל ילד צריך, למי ניגשים קודם ואיך עוזרים לילד שמחכה.', 'לכל הפרטים על המדריך'),
      ('tantrums.html', 'storm', 'טנטרומים והתפרצויות', 'מה קורה לילד בזמן הצפה, ומה עושים כשהבכי מגיע משני הכיוונים.', 'לקרוא עכשיו'),
    ])
    html += '</div>\n' + footer() + CLICK_JS.replace('</body>', FORM_JS % m + '</body>')
    write(m['slug'] + '.html', html)


def thanks(m):
    html = head(m['t_h1'] + ' | שקמה דגרי', m['desc'], 'thanks-' + m['slug'] + '.html')
    html = html.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex">', 1)
    html += header()
    html += '''<div class="wrap" id="main">
  <div class="hero">
    <div class="hero-cover">
      <div>
        <h1>%(t_h1)s</h1>
        <p class="lead">%(t_lead)s</p>
        <p><a class="btn" href="%(pdf)s" download="%(dl)s">להורדה (PDF)</a></p>
      </div>
      %(cv)s
    </div>
  </div>

  <div class="pain">
    <h3>מאיפה להתחיל</h3>
    <p>%(t_start)s</p>
  </div>

  <div class="cnext rv">
    <h2>ורוצים את הדרך המלאה?</h2>
    <p>״הורות בדאבל״ הוא המדריך שבו אני מפרקת את הרגע שבו שניהם צריכים אתכם לשלושה צעדים: להבין, לבחור ולתת מענה. עם דוגמאות מהבית ומה עושים גם כשהיום לא הלך כמו שרציתם.</p>
    <a class="btn" href="double.html">לכל הפרטים על המדריך</a>
  </div>

  <div class="cnext rv">
    <h2>ובינתיים, בואו לקהילה</h2>
    <p>בקהילת ״אמאל׳ה צמודים״ בוואטסאפ אני עונה בעצמי לשאלות של הורים לצמודים, ותוכלו לפגוש עוד הורים שמבינים בדיוק מה עובר עליכם.</p>
    <a class="btn green" href="%(wa)s" target="_blank" rel="noopener">להצטרפות לקהילה</a>
  </div>
</div>
''' % dict(m, cv=cover(m), wa=WA_GROUP)
    html += footer() + CLICK_JS.replace('</body>', DL_JS % m['ga'] + '</body>')
    write('thanks-' + m['slug'] + '.html', html)


for m in MAGNETS:
    landing(m)
    thanks(m)
