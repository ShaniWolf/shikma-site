"""25.9: השם כבר מופיע בראש כרטיס ההמלצה, אז מורידים את הכפילות בתחתית (wa-cap).
taima.html לא נוגעים: שם אין שם למעלה, רק למטה."""
import re, os
ROOT = os.path.join(os.path.dirname(__file__), '..', '..')
for f in ['index.html', 'tantrums.html', 'gvulot.html', 'livuy.html', 'siblings.html']:
    p = os.path.join(ROOT, f); h = open(p, encoding='utf-8').read()
    h = re.sub(r'\n[ \t]*<div class="wa-cap">[^<]*</div>', '', h)
    open(p, 'w', encoding='utf-8').write(h); print('patched', f)
