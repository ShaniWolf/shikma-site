"""קידום כיפור בכל האתר (14.9.2026). עורך את ה-HTML החי ישירות (מחוללי page_* לא מסונכרנים עם עריכות 9.9, לא להריץ אותם).
אידמפוטנטי: כל בלוק מסומן ב-<!--kp-->.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import ICON

ROOT = pathlib.Path(__file__).resolve().parents[2]


def card(href, icon, h3, txt, go):
    return ('      <a class="rm-card" href="%s" aria-label="%s"><span class="ic">%s</span><span class="tx"><h3>%s</h3><p>%s</p></span>'
            '<span class="go"><span>%s</span></span></a>\n') % (href, h3, ICON[icon], h3, txt, go)


K_DAF = card('kippur.html#daf', 'list', 'מי עושה מה ביום כיפור?',
             'דף היערכות קצר להורים לצמודים: מי מוביל ומי נח, מה הילדים יאכלו, ומה עושים כשהם צריכים דברים שונים.', 'לדף ההיערכות')
K_ART = card('kippur.html', 'moon', 'יום כיפור עם צמודים: 5 דברים שכדאי לסגור מראש',
             'חלוקת תפקידים כשאחד צם, אוכל שקל להגיש, והיציאה לרחוב וגם הדרך חזרה.', 'לקרוא עכשיו')


def patch(name, old, new, marker='<!--kp-->'):
    p = ROOT / name
    s = p.read_text(encoding='utf-8')
    if marker in s:
        print('skip', name); return
    assert s.count(old) == 1, (name, s.count(old))
    p.write_text(s.replace(old, new), encoding='utf-8')
    print('patched', name)


# 1. chagim.html = עמוד הנחיתה של החגים: כלים לפי חג מיד אחרי ההירו, כיפור ראשון
chagim = (ROOT / 'chagim.html').read_text(encoding='utf-8')
first_csec = chagim.index('  <div class="csec')
if '<!--kp-->' not in chagim:
    block = '''  <!--kp--><div class="readmore rv" id="tools">
    <p class="rm-eyeb">כלים לפי חג</p>
    <h2>לקראת יום כיפור</h2>
    <div class="rm-grid">
%s%s    </div>
    <p class="btn-note" style="text-align:center">ומראש השנה: <a href="chag.html">חמישה דברים שמכינים מראש</a></p>
  </div>

''' % (K_DAF, K_ART)
    (ROOT / 'chagim.html').write_text(chagim[:first_csec] + block + chagim[first_csec:], encoding='utf-8'); print('patched chagim tools')

# readmore בתחתית: כיפור לפני ראש השנה
chagim = (ROOT / 'chagim.html').read_text(encoding='utf-8')
rh = chagim.index('      <a class="rm-card" href="chag.html"', chagim.index('<h2>קראו עוד בנושא</h2>'))
p = ROOT / 'chagim.html'
if '<!--kp2-->' not in chagim:
    p.write_text(chagim[:rh] + '<!--kp2-->\n' + K_ART + chagim[rh:], encoding='utf-8'); print('patched chagim readmore')

# 2. ריבון בדף הבית
patch('index.html',
      'חגיגת השקה: הבית החדש עלה לאוויר, ולכבוד החגים מחכה כאן משהו מיוחד · <a href="chagim.html">לעמוד החגים</a>',
      '<!--kp-->לקראת יום כיפור: מי עושה מה? דף היערכות קצר להורים לצמודים · <a href="kippur.html#daf">לדף ההיערכות</a>')

# 3. כרטיס החגים בעמוד המדריכים
patch('guides.html',
      '      <p><a class="btn" href="chagim.html">לפרטים על המדריך</a></p>\n',
      '      <p><a class="btn" href="chagim.html">לפרטים על המדריך</a></p>\n'
      '      <p class="btn-note"><!--kp-->לקראת יום כיפור: <a href="kippur.html#daf">מי עושה מה ביום כיפור?</a> דף היערכות קצר.</p>\n')

# 4. מאמר ראש השנה מפנה לכיפור
patch('chag.html',
      '  <h2>1. מספרים להם מה הולך לקרות</h2>',
      '''  <!--kp--><div class="pain">
    <h3>ראש השנה מאחורינו, יום כיפור בדרך</h3>
    <p><a href="kippur.html">יום כיפור עם צמודים: 5 דברים שכדאי לסגור מראש</a>, ודף היערכות קצר: <a href="kippur.html#daf">מי עושה מה ביום כיפור?</a></p>
  </div>

  <h2>1. מספרים להם מה הולך לקרות</h2>''')
