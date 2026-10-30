# -*- coding: utf-8 -*-
"""מעבר ממחיר ההשקה (99 ₪) למחיר המלא (149 ₪) של ״הורות בדאבל״. מתוכנן ליום ראשון 2.11.2026.

מה משתנה: double.html (מחיר, שורת ״מחיר השקה״, קישור התשלום, ה-JSON-LD), guides.html (שורת המחיר בכרטיס),
שישה עמודי הבלוג (השורה ״כרגע המדריך במחיר השקה לזמן מוגבל״), thanks-double.html (ערך אירוע purchase),
ושלושת סקריפטי הבנייה כדי שלא יחזירו את המחיר הישן. כלל ברזל 5: המחיר שמוצג = המחיר שהכפתור גובה.
אידמפוטנטי. SITE_ROOT בסביבה = הרצה על עותק (בדיקה יבשה)."""
import os, io, glob
ROOT = os.environ.get('SITE_ROOT') or os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
LAUNCH_ID = 'a24de58f-78ab-2ecf-dc1d-6ff250428b75'
FULL_ID = '6b5592a3-0bc0-0c74-0cf3-8144f0cda282'

def patch(rel, pairs, must=True):
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        print('missing', rel); return
    s = io.open(p, encoding='utf-8').read(); o = s; n = 0
    for a, b in pairs:
        c = s.count(a); n += c; s = s.replace(a, b)
    if s != o:
        io.open(p, 'w', encoding='utf-8').write(s)
    print('%-32s %d replacements' % (rel, n))

patch('double.html', [
    ('<span class="cprice"><s style="opacity:.55;font-size:.6em">149 ₪</s> 99 ₪</span>\n    <p class="btn-note" style="margin-top:-8px">מחיר השקה</p>\n',
     '<span class="cprice">149 ₪</span>\n'),
    ('SaleId=' + LAUNCH_ID, 'SaleId=' + FULL_ID),
    ('"price": "99",', '"price": "149",'),
])
patch('guides.html', [('<p class="eyeb"><s>149 ₪</s> 99 ₪ · מחיר השקה</p>', '<p class="eyeb">149 ₪</p>')])
for f in ['kinaa-tzmudim.html', 'visut-regashi.html', 'bitachon-atzmi.html', 'tiyugim.html', 'hitnahaguyot-tzmudim.html', 'maavarim-tzmudim.html']:
    patch(f, [('    <p class="btn-note">כרגע המדריך במחיר השקה לזמן מוגבל.</p>\n', '')])
patch('thanks-double.html', [("value:99,currency:'ILS',items:[{item_id:'double',item_name:'הורות בדאבל',price:99,",
                              "value:149,currency:'ILS',items:[{item_id:'double',item_name:'הורות בדאבל',price:149,")])
# סקריפטי הבנייה
patch('spec/build/page_double.py', [('LAUNCH = True\n', 'LAUNCH = False\n')])
patch('spec/build/page_blog.py', [("    <p class=\"btn-note\">כרגע המדריך במחיר השקה לזמן מוגבל.</p>\n", '')])
patch('spec/build/patch_purchase_event.py', [('PRICE = 99\n', 'PRICE = 149\n')])

# בדיקה: לא נשאר זכר למחיר ההשקה בעמודים החיים
left = []
for p in glob.glob(os.path.join(ROOT, '*.html')):
    s = io.open(p, encoding='utf-8').read()
    if LAUNCH_ID in s or ('מחיר השקה' in s and os.path.basename(p) not in ('chagim.html', 'taima.html')):
        left.append(os.path.basename(p))
print('נשאר מחיר השקה ב:', left or 'אף עמוד')
