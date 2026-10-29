# -*- coding: utf-8 -*-
"""מתג אחד: הבלוג מוסתר או גלוי (29.10.2026).

LIVE = False  → העמודים חיים בכתובת אמיתית, אבל מוסתרים:
                אין לינק בתפריט ובפוטר של שאר האתר, אין במפת האתר,
                ויש תגית noindex שאומרת לגוגל לא לסרוק. רק מי שיש לו
                את הקישור מגיע. ככה שולחים לשקמה לאישור.

LIVE = True   → פותחים לציבור: לינק בתפריט ובפוטר של כל האתר,
                שורה בעמוד ״תוכן ומדריכים״, שישה עמודים במפת האתר,
                ו-noindex יורד.

מריצים אחרי page_blog.py. אפשר להריץ שוב ושוב, ולהחליף כיוון בכל רגע.
"""
import glob, os, re

LIVE = False

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
BLOG_PAGES = ['blog.html', 'kinaa-tzmudim.html', 'visut-regashi.html',
              'bitachon-atzmi.html', 'tiyugim.html', 'hitnahaguyot-tzmudim.html']

NAV_LINK = '      <a href="blog.html">הבלוג</a>\n'
F_LINK = '          <li><a href="blog.html">הבלוג</a></li>\n'
NAV_AFTER = '      <a href="guides.html">תוכן ומדריכים</a>\n'
F_AFTER = '          <li><a href="guides.html">תוכן ומדריכים</a></li>\n'

NOINDEX = '<meta name="robots" content="noindex, nofollow">\n'
GUIDES_LINE = ('    <p class="lead">יש גם <a href="blog.html">בלוג עם תכנים חינמיים</a>: '
               'ויסות רגשי, ביטחון עצמי, קנאה בין אחים, איך לדבר עם ילדים '
               'והתנהגויות שחוזרות בבית עם צמודים.</p>\n')
GUIDES_ANCHOR = 'מחבר את כל הרגעים האלה לדרך אחת'

nav_n = foot_n = idx_n = 0
for path in sorted(glob.glob(os.path.join(ROOT, '*.html'))):
    name = os.path.basename(path)
    html = open(path, encoding='utf-8').read()
    orig = html
    is_blog = name in BLOG_PAGES

    # ── תגית noindex: רק על עמודי הבלוג, רק כשהם מוסתרים ──
    if is_blog:
        has = NOINDEX.strip() in html
        if not LIVE and not has:
            html = html.replace('<meta charset="utf-8">\n',
                                '<meta charset="utf-8">\n' + NOINDEX, 1)
            idx_n += 1
        elif LIVE and has:
            html = html.replace(NOINDEX, '', 1)
            idx_n += 1

    # ── לינק בתפריט ובפוטר: בעמודי הבלוג תמיד (כדי שאפשר יהיה לנווט
    #    ביניהם בבדיקה), בשאר האתר רק כשהבלוג גלוי ──
    want = LIVE or is_blog
    nav_m = re.search(r'<nav>.*?</nav>', html, re.S)
    if nav_m:
        nav, has = nav_m.group(0), NAV_LINK in nav_m.group(0)
        new = None
        if want and not has and NAV_AFTER in nav:
            new = nav.replace(NAV_AFTER, NAV_AFTER + NAV_LINK, 1)
        elif not want and has:
            new = nav.replace(NAV_LINK, '', 1)
        if new:
            html = html[:nav_m.start()] + new + html[nav_m.end():]
            nav_n += 1

    has_f = F_LINK in html
    if want and not has_f and F_AFTER in html:
        html = html.replace(F_AFTER, F_AFTER + F_LINK, 1); foot_n += 1
    elif not want and has_f:
        html = html.replace(F_LINK, '', 1); foot_n += 1

    # ── השורה בעמוד ״תוכן ומדריכים״ ──
    if name == 'guides.html':
        has_g = 'blog.html">בלוג עם תכנים חינמיים' in html
        if LIVE and not has_g:
            m = re.search(r'    <p class="lead">[^\n]*%s[^\n]*</p>\n' % re.escape(GUIDES_ANCHOR), html)
            if m:
                html = html[:m.end()] + GUIDES_LINE + html[m.end():]
        elif not LIVE and has_g:
            html = re.sub(r'    <p class="lead">יש גם <a href="blog\.html">.*?</p>\n', '', html, count=1)

    if html != orig:
        open(path, 'w', encoding='utf-8').write(html)

print('מצב: %s' % ('גלוי לכולם' if LIVE else 'חי אבל מוסתר'))
print('תפריט: %d עמודים · פוטר: %d עמודים · noindex: %d עמודים' % (nav_n, foot_n, idx_n))

# ── מפת האתר ──
sm_path = os.path.join(ROOT, 'sitemap.xml')
sm = open(sm_path, encoding='utf-8').read()
before = sm
for u in BLOG_PAGES:
    line = '  <url><loc>https://imale.co/%s</loc></url>\n' % u
    present = line in sm
    if LIVE and not present:
        sm = sm.replace('</urlset>', line + '</urlset>')
    elif not LIVE and present:
        sm = sm.replace(line, '')
if sm != before:
    open(sm_path, 'w', encoding='utf-8').write(sm)
print('מפת האתר: %d כתובות' % sm.count('<url>'))
