# -*- coding: utf-8 -*-
"""Shared building blocks for the imale.co pages (spec v2, 9.9.26)."""
import json, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CSS_V = '26'
JS_V = '10'
SITE = 'https://imale.co/'
WA_GROUP = 'https://chat.whatsapp.com/Fju9PGJPgFhL8h99M1mnX0'
CAL = 'https://calendar.app.google/Rqgzmeg3HPCNJg4cA'
WA_LIVUY = 'https://wa.me/972528594469?text=%D7%94%D7%99%D7%99%20%D7%A9%D7%A7%D7%9E%D7%94%2C%20%D7%90%D7%A9%D7%9E%D7%97%20%D7%9C%D7%A9%D7%9E%D7%95%D7%A2%20%D7%A2%D7%9C%20%D7%94%D7%9C%D7%99%D7%95%D7%95%D7%99%20%D7%94%D7%90%D7%99%D7%A9%D7%99'
PAY = {
    'kshehabait': 'https://pay360.isracard.co.il/CustomerPayment/GenericURL?SaleId=d6643811-bd77-d831-7aad-7c6a91377ba7',
    'gvulot': 'https://pay360.isracard.co.il/CustomerPayment/GenericURL?SaleId=1a139f16-6092-3136-440c-d3c7d1f4ed8b',
    'ligdol': 'https://pay360.isracard.co.il/CustomerPayment/GenericURL?SaleId=ec6f92a6-9e29-ce93-dd0b-70e2cc6f47a3',
    'chagim': 'https://pay360.isracard.co.il/CustomerPayment/GenericURL?SaleId=4bc33c76-8f0d-c8d0-6faa-5de4d97472ad',
}

HEART_PATH = 'M12 21c-.4 0-.8-.15-1.1-.44C6.7 16.9 3 13.6 3 9.9 3 6.9 5.3 4.6 8.2 4.6c1.5 0 2.9.66 3.8 1.72.9-1.06 2.3-1.72 3.8-1.72 2.9 0 5.2 2.3 5.2 5.3 0 3.7-3.7 7-7.9 10.66-.3.29-.7.44-1.1.44z'
HEART = '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="%s"/></svg>' % HEART_PATH
FAVICON = 'data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22%3E%3Cpath fill=%22%23B4694E%22 d=%22M12 21c-.4 0-.8-.15-1.1-.44C6.7 16.9 3 13.6 3 9.9 3 6.9 5.3 4.6 8.2 4.6c1.5 0 2.9.66 3.8 1.72.9-1.06 2.3-1.72 3.8-1.72 2.9 0 5.2 2.3 5.2 5.3 0 3.7-3.7 7-7.9 10.66-.3.29-.7.44-1.1.44z%22/%3E%3C/svg%3E'

WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.5 2 2 6.5 2 12c0 1.8.5 3.5 1.3 5L2 22l5.1-1.3c1.4.8 3.1 1.2 4.9 1.2 5.5 0 10-4.5 10-10S17.5 2 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3 .8.8-2.9-.2-.3C4 15.1 3.6 13.6 3.6 12c0-4.6 3.8-8.4 8.4-8.4s8.4 3.8 8.4 8.4-3.8 8.2-8.4 8.2zm4.6-6.2c-.3-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1-.2.3-.6.8-.8 1-.1.2-.3.2-.5.1-.3-.1-1.1-.4-2-1.2-.7-.7-1.2-1.5-1.4-1.7-.1-.3 0-.4.1-.5l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5 0-.1-.6-1.4-.8-1.9-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.5.1-.7.3-.2.3-.9.9-.9 2.2s.9 2.5 1.1 2.7c.1.2 1.9 2.9 4.5 4 .6.3 1.1.4 1.5.6.6.2 1.2.2 1.6.1.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2 0-.1-.2-.2-.5-.3z"/></svg>'

# section icons (48x48), reused from the existing content pages
ICON = {
 'heart': '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M24 6c-8 0-14 5.6-14 13 0 4.1 1.9 7.4 4.6 9.7V38a2 2 0 0 0 2 2h14.8a2 2 0 0 0 2-2v-9.3C36.1 26.4 38 23.1 38 19c0-7.4-6-13-14-13z" fill="#F6E9E1"/><path class="an-beat" style="transform-origin:24px 20px" d="M24 27.5c-.3 0-.6-.12-.85-.34C19.9 24.2 17 21.6 17 18.7c0-2.3 1.8-4.1 4.1-4.1 1.2 0 2.3.5 3 1.35.7-.85 1.8-1.35 3-1.35 2.3 0 4.1 1.8 4.1 4.1 0 2.9-2.9 5.5-6.15 8.46-.25.22-.55.34-.85.34z" fill="#B4694E"/><rect x="19" y="40" width="10" height="3.2" rx="1.6" fill="#7A8B6F"/></svg>',
 'two': '<svg viewBox="0 0 48 48" aria-hidden="true"><g class="an-sway" style="transform-origin:16px 24px"><circle cx="16" cy="15" r="6.5" fill="#B4694E"/><path d="M5.5 40c0-6 4.7-10.5 10.5-10.5S26.5 34 26.5 40v2h-21z" fill="#B4694E"/></g><g><circle cx="33" cy="18.5" r="5.5" fill="#7A8B6F"/><path d="M24 40c0-5 4-9 9-9s9 4 9 9v2H24z" fill="#7A8B6F"/></g></svg>',
 'tug': '<svg viewBox="0 0 48 48" aria-hidden="true"><path class="an-tug" style="transform-origin:24px 24px" d="M11 17c6-6 12 8 18 2s10-4 10-4" stroke="#B4694E" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M9 31c6-6 12 8 18 2s10-4 10-4" stroke="#7A8B6F" stroke-width="4" fill="none" stroke-linecap="round" opacity=".85"/></svg>',
 'tool': '<svg viewBox="0 0 48 48" aria-hidden="true"><g class="an-turn" style="transform-origin:17px 31px"><circle cx="17" cy="31" r="9" fill="none" stroke="#B4694E" stroke-width="4.5"/><path d="M22.5 25.5 38 10" stroke="#B4694E" stroke-width="4.5" stroke-linecap="round"/><path d="M31.5 16.5 36 21M35.5 12.5 40 17" stroke="#7A8B6F" stroke-width="4.5" stroke-linecap="round"/></g></svg>',
 'chat': '<svg viewBox="0 0 48 48" aria-hidden="true"><path class="an-pop" style="transform-origin:24px 22px" d="M9 12.5A3.5 3.5 0 0 1 12.5 9h23a3.5 3.5 0 0 1 3.5 3.5v16a3.5 3.5 0 0 1-3.5 3.5H22l-8.5 7v-7h-1A3.5 3.5 0 0 1 9 28.5z" fill="#F6E9E1"/><rect x="15" y="16" width="18" height="3.4" rx="1.7" fill="#B4694E"/><rect x="15" y="23" width="12" height="3.4" rx="1.7" fill="#7A8B6F"/></svg>',
 'clock': '<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="16" fill="#F6E9E1"/><g class="an-tick" style="transform-origin:24px 24px"><rect x="22.6" y="13" width="2.8" height="12" rx="1.4" fill="#B4694E"/></g><rect x="24" y="22.6" width="9" height="2.8" rx="1.4" fill="#7A8B6F"/><circle cx="24" cy="24" r="2.6" fill="#8A4A37"/></svg>',
 'cup': '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M10 20h22v11a9 9 0 0 1-9 9h-4a9 9 0 0 1-9-9z" fill="#B4694E"/><path d="M32 23h3.5a4.5 4.5 0 0 1 0 9H32z" fill="none" stroke="#B4694E" stroke-width="3.2"/><g class="an-rise"><rect x="16" y="8" width="3" height="8" rx="1.5" fill="#7A8B6F"/><rect x="23" y="6" width="3" height="10" rx="1.5" fill="#7A8B6F"/></g></svg>',
 'book': '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M8 10h13a5 5 0 0 1 5 5v25a5 5 0 0 0-5-5H8z" fill="#B4694E"/><path d="M40 10H27a5 5 0 0 0-5 5v25a5 5 0 0 1 5-5h13z" fill="#7A8B6F"/></svg>',
 'storm': '<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="15" cy="20" r="7.5" fill="#B4694E"/><circle cx="25" cy="15.5" r="9.5" fill="#B4694E"/><circle cx="34" cy="21" r="7" fill="#B4694E"/><rect x="8" y="19" width="33" height="10" rx="5" fill="#B4694E"/><path d="M27 30l-8 9.5h5.4l-3 7.5 10.4-11.5h-5.4l4-5.5z" fill="#8A4A37"/><circle cx="13.5" cy="36" r="2.2" fill="#7A8B6F"/><circle cx="36" cy="35" r="2.2" fill="#7A8B6F"/></svg>',
 'frame': '<svg viewBox="0 0 48 48" aria-hidden="true"><rect x="6.6" y="6.6" width="34.8" height="34.8" rx="11" fill="none" stroke="#B4694E" stroke-width="3.2"/><path d="%s" fill="#7A8B6F" transform="translate(10.2 9.3) scale(1.15)"/></svg>' % HEART_PATH,
 'hearts': '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="%s" fill="#B4694E" transform="translate(3.5 6) scale(1.18)"/><path d="%s" fill="#7A8B6F" stroke="#F6E9E1" stroke-width="2.4" transform="translate(23.5 21) scale(.78)"/></svg>' % (HEART_PATH, HEART_PATH),
 'hand': '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M14 26V13a3 3 0 0 1 6 0v9" fill="none" stroke="#B4694E" stroke-width="3.4" stroke-linecap="round"/><path d="M20 22v-5a3 3 0 0 1 6 0v5M26 18a3 3 0 0 1 6 0v6M32 22a3 3 0 0 1 6 0v9c0 6-4 11-11 11h-3c-4 0-6.5-1.6-8.6-4.6L9 31a3 3 0 0 1 5-3.4l2 2.6" fill="none" stroke="#B4694E" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="12" cy="10" r="2.4" fill="#7A8B6F"/></svg>',
 'calendar': '<svg viewBox="0 0 48 48" aria-hidden="true"><rect x="8" y="11" width="32" height="29" rx="6" fill="#F6E9E1"/><rect x="8" y="11" width="32" height="9" rx="6" fill="#B4694E"/><rect x="14" y="6" width="3.4" height="9" rx="1.7" fill="#7A8B6F"/><rect x="30.6" y="6" width="3.4" height="9" rx="1.7" fill="#7A8B6F"/><path class="an-pop" style="transform-origin:24px 30px" d="M18 30l4 4 8-8" fill="none" stroke="#7A8B6F" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 'sun': '<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="9" fill="#B4694E"/><g class="an-tick" style="transform-origin:24px 24px" stroke="#7A8B6F" stroke-width="3.2" stroke-linecap="round"><path d="M24 6v5M24 37v5M6 24h5M37 24h5M11.3 11.3l3.5 3.5M33.2 33.2l3.5 3.5M11.3 36.7l3.5-3.5M33.2 14.8l3.5-3.5"/></g></svg>',
 'moon': '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M30 8a16 16 0 1 0 10 28A13 13 0 0 1 30 8z" fill="#B4694E"/><circle cx="35" cy="13" r="2.2" fill="#7A8B6F"/><circle cx="40" cy="21" r="1.6" fill="#7A8B6F"/></svg>',
 'car': '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M8 27l4-10a4 4 0 0 1 3.7-2.5h16.6A4 4 0 0 1 36 17l4 10v9a2 2 0 0 1-2 2h-3a2 2 0 0 1-2-2v-2H15v2a2 2 0 0 1-2 2h-3a2 2 0 0 1-2-2z" fill="#B4694E"/><circle cx="15.5" cy="29.5" r="2.6" fill="#F6E9E1"/><circle cx="32.5" cy="29.5" r="2.6" fill="#F6E9E1"/><path d="M14 24h20l-2.4-6H16.4z" fill="#F6E9E1"/></svg>',
 'list': '<svg viewBox="0 0 48 48" aria-hidden="true"><rect x="10" y="8" width="28" height="34" rx="5" fill="#F6E9E1"/><rect x="17" y="16" width="14" height="3.2" rx="1.6" fill="#B4694E"/><rect x="17" y="23" width="14" height="3.2" rx="1.6" fill="#B4694E"/><rect x="17" y="30" width="9" height="3.2" rx="1.6" fill="#7A8B6F"/><rect x="18" y="4" width="12" height="7" rx="2.5" fill="#7A8B6F"/></svg>',
 'home': '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M8 24 24 9l16 15" fill="none" stroke="#B4694E" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M12 22v16a2 2 0 0 0 2 2h20a2 2 0 0 0 2-2V22" fill="#F6E9E1" stroke="#B4694E" stroke-width="3.2" stroke-linejoin="round"/><rect x="20.5" y="28" width="7" height="12" rx="1.5" fill="#7A8B6F"/></svg>',
}

def esc(s):
    return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')

def head(title, desc, path, ld=(), og_title=None, og_desc=None, body_class=''):
    url = SITE + path if path else SITE
    lds = '\n'.join('<script type="application/ld+json">\n%s\n</script>' % json.dumps(x, ensure_ascii=False, indent=1) for x in ld)
    return '''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XQ1HEQR5HK"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-XQ1HEQR5HK');
</script>
<script type="text/javascript">
(function(c,l,a,r,i,t,y){
    c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
    t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
    y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
})(window, document, "clarity", "script", "ye0z5twmdl");
</script>
<title>%s</title>
<meta name="description" content="%s">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<meta property="og:image" content="https://imale.co/assets/og.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="אמאל׳ה צמודים">
<meta property="og:locale" content="he_IL">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://imale.co/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Varela+Round&family=Rubik:wght@400;500;700&display=swap">
<link rel="canonical" href="%s">
<link rel="apple-touch-icon" href="https://imale.co/assets/apple-touch-icon.png">
<link rel="icon" href="%s">
<link rel="stylesheet" href="style.css?v=%s">
<script defer src="ui.js?v=%s"></script>
%s
</head>
<body%s>
''' % (esc(title), esc(desc), esc(og_title or title), esc(og_desc or desc), url, url, FAVICON, CSS_V, JS_V, lds, (' class="%s"' % body_class) if body_class else '')

def header(home=False):
    c = '' if home else 'index.html'
    return '''
<a class="skip" href="#main">דילוג לתוכן</a>
<header class="top">
  <div class="wrap">
    <a class="logo" href="index.html">
      %s
      אמאל׳ה צמודים
    </a>
    <nav>
      <a href="guides.html">תוכן ומדריכים</a>
      <a href="livuy.html">ליווי אישי</a>
      <a href="%s#community">הקהילה</a>
      <a href="%s#about">אודות</a>
    </nav>
  </div>
</header>
''' % (HEART, c, c)

CONTACT_ICONS = {
 'instagram': ('https://www.instagram.com/shikma_dagary', 'אינסטגרם', '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2-.1-1.3-.1-1.7-.1-4.9s0-3.6.1-4.9c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4 1.3-.1 1.7-.1 4.9-.1zm0 1.8c-3.1 0-3.5 0-4.8.1-1.1.1-1.5.2-1.8.3-.4.2-.7.3-1 .6-.3.3-.5.6-.6 1-.1.3-.3.7-.3 1.8-.1 1.3-.1 1.6-.1 4.8s0 3.5.1 4.8c.1 1.1.2 1.5.3 1.8.2.4.3.7.6 1 .3.3.6.5 1 .6.3.1.7.3 1.8.3 1.3.1 1.6.1 4.8.1s3.5 0 4.8-.1c1.1-.1 1.5-.2 1.8-.3.4-.2.7-.3 1-.6.3-.3.5-.6.6-1 .1-.3.3-.7.3-1.8.1-1.3.1-1.6.1-4.8s0-3.5-.1-4.8c-.1-1.1-.2-1.5-.3-1.8-.2-.4-.3-.7-.6-1-.3-.3-.6-.5-1-.6-.3-.1-.7-.3-1.8-.3-1.3-.1-1.6-.1-4.8-.1zm0 3c2.8 0 5 2.3 5 5s-2.2 5-5 5-5-2.3-5-5 2.2-5 5-5zm0 8.3c1.8 0 3.3-1.5 3.3-3.3S13.8 8.7 12 8.7 8.7 10.2 8.7 12s1.5 3.3 3.3 3.3zm5.2-9.7c.7 0 1.2.5 1.2 1.2s-.5 1.2-1.2 1.2S16 7.5 16 6.8s.5-1.2 1.2-1.2z"/></svg>'),
 'whatsapp': ('https://wa.me/972528594469', 'וואטסאפ', WA_SVG),
 'facebook': ('https://www.facebook.com/share/1GxCUn8s5S/', 'פייסבוק', '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 12c0-5.5-4.5-10-10-10S2 6.5 2 12c0 5 3.7 9.1 8.4 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7C18.3 21.1 22 17 22 12z"/></svg>'),
 'tiktok': ('https://www.tiktok.com/@shikma_dagary', 'טיקטוק', '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19.6 6.9c-1.4-.9-2.3-2.3-2.5-4h-3v12.4c0 1.6-1.3 2.9-2.9 2.9s-2.9-1.3-2.9-2.9 1.3-2.9 2.9-2.9c.3 0 .6.1.9.2V9.5c-.3 0-.6-.1-.9-.1-3.3 0-6 2.7-6 6s2.7 6 6 6 6-2.7 6-6V9.9c1.2.9 2.7 1.4 4.3 1.4V8.2c-.7 0-1.3-.2-1.9-.5v-.8z"/></svg>'),
 'mail': ('mailto:shikma.dagary@gmail.com', 'דוא״ל', '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4.2-8 5-8-5V6.4l8 5 8-5v1.8z"/></svg>'),
 'linkedin': ('https://www.linkedin.com/in/shikma-dagary', 'לינקדאין', '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.4 3H3.6C2.7 3 2 3.7 2 4.6v14.8c0 .9.7 1.6 1.6 1.6h16.8c.9 0 1.6-.7 1.6-1.6V4.6c0-.9-.7-1.6-1.6-1.6zM8 18.6H5V9.7h3v8.9zM6.5 8.4c-1 0-1.7-.8-1.7-1.7S5.5 5 6.5 5s1.7.8 1.7 1.7-.7 1.7-1.7 1.7zM19 18.6h-3v-4.7c0-1.1 0-2.6-1.6-2.6s-1.8 1.2-1.8 2.5v4.8h-3V9.7h2.9V11c.4-.8 1.4-1.6 2.9-1.6 3.1 0 3.6 2 3.6 4.7v4.5z"/></svg>'),
}

def footer(home=False):
    c = '' if home else 'index.html'
    icons = ''.join('          <a href="%s"%s aria-label="%s" title="%s">%s</a>\n' % (u, '' if u.startswith('mailto') else ' target="_blank" rel="noopener"', n, n, s)
                    for k in ('instagram', 'whatsapp', 'facebook', 'tiktok', 'mail', 'linkedin') for (u, n, s) in [CONTACT_ICONS[k]])
    return '''
<footer>
  <div class="wrap">
    <div class="f-grid">
      <div class="f-about">
        <img class="f-seal" src="assets/logo.jpg" alt="" loading="lazy">
        <a class="f-logo" href="index.html">
          %s
          שקמה דגרי
        </a>
        <p class="f-tag">הדרכת הורים לגיל הרך</p>
        <p class="f-bio">יוצרת שיטת ״הורות בדאבל״ למשפחות עם ילדים צמודים</p>
      </div>
      <div class="f-nav">
        <h3 class="f-h">ניווט</h3>
        <ul class="f-links">
          <li><a href="index.html">בית</a></li>
          <li><a href="guides.html">תוכן ומדריכים</a></li>
          <li><a href="livuy.html">ליווי אישי</a></li>
          <li><a href="%s#community">הקהילה</a></li>
          <li><a href="%s#about">אודות</a></li>
        </ul>
      </div>
      <div class="f-connect">
        <h3 class="f-h">יצירת קשר</h3>
        <a class="f-community" href="%s" target="_blank" rel="noopener">מצטרפים לקהילת ההורים</a>
        <p class="contact-cta">חפשו אמאלה צמודים גם ב...</p>
        <div class="contact">
%s        </div>
      </div>
    </div>
    <div class="f-bottom">
      <div class="f-copy">© 2026 שקמה דגרי · כל הזכויות שמורות</div>
      <div class="f-legal">
        <a href="terms.html">תנאי השימוש, הרכישה, האספקה והביטולים</a>
        <a href="privacy.html">מדיניות הפרטיות</a>
        <a href="accessibility.html">הצהרת נגישות</a>
      </div>
    </div>
  </div>
</footer>
''' % (HEART.replace('width="15" height="15"', 'width="19" height="19"'), c, c, WA_GROUP, icons)

CLICK_JS = '''
<script>
document.addEventListener('click', function(e){
  var a = e.target.closest('a');
  if(!a || typeof gtag !== 'function') return;
  var h = a.href || '';
  if(h.indexOf('pay360.isracard') > -1){
    gtag('event', 'click_payment', {product: (document.title.split('|')[0]||'').trim(), page_path: location.pathname});
  } else if(h.indexOf('calendar.app.google') > -1){
    gtag('event', 'book_call', {page_path: location.pathname});
  } else if(h.indexOf('wa.me') > -1 && h.indexOf('text=') > -1){
    gtag('event', 'livuy_inquiry', {page_path: location.pathname});
  } else if(h.indexOf('chat.whatsapp.com') > -1){
    gtag('event', 'join_community', {page_path: location.pathname});
  } else if(h.indexOf('lev.html') > -1){
    gtag('event', 'click_magnet', {magnet: 'lev', page_path: location.pathname});
  } else if(a.closest('.contact')){
    gtag('event', 'contact_click', {channel: (a.getAttribute('aria-label')||a.textContent||'').trim()});
  }
});
</script>
</body>
</html>
'''

CREDITS = {
 'pola-home': ('Helena Lopes', 'Pexels', 'https://www.pexels.com/photo/27176460/'),
 'pola-livuy': ('Helena Lopes', 'Pexels', 'https://www.pexels.com/photo/27176495/'),
 'pola-blocks': ('Marisa Howenstine', 'Unsplash', 'https://unsplash.com/photos/Cq9slNxV8YU'),
 'tex-blocks': ('Marisa Howenstine', 'Unsplash', 'https://unsplash.com/photos/Cq9slNxV8YU'),
 'pola-rug': ('Vika Glitter', 'Pexels', 'https://www.pexels.com/photo/1648389/'),
 'pola-tantrums': ('Luiza Braun', 'Unsplash', 'https://unsplash.com/photos/qaOrl2G-T1M'),
 'pola-gvulot': ('Keira Burton', 'Pexels', 'https://www.pexels.com/photo/6624423/'),
 'pola-siblings': ('Jonathan Borba', 'Pexels', 'https://www.pexels.com/photo/19773887/'),
 'shk-sunset': ('שקמה דגרי', '', ''), 'shk-kitchen': ('שקמה דגרי', '', ''), 'shk-bench': ('שקמה דגרי', '', ''), 'shk-grass': ('שקמה דגרי', '', ''), 'shk-sofa': ('שקמה דגרי', '', ''),
}
CREDIT_LINE = 'צילומים: Helena Lopes, Vika Glitter, Keira Burton, Jonathan Borba (<a href="https://www.pexels.com/license/" target="_blank" rel="noopener">Pexels</a>) · Marisa Howenstine, Luiza Braun (<a href="https://unsplash.com/license" target="_blank" rel="noopener">Unsplash</a>)'

def photo(name, alt='', cls='', eager=False, sizes='(max-width:760px) 170px, 230px'):
    who, src, url = CREDITS[name]
    ws = (1400,) if name.startswith('tex-') else (420, 800)
    srcset = lambda ext: ', '.join('assets/photos/%s-%d.%s %dw' % (name, w, ext, w) for w in ws)
    return ('<picture class="%s"><source type="image/webp" srcset="%s" sizes="%s">'
            '<img src="assets/photos/%s-%d.jpg" srcset="%s" sizes="%s" alt="%s"%s></picture>'
            ) % (cls, srcset('webp'), sizes, name, ws[-1], srcset('jpg'), sizes, esc(alt), '' if eager else ' loading="lazy"')

def polaroid(name, alt='', cap=None, cls='', eager=False):
    capx = ('<p class="cap">%s</p>' % cap) if cap else ''
    return '<div class="polaroid %s">%s%s</div>' % (cls, photo(name, alt, eager=eager), capx)

def polaroid_cover(src, alt='', cls='r', width=140):
    return '<div class="polaroid tall %s"><img src="%s" alt="%s" loading="lazy" width="%d" height="%d"></div>' % (cls, src, esc(alt), width, int(width*1.42))

def pola_side(name, alt=''):
    return '    <div class="pola-side rv">%s</div>\n' % polaroid(name, alt)

def crumb(name):
    return '  <div class="crumb"><a href="index.html">בית</a> › %s</div>\n' % name

def chead(icon, h2, eyeb=None, tag='h2'):
    e = ('<p class="eyeb">%s</p>' % eyeb) if eyeb else ''
    return '<div class="chead"><span class="si">%s</span><div class="tx">%s<%s>%s</%s></div></div>' % (ICON[icon], e, tag, h2, tag)

def csec(icon, h2, body, eyeb=None, extra_class='', style=''):
    st = (' style="%s"' % style) if style else ''
    return '  <div class="csec rv%s"%s>\n    %s\n%s  </div>\n' % ((' ' + extra_class) if extra_class else '', st, chead(icon, h2, eyeb), body)

def ul(items, cls='clist'):
    return '    <ul class="%s">\n%s    </ul>\n' % (cls, ''.join('      <li>%s</li>\n' % i for i in items))

def p(*paras):
    return ''.join('    <p>%s</p>\n' % x for x in paras)

def wa_card(label, cap, img=None, alt=None, text=None, time='21:14', delay=''):
    """WhatsApp testimonial card. Either a real screenshot (img/alt) or a chat bubble (text)."""
    d = (' style="--d:%s"' % delay) if delay else ''
    if img:
        body = '<div class="wa-body shot"><img src="%s" alt="%s" loading="lazy"></div>' % (img, esc(alt or ''))
    else:
        body = '<div class="wa-body chat"><div class="wa-bubble">%s<div class="wa-meta"><span class="wa-time">%s</span><span class="wa-tick" aria-hidden="true">✓✓</span></div></div></div>' % (text, time)
    return '''      <div class="wa-card rv"%s>
        <div class="wa-head"><span class="wa-av" aria-hidden="true">%s</span><span class="wa-name"><b>%s</b><small>%s</small></span>%s</div>
        %s
        <div class="wa-cap">%s</div>
      </div>
''' % (d, cap.strip()[0], cap, label, WA_SVG, body, cap)

def carousel(cards, label='המלצות'):
    return '''    <div class="carousel" data-carousel aria-roledescription="carousel" aria-label="%s">
      <button class="car-btn prev" type="button" aria-label="הקודם">‹</button>
      <div class="car-track">
%s      </div>
      <button class="car-btn next" type="button" aria-label="הבא">›</button>
      <div class="car-dots" role="tablist"></div>
    </div>
''' % (label, ''.join('        <div class="car-slide">\n%s        </div>\n' % c for c in cards))

def faq(items, title='שאלות נפוצות', section=True):
    inner = ''.join('      <details><summary>%s</summary>%s</details>\n' % (q, a if a.strip().startswith('<') else '<p>%s</p>' % a) for q, a in items)
    if section:
        return '  <section class="faqsec" style="border-top:none;padding:34px 0 10px"><h2>%s</h2><div class="faq">\n%s  </div></section>\n' % (title, inner)
    return '    <h2>%s</h2>\n    <div class="faq">\n%s    </div>\n' % (title, inner)

def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": re.sub('<[^>]+>', '', q), "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in items]}

def crumbs_ld(*items):
    lst = [("בית", SITE)] + list(items)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(lst)]}

def bio_box(product=None):
    """'אם עוד לא הכרנו' block, Shikma's 9.9 wording."""
    return '''  <div class="csec rv" style="background:var(--warm-soft);border-color:#EBD9CC">
    <div class="aut">
      <img src="assets/shikma.jpg" alt="שקמה דגרי" loading="lazy">
      <div class="tx">
        <p class="eyeb">אם עוד לא הכרנו</p>
        <h2 style="margin-top:0">שקמה דגרי</h2>
        <p>אני שקמה דגרי, מדריכת הורים ויועצת שינה מוסמכת לגיל הרך, בוגרת מצטיינת בהכשרות להדרכת הורים ולייעוץ שינה בגישה ההוליסטית, ואמא לצמודים בהפרש של שנה וחודש.</p>
        <p>מתוך החיים עם שני קטנטנים והעבודה עם משפחות יצרתי את שיטת ״הורות בדאבל״, דרך שעוזרת להבין מה כל ילד צריך ולדעת איך להגיב גם כששניהם צריכים אתכם יחד.</p>
        <p>אני בעלת תואר ראשון במדעי ההתנהגות ותואר שני בייעוץ ארגוני, ומנהלת את קהילת ״אמאל׳ה צמודים״, שבה חברים יותר מ־300 הורים.%s <a href="index.html#about">עוד עליי</a> · <a href="livuy.html">הליווי האישי</a></p>
      </div>
    </div>
  </div>
''' % ((' ' + product) if product else '')

def buy_box(name, price, pay, btn, lead, terms_note=True, anchor='buy'):
    return '''  <div class="cnext rv" id="%s">
    <h2>%s</h2>
    <p>%s</p>
    <span class="cprice">%s ₪</span>
    <a class="btn" href="%s">%s</a>
    <p class="btn-note">הגישה נשלחת באופן אישי, בדרך כלל בתוך זמן קצר בשעות הפעילות ולא יאוחר מיום עסקים אחד.<br>הגישה ניתנת לצפייה באמצעות כתובת הדוא״ל שאושרה ב־Google Drive. המדריך אינו ניתן להורדה או להעברה.</p>
    <p class="btn-note">בלחיצה על כפתור הרכישה אתם מאשרים שקראתם והסכמתם ל<a href="terms.html">תנאי השימוש, הרכישה, האספקה והביטולים</a> ול<a href="privacy.html">מדיניות הפרטיות</a>.</p>
  </div>
''' % (anchor, name, lead, price, pay, btn)

def readmore(cards):
    inner = ''
    for href, icon, h3, ptxt, go in cards:
        ic = ICON[icon] if icon in ICON else icon
        inner += '      <a class="rm-card" href="%s" aria-label="%s"><span class="ic">%s</span><span class="tx"><h3>%s</h3><p>%s</p></span><span class="go"><span>%s</span></span></a>\n' % (href, h3, ic, h3, ptxt, go)
    return '''  <div class="readmore rv">
    <p class="rm-eyeb">ממשיכים</p>
    <h2>קראו עוד בנושא</h2>
    <div class="rm-grid">
%s    </div>
  </div>
''' % inner

def pains(items):
    return '  <div class="pains">\n%s  </div>\n' % ''.join('    <div class="pain-card rv"%s><span class="pn">%d</span><p>%s</p></div>\n' % ((' style="--d:%ss"' % (i * .08)) if i else '', i + 1, t) for i, t in enumerate(items))

def learn(items):
    return '  <div class="learn">\n%s  </div>\n' % ''.join('    <div class="learn-item rv"%s><h3>%s</h3><p>%s</p></div>\n' % ((' style="--d:%ss"' % (i * .06)) if i else '', h, t) for i, (h, t) in enumerate(items))

def stages(items):
    return '  <div class="steps stages">\n%s  </div>\n' % ''.join('    <div class="step rv"%s><span class="n">%d</span><h3>%s</h3><p>%s</p></div>\n' % ((' style="--d:%ss"' % (i * .08)) if i else '', i + 1, h, t) for i, (h, t) in enumerate(items))

def write(name, html):
    path = os.path.join(ROOT, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('wrote', name, len(html.encode('utf-8')), 'bytes')
