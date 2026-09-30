# -*- coding: utf-8 -*-
"""מסירת ״הורות בדאבל״ (30.9.2026): הקובץ המעודכן של שקמה עלה לאתר.
1. thanks-double.html — עמוד תודה לרכישה (noindex): כריכה, הורדה מיידית, טופס לכידת מייל (MailerLite),
   ״מאיפה להתחיל״ לפי תוכן העניינים של המדריך, קהילה, קראו עוד. נבנה מ-thanks-chagim.html (אותו JS/טופס).
   data-fid ריק = הטופס מוסתר עד שייווצר טופס ML לקבוצת ״רכשו: הורות בדאבל״ (199587285236189169).
2. double.html — כריכת המדריך באזור הרכישה הראשון (#buy).
3. guides.html — כרטיס ״הורות בדאבל״ מציג את הכריכה (כמו שאר כרטיסי המדריכים) במקום תמונת שקמה.
אידמפוטנטי.
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
PDF = 'assets/d/d8e26f50db3d1d8f/double-full.pdf'
COVER = 'assets/covers/double.png'
FID = ''  # טופס MailerLite לעמוד התודה — ממלאים אחרי יצירתו
COVER_TAG = '<div class="polaroid tall r"><img src="%s" alt="כריכת המדריך הורות בדאבל" loading="lazy" width="%d" height="%d"></div>'


def thanks():
    s = (ROOT / 'thanks-chagim.html').read_text(encoding='utf-8')
    rep = [
        ('<meta property="og:title" content="תודה על הרכישה | החגים עם צמודים">', '<meta property="og:title" content="תודה על הרכישה | הורות בדאבל">'),
        ('<title>תודה על הרכישה | החגים עם צמודים</title>', '<title>תודה על הרכישה | הורות בדאבל</title>'),
        ('<h1>תודה! ״החגים עם צמודים״ שלכם מוכן</h1>', '<h1>תודה! ״הורות בדאבל״ שלכם מוכן</h1>'),
        ('<p class="lead">אפשר לקרוא אותו תוך שעה: אילו עוגנים שומרים בחג, איפה מתגמשים, מה עושים כשילד אחד נהנה והשני כבר מוצף, ואיך עוברים את הנסיעות והארוחות.</p>',
         '<p class="lead">המדריך נבנה כדי לתת לכם דרך ברורה יותר לפעול בדיוק ברגעים שבהם שניהם צריכים אתכם. קראו אותו פעם אחת ברצף, ואחר כך חזרו לפרקים שנוגעים ברגעים שהכי חוזרים אצלכם בבית.</p>'),
        ('assets/covers/chagim.png', COVER),
        ('assets/d/d66ca34652049b85/chagim-full.pdf" download="החגים עם צמודים - שקמה דגרי.pdf"', PDF + '" download="הורות בדאבל - שקמה דגרי.pdf"'),
        ('data-fid="198150250229138748" data-product="chagim"', 'data-fid="%s" data-product="double"' % FID),
        ('קיבלתי. ״החגים עם צמודים״ בדרך ל', 'קיבלתי. ״הורות בדאבל״ בדרך ל'),
        ('<p class="btn-note">הקישור נשאר בתוקף גם אחרי החגים.</p>', '<p class="btn-note">הקובץ שלכם לתמיד, והקישור לא פג.</p>'),
        ('chagim-full', 'double-full'),
    ]
    for a, b in rep:
        assert a in s, a[:60]
        s = s.replace(a, b)
    # מאיפה להתחיל — לפי תוכן העניינים של המדריך (בלי לחשוף את שלבי השיטה)
    m = re.search(r'    <ul class="get">\n.*?    </ul>\n', s, re.S)
    assert m
    start = '''    <ul class="get">
      <li>אם הרגע שהכי חוזר אצלכם הוא ששניהם בוכים יחד, פתחו בפרק 2, ״למי ניגשים קודם?״: איך להחליט למי לתת מענה קודם, בלי לבחור אוטומטית בצעיר או במי שבוכה חזק יותר</li>
      <li>פרק 3, ״איך עוזרים לילד שצריך לחכות?״, נותן מה לעשות כשהוא רוצה אתכם עכשיו ואתם עדיין לא יכולים להתפנות אליו</li>
      <li>בערב שבו צעקתם, או הבנתם רק אחר כך מה הילד היה צריך, יש לכם את פרק 6: ״ואם היום לא הלך כמו שרציתם?״</li>
    </ul>
'''
    s = s[:m.start()] + start + s[m.end():]
    # הטופס מוסתר כל עוד אין טופס ML
    if FID == '' and 'data-fid=""' in s and 'if(!f.getAttribute(\'data-fid\'))' not in s:
        s = s.replace("var f=document.getElementById('mform'); if(!f) return;",
                      "var f=document.getElementById('mform'); if(!f) return; if(!f.getAttribute('data-fid')){f.hidden=true;return;}")
    assert 'חג' not in re.sub(r'<script.*?</script>', '', s, flags=re.S).split('<footer')[0].split('id="main"')[1], 'leftover chag text'
    (ROOT / 'thanks-double.html').write_text(s, encoding='utf-8')


def patch_double():
    p = ROOT / 'double.html'
    s = p.read_text(encoding='utf-8')
    if 'class="bcv"' not in s:
        s = s.replace('  <div class="cnext rv" id="buy">\n    <h2>הורות בדאבל</h2>',
                      '  <div class="cnext rv" id="buy">\n    <div class="bcv">%s</div>\n    <h2>הורות בדאבל</h2>' % (COVER_TAG % (COVER, 170, 241)), 1)
        assert 'class="bcv"' in s
    p.write_text(s, encoding='utf-8')


def patch_guides():
    p = ROOT / 'guides.html'
    s = p.read_text(encoding='utf-8')
    if COVER not in s:
        s = re.sub(r'(<div class="csec gcard rv" style="border:2px solid var\(--warm\)">\n)    <div class="polaroid r">.*?</div>\n',
                   lambda m: m.group(1) + '    ' + (COVER_TAG % (COVER, 140, 198)) + '\n', s, count=1, flags=re.S)
        assert COVER in s
    p.write_text(s, encoding='utf-8')


if __name__ == '__main__':
    thanks(); patch_double(); patch_guides(); print('ok')
