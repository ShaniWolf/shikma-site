# -*- coding: utf-8 -*-
"""מוסיף את הבלוג לתפריט העליון, לניווט בפוטר ולמפת האתר (29.10.2026).
רץ על כל קבצי ה-HTML החיים, כולל אלה שנבנו בסקריפטים הישנים. אפשר להריץ שוב ושוב.
"""
import glob, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
LINK = '<a href="blog.html">הבלוג</a>'
NAV_OLD = '      <a href="guides.html">תוכן ומדריכים</a>\n'
NAV_NEW = NAV_OLD + '      %s\n' % LINK
F_OLD = '          <li><a href="guides.html">תוכן ומדריכים</a></li>\n'
F_NEW = F_OLD + '          <li><a href="blog.html">הבלוג</a></li>\n'

# שורה שמפנה לבלוג מתוך עמוד ״תוכן ומדריכים״
GUIDES_ANCHOR = 'מחבר את כל הרגעים האלה לדרך אחת'
GUIDES_EXTRA = ('    <p class="lead">יש גם <a href="blog.html">בלוג עם תכנים חינמיים</a>: '
                'ויסות רגשי, ביטחון עצמי, קנאה בין אחים, איך לדבר עם ילדים '
                'והתנהגויות שחוזרות בבית עם צמודים.</p>\n')

nav_n = foot_n = 0
for path in sorted(glob.glob(os.path.join(ROOT, '*.html'))):
    name = os.path.basename(path)
    with open(path, encoding='utf-8') as f:
        html = f.read()
    orig = html
    # רק בתוך בלוק ה-<nav>, אחרת פירור הלחם ״הבלוג״ נראה כאילו התפריט כבר מעודכן
    nav_m = re.search(r'<nav>.*?</nav>', html, re.S)
    if nav_m and LINK not in nav_m.group(0) and NAV_OLD in nav_m.group(0):
        fixed = nav_m.group(0).replace(NAV_OLD, NAV_NEW, 1)
        html = html[:nav_m.start()] + fixed + html[nav_m.end():]
        nav_n += 1
    if '<li><a href="blog.html">' not in html and F_OLD in html:
        html = html.replace(F_OLD, F_NEW, 1)
        foot_n += 1
    if name == 'guides.html' and 'blog.html">בלוג עם תכנים חינמיים' not in html:
        m = re.search(r'    <p class="lead">[^\n]*%s[^\n]*</p>\n' % re.escape(GUIDES_ANCHOR), html)
        if m:
            html = html[:m.end()] + GUIDES_EXTRA + html[m.end():]
            print('  + שורה לבלוג בעמוד תוכן ומדריכים')
    if html != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print('patched', name)

print('תפריט עליון: %d עמודים · פוטר: %d עמודים' % (nav_n, foot_n))

# ───────── מפת האתר ─────────
NEW_URLS = ['blog.html', 'kinaa-tzmudim.html', 'visut-regashi.html',
            'bitachon-atzmi.html', 'tiyugim.html', 'hitnahaguyot-tzmudim.html']
sm_path = os.path.join(ROOT, 'sitemap.xml')
with open(sm_path, encoding='utf-8') as f:
    sm = f.read()
added = []
for u in NEW_URLS:
    loc = 'https://imale.co/%s' % u
    if loc not in sm:
        sm = sm.replace('</urlset>', '  <url><loc>%s</loc></url>\n</urlset>' % loc)
        added.append(u)
if added:
    with open(sm_path, 'w', encoding='utf-8') as f:
        f.write(sm)
print('נוספו למפת האתר:', ', '.join(added) if added else 'כלום (היה מעודכן)')

# ───────── common.py לעמודים עתידיים ─────────
cp = os.path.join(os.path.dirname(__file__), 'common.py')
with open(cp, encoding='utf-8') as f:
    src = f.read()
if 'blog.html">הבלוג' not in src:
    src = src.replace('      <a href="guides.html">תוכן ומדריכים</a>\n',
                      '      <a href="guides.html">תוכן ומדריכים</a>\n      <a href="blog.html">הבלוג</a>\n', 1)
    src = src.replace('          <li><a href="guides.html">תוכן ומדריכים</a></li>\n',
                      '          <li><a href="guides.html">תוכן ומדריכים</a></li>\n          <li><a href="blog.html">הבלוג</a></li>\n', 1)
    with open(cp, 'w', encoding='utf-8') as f:
        f.write(src)
    print('common.py עודכן')
else:
    print('common.py כבר מעודכן')
