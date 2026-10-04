# -*- coding: utf-8 -*-
"""4.10: ״הורים מספרים״ ב-double.html - 3 הודעות וואטסאפ על ״הורות בדאבל״ ששקמה שלחה.
מוצגות כבועות טקסט (wa-body chat) ולא כצילום מסך, כדי שלא יופיע שם שלב מהשיטה (״לתת מענה״) מההודעה הראשונה."""
import re, pathlib
P = pathlib.Path(__file__).resolve().parents[2] / 'double.html'
SIB = P.parent / 'siblings.html'
QUOTES = [
 'כבר באותו יום ששלחת לי סיימתי לקרוא הכל מרב שזה עניין אותי וכבר למחרת התחלתי ליישם!<br>אני ממש מרגישה את ההשפעה של המדריך על הרוגע בבית ושאני מבינה יותר מה לעשות כששניהם צריכים אותי יחד',
 'המדריך הזה זה החיים עצמם! כל סיטואציה שתיארת שם היא בול הבית שלנו!!!<br>התחלתי לחפש את הרגעים שחוזרים כמו שהמלצת שם והיום ממש הרגשתי שהצלחתי להחזיק את הסיטואציה לבד בלי להתפרק 🫶🏻',
 'הדוגמה על הצורך שהגדול צריך אותך - מושלמת כי זה מדוייק, ושרשמת שהמענה לא תמיד יפסיק את הבכי - עבורי זה שורה מאוד חשובה כי הייתי בסיטואציה כמה פעמים ועכשיו הרגעת לי את הרגשות אשם',
]
h = P.read_text(encoding='utf-8')
if 'aria-label="הורים מספרים"' in h:
    print('already there'); raise SystemExit
svg = re.search(r'<svg viewBox="0 0 24 24" aria-hidden="true">.*?</svg>', SIB.read_text(encoding='utf-8')).group(0)
slides = ''
for i, q in enumerate(QUOTES):
    d = ' style="--d:%.2fs"' % (i * .08) if i else ''
    slides += ('        <div class="car-slide">\n'
               '      <div class="wa-card rv%s">\n' % d +
               '        <div class="wa-head"><span class="wa-av" aria-hidden="true">א</span><span class="wa-name"><b>אמא שקראה את ״הורות בדאבל״</b></span>%s</div>\n' % svg +
               '        <div class="wa-body chat"><div class="wa-bubble">%s</div></div>\n' % q +
               '      </div>\n        </div>\n')
block = ('  <h2 style="margin-top:34px">הורים מספרים</h2>\n'
         '    <div class="carousel" data-carousel aria-roledescription="carousel" aria-label="הורים מספרים">\n'
         '      <button class="car-btn prev" type="button" aria-label="הקודם">‹</button>\n'
         '      <div class="car-track">\n' + slides +
         '      </div>\n'
         '      <button class="car-btn next" type="button" aria-label="הבא">›</button>\n'
         '      <div class="car-dots" role="tablist"></div>\n'
         '    </div>\n')
anchor = '  <section class="faqsec"'
assert h.count(anchor) == 1
h = h.replace(anchor, block + anchor)
P.write_text(h, encoding='utf-8')
print('ok')
