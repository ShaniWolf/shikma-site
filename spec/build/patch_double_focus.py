"""מיקוד ב״הורות בדאבל״ (אפיון שקמה, 25.9.2026): עמודי התוכן נשארים, אזורי המכירה של המדריכים
הישנים מוחלפים בהפניה ל-double.html. הטקסטים מילה במילה מהאפיון. עורך את ה-HTML החי; אידמפוטנטי (<!--dbl-->).
"""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
BTN = '<a class="btn" href="double.html">להכיר את ״הורות בדאבל״</a>'


def promo(kicker, h, paras, items, note):
    k = ('    <span class="kicker">%s</span>\n' % kicker) if kicker else ''
    n = ('    <p class="btn-note">%s</p>\n' % note) if note else ''
    return ('  <!--dbl--><div class="guide-intro rv" id="guide">\n%s    <h2>%s</h2>\n%s    <ul class="check">\n%s    </ul>\n    %s\n%s  </div>\n\n'
            % (k, h, ''.join('    <p>%s</p>\n' % x for x in paras), ''.join('      <li>%s</li>\n' % i for i in items), BTN, n))


def bottom(h):
    return '  <div class="cnext rv" id="buy">\n    <h2>%s</h2>\n    %s\n  </div>\n' % (h, BTN)


PAGES = {
 'tantrums.html': dict(
   top=('ישר למדריך ״כשהבית מתפוצץ״', 'מה עושים כשהוא כבר מתפרץ?'),
   label=('על ״כשהבית מתפוצץ״', 'על הכלים להתמודדות עם התפרצויות'),
   promo=promo('הבנתם למה ההתפרצות מגיעה. עכשיו נשאר לדעת מה עושים.',
               'כשהוא כבר צורח והשני מתחיל לבכות — למי ניגשים קודם ומה עושים?',
               ['ברגעים האלה לא מספיק להבין למה הטנטרום התחיל. צריך לדעת למי לגשת קודם, מה לעשות עם הילד שמתפרץ ואיך לעזור גם לאח שלו שמחכה.',
                'זו בדיוק הדרך שמלמד מדריך ״הורות בדאבל״.'],
               ['להבין מה הילד מנסה להגיד דרך ההתפרצות.', 'לדעת למי לגשת קודם כששניהם בוכים.', 'לעזור גם לילד שמחכה להרגיש שלא שכחתם אותו.'],
               'לא כדי שלא יהיו יותר התפרצויות — אלא כדי שתדעו מה לעשות כשהן מגיעות.'),
   bottom=bottom('רוצים פחות לנחש ויותר לדעת מה לעשות כששניהם בוכים?')),
 'gvulot.html': dict(
   top=('ישר למדריך ״גבולות מתוך חיבור״', 'מה עושים כשהצבתם גבול והוא מתחיל לבכות?'),
   label=('על ״גבולות מתוך חיבור״', 'על הכלים להצבת גבולות'),
   promo=promo('הבנתם למה הילד מתנגד. אבל מה עושים כשהוא בוכה והשני מצטרף?',
               'הצבתם גבול. עכשיו צריך לדעת מה לעשות עם הבכי וההתנגדות',
               ['בבית עם שני קטנטנים, הצבת גבול לילד אחד משפיעה לא פעם גם על אחיו. אחד מתנגד, השני מגיב לבכי, ובתוך רגע אתם כבר מנסים להרגיע את שניהם.',
                'מדריך ״הורות בדאבל״ יעזור לכם להבין מה כל ילד צריך ולדעת מה לעשות גם כשהילד בוכה, מתנגד והאח שלו כבר מצטרף.'],
               ['להבין מה נמצא מאחורי ההתנגדות של הילד.', 'להציב גבול בלי לחזור בכם רק כדי שהבכי ייפסק.', 'לדעת מה לעשות כשילד אחד מתנגד והשני כבר דורש אתכם.'],
               'הורות מובילה אינה הורות קשוחה. אפשר להבין את הילד, להציב גבול ולהישאר בו גם כשהוא בוכה או כועס.'),
   bottom=bottom('רוצים לדעת איך להציב גבול בלי שהבכי יגרום לכם מיד לחזור בכם?')),
 'siblings.html': dict(
   top=None,
   label=('על ״לגדול ביחד״', 'על הכלים ליחסים בין האחים'),
   promo=promo(None, 'בשביל החיים שאחרי הלידה יצרתי את „הורות בדאבל”',
               ['מדריך מעשי שיעזור לכם להבין מה כל ילד צריך ולדעת למי לגשת ומה לעשות כששניהם צריכים אתכם באותו הרגע.',
                'המדריך אינו מבטיח שלא יהיו קנאה, בכי או מריבות. הוא יעזור לכם לדעת מה לעשות כשהרגעים האלה מגיעים, בלי לבחור מיד צד ובלי לצפות מעצמכם להיות בשני מקומות באותו הזמן.'],
               ['לדעת למי לגשת קודם כשהם צריכים אתכם יחד.', 'לעזור לילד שמחכה להרגיש שלא שכחתם אותו.', 'לעצור מכה או חטיפה בלי להפוך מיד ילד אחד ל״אשם״.'],
               None),
   bottom=''),
}

SIB_BRIDGE_P = ['״להכין את הלב״ יעזור לכם להכין את הילד ואת הבית לקראת השינוי. אחרי שהתינוק מצטרף, מתחילה מציאות חדשה: לפעמים שניהם צריכים אתכם יחד, הבכור מתקשה לחכות והתינוק צריך אתכם עכשיו.']
SIB_BRIDGE_Q = ['למי ניגשים קודם כששניהם בוכים?', 'איך נותנים מקום לקנאה בלי להיבהל ממנה?', 'איך עוצרים מכה או חטיפה בלי להפוך ילד אחד ל״אשם״?', 'איך עוזרים לילד שמחכה להרגיש שעדיין רואים אותו?']

# FAQ items that sell the old guide go; product sentences inside kept answers go too
FAQ_DROP = re.compile(r'<summary>[^<]*(המדריך|מדריך ארוך|לקרוא הכול|איך מקבלים)[^<]*</summary>')
IN_GUIDE = re.compile(r'\s*(במדריך|המדריך)[^.<]*\.')


def strip_csec(s, marker):
    """Remove the csec block whose heading contains marker."""
    i = s.find(marker)
    if i < 0:
        return s
    a = s.rfind('  <div class="csec rv', 0, i)
    b = s.index('\n  </div>\n', i) + len('\n  </div>\n')
    return s[:a] + s[b:]


def fix_faq(s):
    m = re.search(r'(<section class="faqsec".*?<div class="faq">\n)(.*?)(  </div></section>)', s, re.S)
    items = re.findall(r'      <details>.*?</details>\n', m.group(2))
    keep = []
    for it in items:
        if FAQ_DROP.search(it):
            continue
        q = re.search(r'<summary>(.*?)</summary>', it).group(1)
        body = it[it.index('</summary>') + 10:it.rindex('</details>')]
        body = re.sub(r'<p>(.*?)</p>', lambda mm: '<p>%s</p>' % IN_GUIDE.sub('', mm.group(1)).strip(), body)
        keep.append(('      <details><summary>%s</summary>%s</details>\n' % (q, body), q, body))
    s = s[:m.start(2)] + ''.join(k[0] for k in keep) + s[m.end(2):]
    ld = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": re.sub('<[^>]+>', '', q),
                          "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', ' ', b).strip()}} for _, q, b in keep]}
    s = re.sub(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema.org",\s*"@type": "FAQPage".*?</script>',
               lambda _: '<script type="application/ld+json">\n%s\n</script>' % json.dumps(ld, ensure_ascii=False, indent=1), s, count=1, flags=re.S)
    return s


for name, cfg in PAGES.items():
    p = ROOT / name
    s = p.read_text(encoding='utf-8')
    if '<!--dbl-->' in s:
        print('skip', name); continue
    # Product schema out
    s, n = re.subn(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema.org",\s*"@type": "Product".*?</script>\n?', '', s, count=1, flags=re.S)
    assert n == 1, (name, 'product')
    # hero button
    if cfg['top']:
        old = '<a class="btn ghost" href="#guide">%s</a>' % cfg['top'][0]
        assert s.count(old) == 1, (name, 'top')
        s = s.replace(old, '<a class="btn ghost" href="#guide">%s</a>' % cfg['top'][1])
    # sales block -> promo (up to the testimonials)
    a = s.index('  <div class="guide-intro rv" id="guide">')
    b = s.index('  <h2 style="margin-top:34px">הורים מספרים</h2>')
    s = s[:a] + cfg['promo'] + s[b:]
    # testimonials: context, not the old product name
    s = s.replace('<small>%s</small>' % cfg['label'][0], '<small>%s</small>' % cfg['label'][1])
    s = re.sub(r'aria-label="הורים מספרים על [^"]*"', 'aria-label="הורים מספרים"', s)
    # "who is the guide for" belongs to the old product
    s = strip_csec(s, 'למי המדריך מתאים?')
    s = fix_faq(s)
    # buy box -> bottom CTA
    a = s.index('  <div class="cnext rv" id="buy">')
    b = s.index('  <div class="readmore rv">', a)
    s = s[:a] + cfg['bottom'] + s[b:]
    if name == 'siblings.html':
        i = s.index('<p>ההיריון מעלה שאלות על ההכנה.')
        a = s.rfind('  <div class="csec rv">', 0, i)
        b = s.index('\n  </div>\n', i) + len('\n  </div>\n')
        head = s[a:s.index('<p>', a)]
        head = re.sub(r'<h2>[^<]*</h2>', '<h2>ההכנה בהיריון היא רק תחילת הדרך</h2>', head)
        s = s[:a] + head + ''.join('<p>%s</p>\n' % x for x in SIB_BRIDGE_P) + '    <ul class="clist">\n%s    </ul>\n  </div>\n' % ''.join('      <li>%s</li>\n' % q for q in SIB_BRIDGE_Q) + s[b:]
    p.write_text(s, encoding='utf-8')
    print('patched', name)
