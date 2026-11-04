# -*- coding: utf-8 -*-
"""4.11: הורדת הטופס שלפני התשלום ב-double.html (לבקשת שני).

מחזיר את שני כפתורי ״אני רוצה את המדריך״ שמובילים ישר ל-pay360 (הקישור שהיה ב-data-pay, 149 ₪),
ומסיר את הסקריפט של הטופס. אירוע click_payment ממשיך לעבוד דרך המאזין הכללי לקישורי pay360.
הטופס 202841816552179432 והקבוצה ״התחילו רכישה: הורות בדאבל״ נשארים ב-MailerLite, רק לא בשימוש. אידמפוטנטי."""
import pathlib, re
P = pathlib.Path(__file__).resolve().parents[2] / 'double.html'
h = P.read_text(encoding='utf-8')
if 'class="mform buyform"' not in h:
    print('already reverted'); raise SystemExit

FORM = re.compile(r'    <form class="mform buyform" novalidate data-pay="(https://pay360\.isracard\.co\.il/CustomerPayment/GenericURL\?SaleId=[0-9a-f-]+)">.*?</form>\n', re.S)
n = [0]
def rep(m):
    n[0] += 1
    return '    <a class="btn" href="%s">אני רוצה את המדריך</a>\n' % m.group(1)
h = FORM.sub(rep, h)
assert n[0] == 2, n

JS = re.compile(r'\n<script>\n\(function\(\)\{\n  var FORM=\'202841816552179432\';.*?</script>\n</body>', re.S)
h, k = JS.subn('</body>', h)
assert k == 1, k
P.write_text(h, encoding='utf-8')
print('ok: 2 buttons, form script removed')
