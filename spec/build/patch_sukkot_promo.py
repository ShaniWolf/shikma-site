"""סוכות מחליף את קידום כיפור (25.9.2026). עורך את ה-HTML החי ישירות, כמו patch_kippur_promo.
אידמפוטנטי: כל בלוק מסומן ב-<!--sk-->.
"""
import pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import ICON

ROOT = pathlib.Path(__file__).resolve().parents[2]


def card(href, icon, h3, txt, go):
    return ('      <a class="rm-card" href="%s" aria-label="%s"><span class="ic">%s</span><span class="tx"><h3>%s</h3><p>%s</p></span>'
            '<span class="go"><span>%s</span></span></a>\n') % (href, h3, ICON[icon], h3, txt, go)


S_CHECK = card('both-now.html', 'list', 'כששניהם צריכים אותי עכשיו',
               'צ׳קליסט קצר לחול המועד: למי ניגשים קודם כששניהם בוכים, ומה אומרים לילד שצריך לחכות.', 'לקבל את הצ׳קליסט')
S_OMES = card('rush-hour.html', 'clock', 'שעת העומס בדאבל',
              'הארוחה בסוכה, החזרה מהטיול, ההשכבות: מיני מדריך לשעה שמסתבכת שוב ושוב.', 'לקבל את המיני מדריך')


def sub(name, pattern, new, marker='<!--sk-->'):
    p = ROOT / name
    s = p.read_text(encoding='utf-8')
    if marker in s:
        print('skip', name); return
    s2, n = re.subn(pattern, lambda m: new, s, flags=re.S)
    assert n == 1, (name, n)
    p.write_text(s2, encoding='utf-8')
    print('patched', name)


# 1. ריבון בדף הבית
sub('index.html', r'<!--kp-->לקראת יום כיפור:.*?</a>',
    '<!--sk-->סוכות עם צמודים: ארוחות בסוכה, חול המועד ושינה מחוץ לבית · <a href="chagim.html">למדריך החגים</a>')

# 2. עמוד החגים: בלוק הכלים לפי חג
sub('chagim.html', r'  <!--kp--><div class="readmore rv" id="tools">.*?\n  </div>\n',
    '''  <!--sk--><div class="readmore rv" id="tools">
    <p class="rm-eyeb">כלים לפי חג</p>
    <h2>לחול המועד</h2>
    <div class="rm-grid">
%s%s    </div>
    <p class="btn-note" style="text-align:center">ומהחגים שעברו: <a href="chag.html">ראש השנה</a> · <a href="kippur.html">יום כיפור</a></p>
  </div>
''' % (S_CHECK, S_OMES))

# 3. כרטיס החגים בעמוד המדריכים
sub('guides.html', r'<p class="btn-note"><!--kp-->לקראת יום כיפור:.*?</p>',
    '<p class="btn-note"><!--sk-->לחול המועד: <a href="both-now.html">מה עושים כששניהם צריכים אותי עכשיו?</a> צ׳קליסט קצר.</p>')

# 4. מאמר ראש השנה
sub('chag.html', r'  <!--kp--><div class="pain">.*?\n  </div>\n',
    '''  <!--sk--><div class="pain">
    <h3>סוכות כבר כאן</h3>
    <p>לחול המועד: <a href="both-now.html">מה עושים כששניהם צריכים אותי עכשיו?</a> צ׳קליסט קצר, ו<a href="chagim.html">המדריך ״חגים עם צמודים״</a> לכל מה שנשאר מהחגים.</p>
  </div>
''')
