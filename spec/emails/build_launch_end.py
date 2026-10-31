# -*- coding: utf-8 -*-
"""קמפיין חד-פעמי (שישי 31.10.2026). v4: הטקסט המלא של שקמה (שלחה לשני 31.10) מילה במילה, עם צילום ההמלצה assets/wa/dbl-a.jpg: מחיר ההשקה של ״הורות בדאבל״ מסתיים, הבלוג החדש, והמלצה.
נבנה על התבנית של שנה טובה (build_shana_tova.py). הטקסט על המדריך לקוח מ-double.html (האפיון של שקמה),
כותרות המאמרים הן של שקמה, וההמלצה היא הודעת הוואטסאפ מ-30.10 מילה במילה (בלי שורת הפתיחה ״היי שקמה, סליחה על השעה״).
שליחה לכל המנויות הפעילות (כמו שנה טובה). קישורים עם UTM: double-launch-end."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_emails import shell as _shell, OUT, polaroid
import build_emails, html as _html
F = "Rubik,Arial,Helvetica,sans-serif"
def para(x): return '<p style="margin:0 0 20px;font-family:%s;font-size:17px;line-height:1.9;color:#3A3128">%s</p>' % (F, x)
def h1(x): return '<h1 style="margin:0 0 18px;font-family:\'Varela Round\',%s;font-weight:400;font-size:25px;line-height:1.4;color:#3A3128">%s</h1>' % (F, x)
def h2(x): return '<h2 style="margin:0 0 14px;font-family:\'Varela Round\',%s;font-weight:400;font-size:21px;line-height:1.4;color:#3A3128">%s</h2>' % (F, x)
def kicker(x): return '<p style="margin:0 0 12px;font-family:%s;font-size:13px;letter-spacing:.06em;color:#B4694E;font-weight:500">%s</p>' % (F, x)
def divider(): return '<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin:30px 0"><tr><td style="border-top:1px dashed #ECE2D2;font-size:0;line-height:0">&nbsp;</td></tr></table>'
def ul(items):
    return '<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%%" style="margin:6px 0 22px">%s</table>' % ''.join(
        '<tr><td width="24" valign="top" style="padding:8px 0 8px 12px;font-family:Arial,sans-serif;font-size:16px;color:#B4694E">&#9679;</td>'
        '<td valign="top" style="padding:8px 0;font-family:%s;font-size:17px;line-height:1.8;color:#3A3128">%s</td></tr>' % (F, i) for i in items)
def btn(text, href, color='#B4694E'):
    return ('<table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center" class="btn" style="margin:26px auto 26px">'
            '<tr><td align="center" bgcolor="%s" style="border-radius:999px;background:%s">'
            '<a href="%s" target="_blank" style="display:inline-block;padding:16px 36px;font-family:%s;font-size:17px;font-weight:500;color:#ffffff;text-decoration:none;border-radius:999px">%s</a>'
            '</td></tr></table>') % (color, color, href, F, _html.escape(text))
def shell(title, body, preheader=''):
    out = _shell(title, body, preheader)
    return out.replace("@media (max-width:600px){ .wrap{width:100% !important} .card{padding:26px 20px !important} }",
        "@media (max-width:600px){ .wrap{width:100% !important} .card{padding:32px 22px !important} .btn{width:100% !important} .btn a{display:block !important;padding:17px 18px !important} h1{font-size:23px !important} p{font-size:17px !important} }")
def signature():
    return ('<p style="margin:26px 0 0;font-family:\'Varela Round\',Rubik,Arial,Helvetica,sans-serif;font-size:19px;line-height:1.5;color:#3A3128">שקמה דגרי</p>'
            '<p style="margin:4px 0 0;font-family:Rubik,Arial,Helvetica,sans-serif;font-size:14px;line-height:1.7;color:#7C7062">הדרכת הורים לגיל הרך | התמחות בצמודים</p>')
def ps(t): return '<p style="margin:30px 0 0;padding-top:22px;border-top:1px dashed #ECE2D2;font-family:%s;font-size:16px;line-height:1.85;color:#3A3128">%s</p>' % (F, t)
def small(t): return '<p style="margin:-10px 0 20px;text-align:center;font-family:%s;font-size:14px;line-height:1.7;color:#7C7062">%s</p>' % (F, t)

SITE = build_emails.SITE
UTM = '?utm_source=mailerlite&utm_medium=email&utm_campaign=double-launch-end'
DOUBLE = SITE + 'double.html' + UTM + '#buy'
def blog(u): return SITE + u + UTM
def link(u, t): return '<a href="%s" style="color:#3A3128;font-weight:500;text-decoration:underline;text-decoration-color:#B4694E">%s</a>' % (blog(u), t)

# ───────── גרסה 4 (31.10): הטקסט של שקמה מילה במילה, כולל הוראות העיצוב שלה בסוגריים ─────────
SUBJECT = 'אחד בוכה, השני רוצה שתשחקי איתו. למי ניגשים קודם?'
PREHEADER = 'היום בחצות מסתיים מחיר ההשקה של ״הורות בדאבל״. ושלושה מאמרים חדשים בבלוג.'

def big(x): return '<p style="margin:6px 0 20px;font-family:\'Varela Round\',%s;font-size:26px;line-height:1.4;color:#B4694E">%s</p>' % (F, x)
def h3(x): return '<p style="margin:0 0 10px;font-family:%s;font-size:14px;letter-spacing:.06em;color:#B4694E;font-weight:500">%s</p>' % (F, x)
def shot(src, alt):
    return ('<table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center" style="margin:6px auto 22px">'
            '<tr><td style="border-radius:16px;overflow:hidden;box-shadow:0 8px 22px rgba(58,49,40,.12)">'
            '<img src="%s" width="420" alt="%s" style="display:block;width:420px;max-width:100%%;height:auto;border:0;border-radius:16px">'
            '</td></tr></table>') % (src, _html.escape(alt))
def price():
    return ('<p style="margin:0 0 20px;font-family:%s;font-size:17px;line-height:1.9;color:#3A3128">עד אז תוכלי לרכוש את המדריך ב'
            '<span style="font-family:\'Varela Round\',%s;font-size:30px;color:#B4694E;font-weight:500">99 ₪</span> במקום '
            '<span style="text-decoration:line-through;color:#7C7062">149 ₪</span>.</p>') % (F, F)

POSTS = [
 ('kinaa-tzmudim.html', 'איך מפחיתים קנאה ותחרות בין צמודים מהרגע הראשון?',
  '5 עקרונות שיעזרו לך לחזק את הקשר ביניהם ולהפחית קנאה ותחרות.'),
 ('hitnahaguyot-tzmudim.html', 'התנהגויות אצל צמודים ואיך להגיב אליהן',
  '5 סיטואציות שחוזרות כמעט בכל בית עם צמודים, ומה אפשר לעשות בכל אחת מהן.'),
 ('maavarim-tzmudim.html', 'מעברים ופרידות אצל צמודים',
  'איך אפשר להקל על היציאה מהבית, הפרידה בגן ושינויים בשגרה.'),
]
def post_row(u, t, d):
    return ('<tr><td style="padding:0 0 16px">'
            '<p style="margin:0 0 4px;font-family:\'Varela Round\',%s;font-size:18px;line-height:1.5;color:#3A3128">%s</p>'
            '<p style="margin:0;font-family:%s;font-size:15px;line-height:1.75;color:#5B5146">%s</p>'
            '</td></tr>') % (F, link(u, t), F, d)

body = ''.join([
    para('היי {$first_name|default(\'\')} ❤️'),
    para('אחד בוכה כי אח שלו לקח לו צעצוע.<br>השני רוצה שתשחקי איתו.<br>ואת מנסה להבין למי לגשת קודם ומה לעשות כדי לעזור לשניהם.'),
    para('מוכר לך?'),
    para('גם אני מכירה את הרגעים האלה מהבית שלי.'),
    para('ועם הזמן הבנתי משהו חשוב: הורות לשני ילדים צמודים דורשת כלים אחרים.'),
    para('כי כששניהם צריכים אותך יחד, לא תמיד אפשר להגיב לכל אחד כמו שהיית מגיבה אם הוא היה לבד.'),
    para('צריך להבין מה כל אחד מהם צריך, ולדעת איך להגיב גם כששניהם בוכים, רבים או רוצים אותך באותו רגע.'),
    para('ובדיוק בשביל זה כתבתי את'),
    big('״הורות בדאבל״ ❤️'),
    para('מדריך שיעזור לך להבין מה עומד מאחורי ההתנהגויות של הילדים שלך, לדעת איך להגיב בסיטואציות שחוזרות אצלכם בבית ולהרגיש בטוחה יותר במה שאת עושה.'),
    para('תראי איזו הודעה מרגשת קיבלתי השבוע מאמא שרכשה את המדריך:'),
    shot(SITE + 'assets/wa/dbl-a.jpg', 'הודעת וואטסאפ: מהרגע שקניתי את המדריך דאבל אני שקועה בו ולא מצליחה להפסיק לקרוא. נופלים לי אסימונים. ממש תודה, זה מדריך מעולה'),
    para('התרגשתי לקרוא את זה, כי זה בדיוק מה שרציתי שהמדריך ייתן לך.'),
    para('לא עוד רשימה של טיפים שצריך לנסות לזכור, אלא הבנה של מה כל ילד צריך ואיך אפשר לעזור לו.'),
    divider(),
    h2('אם עדיין לא יצא לך להכיר, כתבתי לאחרונה גם כמה מאמרים בבלוג שיכולים לעזור לך:'),
    '<table role="presentation" width="100%%" cellspacing="0" cellpadding="0" border="0" style="margin:8px 0 6px">%s</table>' % ''.join(post_row(*p) for p in POSTS),
    btn('למאמרים בבלוג', blog('blog.html'), '#7A8B6F'),
    divider(),
    h3('ועוד משהו קטן לפני סיום:'),
    para('<strong>היום בחצות מסתיים מחיר ההשקה של ״הורות בדאבל״.</strong>'),
    price(),
    para('אם גם את רוצה להבין טוב יותר את הילדים שלך, לדעת איך להגיב כששניהם צריכים אותך ולהרגיש בטוחה יותר בהורות שלך, המדריך הזה בשבילך ❤️'),
    btn('להכיר את ״הורות בדאבל״', DOUBLE),
    para('מאחלת לך שבוע רגוע ❤️'),
    signature(),
    ps('נ.ב. אם יש לך שאלה על המדריך, את מוזמנת פשוט להשיב למייל הזה ואשמח לענות.'),
])

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    html_out = shell(SUBJECT, body, PREHEADER)
    html_out = html_out.replace('href="%s"' % SITE, 'href="%s%s"' % (SITE, UTM))
    open(os.path.join(OUT, 'double-launch-end.html'), 'w', encoding='utf-8').write(html_out)
    open(os.path.join(OUT, 'double-launch-end.subject.txt'), 'w', encoding='utf-8').write(SUBJECT + '\n' + PREHEADER + '\n')
    print('built', len(html_out), 'bytes')
