"""מבצע חגים: כל המדריכים ב-36 ₪ (עד מוצאי שמחת תורה, 3.10.2026).
ממתין לקישורי תשלום חדשים מישראכרט. להריץ: python3 patch_holiday_sale.py <tantrums> <gvulot> <together>
(שלושה SaleId או קישורים מלאים של 36 ₪). עורך את ה-HTML החי; אידמפוטנטי (<!--sale-->).
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAY = 'https://pay360.isracard.co.il/CustomerPayment/GenericURL?SaleId='
NOTE = 'מחיר מיוחד לחגים, עד מוצאי שמחת תורה (3.10)'

# (עמוד, SaleId נוכחי, מחיר מלא)
PRODUCTS = [
    ('tantrums.html', 'd6643811-bd77-d831-7aad-7c6a91377ba7', '99'),
    ('gvulot.html', '1a139f16-6092-3136-440c-d3c7d1f4ed8b', '99'),
    ('siblings.html', 'ec6f92a6-9e29-ce93-dd0b-70e2cc6f47a3', '149'),
]
GUIDE_CARDS = {'כשהבית מתפוצץ': '99', 'גבולות מתוך חיבור': '99', 'לגדול ביחד': '149'}


def sale_id(x):
    m = re.search(r'SaleId=([0-9a-f-]{36})', x) or re.fullmatch(r'([0-9a-f-]{36})', x.strip())
    assert m, 'לא נמצא SaleId: ' + x
    return m.group(1)


new_ids = [sale_id(a) for a in sys.argv[1:4]]
assert len(new_ids) == 3, 'צריך שלושה קישורים: כשהבית מתפוצץ, גבולות מתוך חיבור, לגדול ביחד'

for (page, old_id, full), new_id in zip(PRODUCTS, new_ids):
    p = ROOT / page
    s = p.read_text(encoding='utf-8')
    if '<!--sale-->' in s:
        print('skip', page); continue
    assert s.count(old_id) >= 1, page
    s = s.replace(PAY + old_id, PAY + new_id)
    s = s.replace('"price": "%s"' % full, '"price": "36"', 1)
    old_box = '<span class="cprice">%s ₪</span>' % full
    assert s.count(old_box) == 1, page
    s = s.replace(old_box, '<!--sale--><span class="cprice"><s style="opacity:.55;font-size:.6em">%s ₪</s> 36 ₪</span>\n    <p class="btn-note" style="margin-top:-6px">%s</p>' % (full, NOTE))
    p.write_text(s, encoding='utf-8')
    print('patched', page)

p = ROOT / 'guides.html'
s = p.read_text(encoding='utf-8')
if '<!--sale-->' not in s:
    for name, full in GUIDE_CARDS.items():
        old = '<p class="eyeb">%s ₪</p><h2>%s</h2>' % (full, name)
        assert s.count(old) == 1, name
        s = s.replace(old, '<p class="eyeb"><!--sale--><s>%s ₪</s> 36 ₪ · מחיר מיוחד לחגים</p><h2>%s</h2>' % (full, name))
    p.write_text(s, encoding='utf-8')
    print('patched guides.html')
