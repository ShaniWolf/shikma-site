"""25.9: שקמה ביקשה להוריד המלצות שמזכירות מדריכים ישנים בשמם
(״כשהבית מתפוצץ״, ״לגדול ביחד״) ולהשאיר המלצות כלליות.
מחליף כל כרטיס כזה בכרטיס כללי שכבר קיים באתר (אותה תמונה, אותו טקסט חלופי)."""
import re, os
ROOT = os.path.join(os.path.dirname(__file__), '..', '..')
CARD = re.compile(r'<div class="wa-card rv"(?: style="[^"]*")?>.*?<div class="wa-cap">.*?</div>\s*</div>', re.S)

def read(f): return open(os.path.join(ROOT, f), encoding='utf-8').read()
def cards(html): return {re.search(r'assets/wa/([\w-]+)\.jpg', m.group(0)).group(1): m.group(0) for m in CARD.finditer(html)}

src = {}
for f in ['index.html', 'tantrums.html']:
    for k, v in cards(read(f)).items(): src.setdefault(k, v)
# tan-c עוד לא הופיע באתר: אותו כרטיס כמו tan-b, עם התמונה שלו
src['tan-c'] = src['tan-b'].replace('assets/wa/tan-b.jpg', 'assets/wa/tan-c.jpg').replace(
    re.search(r'alt="[^"]*"', src['tan-b']).group(0),
    'alt="הודעת וואטסאפ: פתאום אני ובעלי מדברים באותה שפה מול הילדים וזה הוריד המון מתח בבית. תודה!"')

PLAN = {
    'index.html':    {'tan-f': 'tan-e', 'lig-a': 'tan-a'},
    'tantrums.html': {'tan-f': 'tan-c'},
    'siblings.html': {'lig-a': 'gvu-e', 'lig-b': 'tan-b', 'lig-c': 'tan-a', 'lig-d': 'tan-c'},
}
def delay(card):
    m = re.match(r'<div class="wa-card rv"( style="[^"]*")?>', card); return m.group(1) or ''
for f, swaps in PLAN.items():
    html = read(f); cur = cards(html)
    for old, new in swaps.items():
        if old not in cur: print(f, old, 'already gone'); continue
        c = src[new]; c = re.sub(r'^<div class="wa-card rv"(?: style="[^"]*")?>', '<div class="wa-card rv"%s>' % delay(cur[old]), c)
        html = html.replace(cur[old], c)
    assert not re.search(r'assets/wa/(lig-|tan-f)', html), f
    open(os.path.join(ROOT, f), 'w', encoding='utf-8').write(html); print('patched', f)
