# -*- coding: utf-8 -*-
"""עדכון 30.9.2026 לפי הגרסה המעודכנת (המקוצרת) של מדריך ״הורות בדאבל״ + תיקוני UI/UX של שקמה.
1. double.html: ״מה תמצאו במדריך?״ משקף את מבנה המדריך החדש: 3 חלקים, 6 פרקים, בשמות הפרקים מתוך המדריך עצמו
   (לשון רבים ניטרלית במקום ״את״). שורת הפתיחה מבוססת על ההנחיה בעמוד ״לפני שנתחיל״ של המדריך.
2. double.html: שאלת העצירה אחרי ״גם אצלכם זה נראה ככה?״ בולטת וגדולה (class q-stop).
3. tantrums.html: המקפים בבלוק ״הורות בדאבל״ (כותרת + שורת הסיום) הוסרו; בגלישת שורה המקף נחת בתחילת שורה ונראה זר.
4. style.css v38 → v39 בכל העמודים וב-common.py.
עורך HTML חי; אידמפוטנטי.
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
OLD_V, NEW_V = '38', '39'

PARTS = [
 ('חלק 1 · בתוך הרגע', [
   ('כששניהם צריכים אתכם', 'למה כל כך קשה לדעת מה לעשות כששניהם צריכים מכם משהו באותו רגע.'),
   ('למי ניגשים קודם?', 'איך להחליט למי לתת מענה קודם, בלי לבחור אוטומטית בצעיר או במי שבוכה חזק יותר.'),
   ('איך עוזרים לילד שצריך לחכות?', 'מה אפשר לעשות כשהוא רוצה אתכם עכשיו ואתם עדיין לא יכולים להתפנות אליו.'),
 ]),
 ('חלק 2 · החיים עצמם', [
   ('איך זה נראה בבית באמת?', 'כשהאכלה נמשכת, הערב מסתבך או שמה שהיה נכון לפני חמש דקות כבר לא מתאים למה שקורה עכשיו.'),
   ('איך מפחיתים מראש את רגעי ההתנגשות?', 'איך לזהות את הרגעים שחוזרים אצלכם ולהגיע אליהם קצת אחרת.'),
 ]),
 ('חלק 3 · גם כשלא הלך כמו שרציתם', [
   ('ואם היום לא הלך כמו שרציתם?', 'איך חוזרים לרגע שבו צעקתם, פספסתם או הבנתם רק אחר כך מה הילד שלכם היה צריך.'),
 ]),
]
INTRO = 'שלושה חלקים ושישה פרקים קצרים. אפשר לקרוא פעם אחת ברצף ואחר כך לחזור לפרקים שנוגעים ברגעים שהכי חוזרים אצלכם בבית.'


def learn_parts():
    out = ['  <h2 style="margin-top:34px">מה תמצאו במדריך?</h2>\n  <p class="learn-intro">%s</p>\n  <div class="learn-parts">\n' % INTRO]
    n = 0
    for title, items in PARTS:
        out.append('    <div class="learn-part rv">\n      <p class="learn-part-title">%s</p>\n      <div class="learn">\n' % title)
        for i, (h, t) in enumerate(items):
            d = (' style="--d:%ss"' % (i * .06)) if i else ''
            n += 1
            out.append('        <div class="learn-item"%s><span class="ln">פרק %d</span><h3>%s</h3><p>%s</p></div>\n' % (d, n, h, t))
        out.append('      </div>\n    </div>\n')
    out.append('  </div>\n')
    return ''.join(out)


def patch_double():
    p = ROOT / 'double.html'
    s = p.read_text(encoding='utf-8')
    # 1. guide structure
    m = re.search(r'  <h2 style="margin-top:34px">מה תמצאו במדריך\?</h2>\n(?:  <p class="learn-intro">.*?\n  <div class="learn-parts">\n.*?\n  </div>\n|  <div class="learn">\n.*?\n  </div>\n)', s, re.S)
    assert m, 'guide block not found'
    s = s[:m.start()] + learn_parts() + s[m.end():]
    # 2. scroll-stopping question
    q = 'ומה אם אתם לא אמורים לדעת לבד איך לפעול ברגע שבו שניהם צריכים אתכם ואי אפשר לתת לשניהם הכול?'
    s = s.replace('<p class="q">%s</p>' % q, '<p class="q q-stop">%s</p>' % q)
    assert 'q q-stop' in s
    p.write_text(s, encoding='utf-8')


def patch_tantrums():
    p = ROOT / 'tantrums.html'
    s = p.read_text(encoding='utf-8')
    s = s.replace('כשהוא כבר צורח והשני מתחיל לבכות — למי ניגשים קודם ומה עושים?', 'כשהוא כבר צורח והשני מתחיל לבכות, למי ניגשים קודם ומה עושים?')
    s = s.replace('לא כדי שלא יהיו יותר התפרצויות — אלא כדי שתדעו מה לעשות כשהן מגיעות.', 'לא כדי שלא יהיו יותר התפרצויות, אלא כדי שתדעו מה לעשות כשהן מגיעות.')
    p.write_text(s, encoding='utf-8')


CSS_ADD = '''/* v39: מבנה המדריך (3 חלקים) + שאלת עצירה בולטת */
.q-stop{font-size:1.45rem;line-height:1.45;font-weight:700;color:var(--warm-deep);background:var(--warm-soft);border-inline-start:5px solid var(--warm);border-radius:18px;padding:20px 22px;margin:24px 0 6px}
@media(max-width:640px){.q-stop{font-size:1.2rem;padding:16px 18px}}
.learn-intro{color:var(--soft);margin:-4px 0 4px}
.learn-parts{margin:8px 0 16px}
.learn-part+.learn-part{margin-top:18px}
.learn-part-title{font-family:'Varela Round','Rubik',sans-serif;color:var(--green);font-size:.95rem;margin:0 0 -6px}
.learn-part .learn{margin:12px 0 0}
.learn-item .ln{display:block;font-size:.78rem;color:var(--green);margin-bottom:2px}
'''


def patch_css():
    p = ROOT / 'style.css'
    s = p.read_text(encoding='utf-8')
    if '.q-stop{' not in s:
        s = s.rstrip('\n') + '\n' + CSS_ADD
    p.write_text(s, encoding='utf-8')


def bump_version():
    for p in ROOT.glob('*.html'):
        s = p.read_text(encoding='utf-8')
        t = s.replace('style.css?v=%s' % OLD_V, 'style.css?v=%s' % NEW_V)
        if t != s:
            p.write_text(t, encoding='utf-8')
    c = ROOT / 'spec/build/common.py'
    s = c.read_text(encoding='utf-8')
    c.write_text(s.replace("CSS_V = '%s'" % OLD_V, "CSS_V = '%s'" % NEW_V), encoding='utf-8')


if __name__ == '__main__':
    patch_double()
    patch_tantrums()
    patch_css()
    bump_version()
    print('ok')
