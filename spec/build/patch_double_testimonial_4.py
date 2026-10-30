# -*- coding: utf-8 -*-
"""30.10: המלצה רביעית ב״הורים מספרים״ של double.html (צילום וואטסאפ ששני שלחה, 22:40).
הטקסט מילה במילה מההודעה. בדרך גם תוקן באג קטן: בכרטיסים 2-3 המרכאות של class נסגרו במקום הלא נכון."""
import pathlib
P = pathlib.Path(__file__).resolve().parents[2] / 'double.html'
Q4 = ('היי שקמה, סליחה על השעה<br>'
      'רק רציתי להגיד לך שמהרגע שקניתי את המדריך דאבל, אני שקועה בו ולא מצליחה להפסיק לקרוא 🥱<br>'
      'נופלים לי אסימונים ואני ממש מרגישה שזה שינה לי את קו המחשבה על ההתנהגות שלי לבנים שלי וגם איך שהם מתנהגים אחד לשני<br>'
      'ממש תודה זה מדריך מעולה ואני עדין לא סיימתי לקרוא ❤️😅')
h = P.read_text(encoding='utf-8')
# תיקון המרכאות בכרטיסים הקיימים
for d in ('0.08s', '0.16s'):
    h = h.replace('class="wa-card rv style="--d:%s""' % d, 'class="wa-card rv" style="--d:%s"' % d)
if 'נופלים לי אסימונים' in h:
    print('already there'); raise SystemExit
# מעתיקים את כרטיס 3 כתבנית לכרטיס 4
start = h.index('        <div class="car-slide">\n      <div class="wa-card rv" style="--d:0.16s"')
end = h.index('        </div>\n', h.index('</div></div>\n      </div>\n', start)) + len('        </div>\n')
card3 = h[start:end]
assert card3.count('car-slide') == 1 and 'הדוגמה על הצורך' in card3
import re
card4 = card3.replace('--d:0.16s', '--d:0.24s')
card4 = re.sub(r'<div class="wa-bubble">.*?</div></div>', '<div class="wa-bubble">%s</div></div>' % Q4, card4, count=1, flags=re.S)
assert 'נופלים לי אסימונים' in card4
h = h[:end] + card4 + h[end:]
P.write_text(h, encoding='utf-8')
print('ok: 4 cards')
