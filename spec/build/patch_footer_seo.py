"""פוטר SEO/AEO (25.9.2026): עמודת ״נושאים״ עם קישורים בניסוח של החיפושים הגדולים,
ותיאור שקמה שמחבר את הישות לביטויים ״מדריכת הורים לגיל הרך״, ״יועצת שינה״ ו״ילדים צמודים״.
נפחי חיפוש חודשיים בישראל (Ahrefs, ספטמבר 2026): טנטרום 1,700 · הדרכת הורים 1,600 ·
התקפי זעם אצל ילדים 400 · מדריכת הורים 250 · יועצת שינה 250 · הצבת גבולות לילדים 200 ·
מריבות בין אחים 150 · הדרכת הורים לגיל הרך 150. עורך את ה-HTML החי ישירות; אידמפוטנטי (f-topics).
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]

TOPICS = [
    ('tantrums.html', 'טנטרומים והתקפי זעם אצל ילדים'),
    ('gvulot.html', 'הצבת גבולות לילדים'),
    ('siblings.html', 'מריבות וקנאה בין אחים'),
    ('lev.html', 'הכנת הבכור לאח חדש'),
    ('double.html', 'הורות בדאבל: שני ילדים קטנים יחד'),
    ('chagim.html', 'חגים עם ילדים צמודים'),
    ('livuy.html', 'הדרכת הורים לגיל הרך'),
]

COL = '''      <div class="f-nav f-topics">
        <h3 class="f-h">נושאים</h3>
        <ul class="f-links">
%s        </ul>
      </div>
''' % ''.join('          <li><a href="%s">%s</a></li>\n' % t for t in TOPICS)

OLD_TAG = '<p class="f-tag">הדרכת הורים לגיל הרך</p>'
NEW_TAG = '<p class="f-tag">מדריכת הורים לגיל הרך ויועצת שינה</p>'
OLD_BIO = '<p class="f-bio">יוצרת שיטת ״הורות בדאבל״ למשפחות עם ילדים צמודים</p>'
NEW_BIO = '<p class="f-bio">מתמחה בילדים צמודים, בהפרש של עד שנתיים, ויוצרת שיטת ״הורות בדאבל״</p>'

n = 0
for p in sorted(ROOT.glob('*.html')):
    s = p.read_text(encoding='utf-8')
    if '<footer>' not in s or 'f-topics' in s:
        continue
    s = s.replace(OLD_TAG, NEW_TAG).replace(OLD_BIO, NEW_BIO)
    s, k = re.subn(r'(\n      <div class="f-connect">)', '\n' + COL.rstrip('\n') + r'\1', s, count=1)
    assert k == 1, p.name
    s = s.replace('style.css?v=32', 'style.css?v=33')
    p.write_text(s, encoding='utf-8')
    n += 1
print('patched', n, 'pages')
