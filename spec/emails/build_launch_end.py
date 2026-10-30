# -*- coding: utf-8 -*-
"""קמפיין חד-פעמי (שישי 31.10.2026): מחיר ההשקה של ״הורות בדאבל״ מסתיים, הבלוג החדש, והמלצה.
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
def quote(text, who):
    """בועת וואטסאפ כמו ב״הורים מספרים״ באתר."""
    return ('<table role="presentation" width="100%%" cellspacing="0" cellpadding="0" border="0" style="margin:6px 0 26px">'
            '<tr><td bgcolor="#F6E9E1" style="background:#F6E9E1;border-radius:18px 18px 4px 18px;padding:18px 20px">'
            '<p style="margin:0 0 10px;font-family:%s;font-size:17px;line-height:1.85;color:#3A3128">%s</p>'
            '<p style="margin:0;font-family:%s;font-size:13px;color:#7C7062">%s</p>'
            '</td></tr></table>') % (F, text, F, who)
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

SUBJECT = 'עד מוצאי שבת: ״הורות בדאבל״ ב-99 ₪, ומה חדש באתר'
PREHEADER = 'מיום ראשון המדריך חוזר ל-149 ₪. ובינתיים: שישה מאמרים פתוחים לכולם בבלוג החדש.'

TESTIMONIAL = ('רק רציתי להגיד לך שמהרגע שקניתי את המדריך דאבל, אני שקועה בו ולא מצליחה להפסיק לקרוא.<br>'
               'נופלים לי אסימונים ואני ממש מרגישה שזה שינה לי את קו המחשבה על ההתנהגות שלי לבנים שלי וגם איך שהם מתנהגים אחד לשני.<br>'
               'ממש תודה זה מדריך מעולה ואני עדין לא סיימתי לקרוא ❤️')

POSTS = [
 ('kinaa-tzmudim.html', 'איך מפחיתים קנאה ותחרות בין צמודים מהרגע הראשון?'),
 ('visut-regashi.html', 'ויסות רגשי אצל ילדים: 5 דברים שאפשר ללמד כבר בגיל הרך'),
 ('bitachon-atzmi.html', 'איך מחזקים ביטחון עצמי אצל ילדים: 5 דברים להתחיל בגיל הרך'),
 ('tiyugim.html', '10 תיוגים שהורים נותנים לילדים שלהם ומה אפשר להגיד במקום'),
 ('hitnahaguyot-tzmudim.html', 'התנהגויות אצל צמודים ואיך להגיב אליהן'),
 ('maavarim-tzmudim.html', 'מעברים ופרידות אצל צמודים: מתי להתקדם ומתי לתת עוד זמן'),
]

body = ''.join([
    kicker('אמאל׳ה צמודים | עדכון קצר לפני סוף השבוע'),
    h1('מחיר ההשקה של ״הורות בדאבל״ מסתיים במוצאי שבת'),
    para('היי {$first_name|default(\'\')}'),
    para('לפני קצת יותר מחודש השקתי את ״הורות בדאבל״, המדריך המעשי לחיים עם שני ילדים קטנים, במחיר השקה של 99 ₪ במקום 149 ₪.'),
    para('<strong>מיום ראשון (2.11) המדריך חוזר למחירו המלא, 149 ₪.</strong> עד מוצאי שבת הוא עדיין ב-99 ₪.'),
    polaroid(SITE + 'assets/covers/double.png', 'כריכת המדריך הורות בדאבל', 150),
    para('אחד בוכה והשני קורא לכם. במקום לעמוד ביניהם ולא לדעת למי לגשת קודם, אתם יודעים מה לעשות עכשיו ואיך להראות גם לילד שמחכה שלא שכחתם אותו.'),
    para('״הורות בדאבל״ יעזור לכם להבין מה כל ילד באמת צריך ולדעת מה לעשות גם כשהכול קורה יחד, עם יותר בהירות ופחות ניחושים ואשמה.'),
    kicker('באילו רגעים המדריך יעזור לכם?'),
    ul(['כששניהם בוכים יחד ולא ברור למי לגשת קודם.',
        'כשהבכור זקוק לכם בדיוק בזמן האכלה או הרדמה של התינוק.',
        'כשצריך להציב גבול ואחד הילדים מתנגד.',
        'כשאתם לבד בערב וצריך לקלח, להאכיל ולהשכיב את שניהם.']),
    kicker('אמא שקראה את המדריך כתבה לי השבוע'),
    quote(TESTIMONIAL, 'אמא לשני בנים, מתוך הודעת וואטסאפ'),
    btn('אני רוצה את המדריך ב-99 ₪', DOUBLE),
    small('מדריך דיגיטלי בפרקים קצרים, שאפשר לעבור בהם ישר לנושא שהכי מעסיק אתכם. עד מוצאי שבת 99 ₪, מיום ראשון 149 ₪.'),
    divider(),
    h1('ומשהו חדש באתר: הבלוג'),
    para('העליתי לאתר שישה מאמרים שפתוחים לכולם, בלי להשאיר מייל. בכל אחד מהם מה קורה לילד, מה אפשר לעשות ומה אפשר להגיד ברגע עצמו:'),
    ul(['<a href="%s" style="color:#3A3128;text-decoration:underline;text-decoration-color:#B4694E">%s</a>' % (blog(u), t) for u, t in POSTS]),
    btn('לכל המאמרים בבלוג', blog('blog.html'), '#7A8B6F'),
    para('מאחלת לכם סוף שבוע רגוע, גם ברגעים שבהם שניהם צריכים אתכם יחד.'),
    signature(),
    ps('נ.ב. אם יש שאלה על מה שקורה אצלכם בבית, אפשר להשיב למייל הזה. אני קוראת הכל.'),
])

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    html_out = shell(SUBJECT, body, PREHEADER)
    html_out = html_out.replace('href="%s"' % SITE, 'href="%s%s"' % (SITE, UTM))
    open(os.path.join(OUT, 'double-launch-end.html'), 'w', encoding='utf-8').write(html_out)
    open(os.path.join(OUT, 'double-launch-end.subject.txt'), 'w', encoding='utf-8').write(SUBJECT + '\n' + PREHEADER + '\n')
    print('built', len(html_out), 'bytes')
