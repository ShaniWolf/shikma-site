# -*- coding: utf-8 -*-
"""עמוד המדריך ״הורות בדאבל״ — מדריך הדגל שכל האתר מוביל אליו.
טקסט: רק מה ששקמה כתבה על כריכת המדריך. מחיר: 149 ₪, מחיר השקה 99 ₪ (קישורי ישראכרט משקמה, 25.9.2026).
"""
from common import *

TITLE = 'הורות בדאבל | שקמה דגרי'
DESC = 'הורות בדאבל: השיטה שתעזור לך לדעת מה לעשות גם כששניהם צריכים אותך. שקמה דגרי, הדרכת הורים לגיל הרך | התמחות בצמודים.'
OG_T = 'הורות בדאבל'
PAY_LAUNCH = 'https://pay360.isracard.co.il/CustomerPayment/GenericURL?SaleId=a24de58f-78ab-2ecf-dc1d-6ff250428b75'   # 99 ₪
PAY_FULL = 'https://pay360.isracard.co.il/CustomerPayment/GenericURL?SaleId=6b5592a3-0bc0-0c74-0cf3-8144f0cda282'     # 149 ₪
LAUNCH = True   # False = חזרה למחיר המלא
PAY, PRICE = (PAY_LAUNCH, '99') if LAUNCH else (PAY_FULL, '149')

LINE1 = 'להבין מה כל ילד באמת צריך, לדעת למה להגיב קודם, לתת מענה לשניהם עם יותר בהירות ופחות ניחושים ואשמה.'
LINE2 = 'השיטה שתעזור לך לדעת מה לעשות גם כששניהם צריכים אותך.'

PROD = {"@context": "https://schema.org", "@type": "Product", "name": "הורות בדאבל", "description": LINE2 + ' ' + LINE1,
        "brand": {"@type": "Person", "name": "שקמה דגרי"}, "url": SITE + "double.html",
        "offers": {"@type": "Offer", "price": PRICE, "priceCurrency": "ILS", "availability": "https://schema.org/InStock", "url": SITE + "double.html#buy"}}

html = head(TITLE, DESC, 'double.html', ld=[PROD, crumbs_ld(('הורות בדאבל', SITE + 'double.html'))], og_title=OG_T, body_class='cpage')
html += header()
html += '<div class="wrap" id="main">\n' + crumb('הורות בדאבל')
html += '''
  <div class="hero">
    <div class="hero-cover">
      <div>
        <span class="kicker">שקמה דגרי · הדרכת הורים לגיל הרך | התמחות בצמודים</span>
        <h1>הורות בדאבל</h1>
        <p class="lead">%s</p>
        <p class="lead">%s</p>
        <p><a class="btn" href="#buy">אני רוצה את המדריך</a></p>
      </div>
      <div class="cv">%s</div>
    </div>
  </div>
''' % (LINE1, LINE2, polaroid('shk-sofa', 'שקמה על הספה בסלון עם יובל ותום', eager=True))
price = ('<s style="opacity:.55;font-size:.6em">149 ₪</s> 99 ₪' if LAUNCH else '149 ₪')
html += buy_box('״הורות בדאבל״', PRICE, PAY, 'אני רוצה את המדריך', LINE2).replace(
    '<span class="cprice">%s ₪</span>' % PRICE,
    '<span class="cprice">%s</span>%s' % (price, '\n    <p class="btn-note" style="margin-top:-8px">מחיר השקה</p>' if LAUNCH else ''))
html += bio_box()
html += '</div>\n' + footer() + CLICK_JS
write('double.html', html)
