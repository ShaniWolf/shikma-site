# -*- coding: utf-8 -*-
"""Redirect stubs + in-place patches for the pages that keep their body (lev, chag, shana-tova, thanks-*, taima, legal, 404)."""
import re, os
from common import *

# 1) redirect stubs: product slugs -> merged topic pages
STUB = '''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="0; url=%(to)s">
<link rel="canonical" href="https://imale.co/%(canon)s">
<meta name="robots" content="noindex">
<title>%(title)s | שקמה דגרי</title>
<link rel="stylesheet" href="style.css?v=%(v)s">
<script>location.replace("%(to)s");</script>
</head>
<body>
<div class="wrap center" style="padding:4rem 0">
<p>העמוד עבר לכתובת חדשה.</p>
<p><a class="btn" href="%(to)s">%(title)s</a></p>
</div>
</body>
</html>
'''
for name, to, canon, title in [
    ('kshehabait.html', 'tantrums.html#guide', 'tantrums.html', 'כשהבית מתפוצץ'),
    ('gvulot-mechibur.html', 'gvulot.html#guide', 'gvulot.html', 'גבולות מתוך חיבור'),
    ('ligdol-beyachad.html', 'siblings.html#guide', 'siblings.html', 'לגדול ביחד'),
    ('together.html', 'siblings.html#guide', 'siblings.html', 'לגדול ביחד'),
    ('liyuy.html', 'livuy.html', 'livuy.html', 'צמודים בדרך שלכם'),
]:
    write(name, STUB % dict(to=to, canon=canon, title=title, v=CSS_V))

# 2) in-place patches
LINKMAP = {
    'kshehabait.html': 'tantrums.html#guide',
    'gvulot-mechibur.html': 'gvulot.html#guide',
    'ligdol-beyachad.html': 'siblings.html#guide',
}
HDR_RE = re.compile(r'<a class="skip" href="#main">דילוג לתוכן</a>\s*<header class="top">.*?</header>', re.S)
FTR_RE = re.compile(r'<footer>.*?</footer>', re.S)

for name in ['lev.html', 'chag.html', 'shana-tova.html', 'taima.html', 'privacy.html', 'terms.html', 'accessibility.html', '404.html',
             'thanks-lev.html', 'thanks-tantrums.html', 'thanks-gvulot.html', 'thanks-together.html', 'thanks-chagim.html']:
    path = os.path.join(ROOT, name)
    s = open(path, encoding='utf-8').read()
    orig = s
    s = HDR_RE.sub(lambda m: header().strip('\n'), s, count=1)
    s = FTR_RE.sub(lambda m: footer().strip('\n'), s, count=1)
    for k, v in LINKMAP.items():
        s = s.replace('href="%s"' % k, 'href="%s"' % v)
    s = s.replace('380+ הורים לצמודים', 'יותר מ־300 הורים לצמודים').replace('קהילה של 380+ הורים', 'קהילה של יותר מ־300 הורים')
    s = re.sub(r'style\.css\?v=\d+', 'style.css?v=' + CSS_V, s)
    s = re.sub(r'ui\.js\?v=\d+', 'ui.js?v=' + JS_V, s)
    # legal/404/thanks pages: make sure the click tracker exists once, harmless if not
    if s != orig:
        open(path, 'w', encoding='utf-8').write(s)
        print('patched', name)
    else:
        print('unchanged', name)

# 3) sitemap
pages = ['', 'tantrums.html', 'gvulot.html', 'siblings.html', 'guides.html', 'livuy.html', 'chagim.html', 'chag.html', 'lev.html', 'taima.html', 'shana-tova.html', 'privacy.html', 'terms.html', 'accessibility.html']
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join('  <url><loc>%s%s</loc></url>\n' % (SITE, p) for p in pages) + '</urlset>\n'
open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm)
print('sitemap', len(pages), 'urls')
