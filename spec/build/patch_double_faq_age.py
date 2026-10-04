# -*- coding: utf-8 -*-
"""4.10: שאלה חדשה משקמה בשאלות הנפוצות של double.html - לאילו גילאים המדריך מתאים (ראשונה ברשימה)."""
import json, re, pathlib
P = pathlib.Path(__file__).resolve().parents[2] / 'double.html'
Q = 'לאילו גילאים המדריך מתאים?'
PARAS = [
 '"הורות בדאבל" נכתב בעיקר להורים לשני ילדים קטנים, מהרגע שהצעיר נולד ועד בערך גיל 4.',
 'אבל הגיל הוא לא המדד היחיד. המדריך מתאים כל עוד יש אצלכם הרבה רגעים שבהם שני הילדים צריכים אותך יחד ואת מוצאת את עצמך מתלבטת למי לגשת קודם, איך לעזור לילד שצריך לחכות ואיך לתת מענה לשניהם בלי להתפצל לשתיים.',
 'אם אלה עדיין רגעים שחוזרים אצלכם בבית, סביר שתמצאי במדריך כלים שרלוונטיים לשלב שבו אתם נמצאים.',
]
h = P.read_text(encoding='utf-8')
if Q in h:
    print('already there'); raise SystemExit
anchor = '<div class="faq">\n'
item = '      <details><summary>%s</summary>%s</details>\n' % (Q, ''.join('<p>%s</p>' % p for p in PARAS))
assert h.count(anchor) == 1
h = h.replace(anchor, anchor + item)
ld = '"mainEntity": [\n'
assert h.count(ld) == 1
entry = json.dumps({"@type": "Question", "name": Q, "acceptedAnswer": {"@type": "Answer", "text": ' '.join(PARAS)}}, ensure_ascii=False, indent=1)
entry = '\n'.join('  ' + l for l in entry.split('\n'))
h = h.replace(ld, ld + entry + ',\n')
P.write_text(h, encoding='utf-8')
print('ok')
