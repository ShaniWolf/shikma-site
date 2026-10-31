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

SUBJECT = '״גם אני!״, קנאה ומריבות על אותו צעצוע: מה אפשר להגיד ברגע עצמו'
PREHEADER = 'שישה מאמרים קצרים, פתוחים לכולם. ומשהו קטן לפני יום ראשון.'

def wa(text, time):
    """הודעת וואטסאפ כמו המקור: רקע צ׳אט, בועה לבנה, שעה וסימון ✓✓."""
    return ('<table role="presentation" width="100%%" cellspacing="0" cellpadding="0" border="0" style="margin:6px 0 26px">'
            '<tr><td bgcolor="#E5DDD5" style="background:#E5DDD5;border-radius:14px;padding:16px 14px 14px">'
            '<table role="presentation" width="100%%" cellspacing="0" cellpadding="0" border="0"><tr>'
            '<td width="8%%"></td>'
            '<td bgcolor="#ffffff" style="background:#ffffff;border-radius:12px 2px 12px 12px;padding:10px 14px 8px;box-shadow:0 1px 1px rgba(0,0,0,.08)" dir="rtl">'
            '<p style="margin:0 0 6px;font-family:%s;font-size:16px;line-height:1.7;color:#111b21">%s</p>'
            '<p style="margin:0;text-align:left;font-family:%s;font-size:11px;color:#667781">%s <span style="color:#53bdeb">&#10003;&#10003;</span></p>'
            '</td></tr></table></td></tr></table>') % (F, text, F, time)

TESTIMONIAL = ('היי שקמה, סליחה על השעה<br>'
               'רק רציתי להגיד לך שמהרגע שקניתי את המדריך דאבל, אני שקועה בו ולא מצליחה להפסיק לקרוא 🥱<br>'
               'נופלים לי אסימונים ואני ממש מרגישה שזה שינה לי את קו המחשבה על ההתנהגות שלי לבנים שלי וגם איך שהם מתנהגים אחד לשני<br>'
               'ממש תודה זה מדריך מעולה ואני עדין לא סיימתי לקרוא ❤️😅')

POSTS = [
 ('kinaa-tzmudim.html', 'איך מפחיתים קנאה ותחרות בין צמודים מהרגע הראשון?',
  'קנאה מתחילה הרבה לפני הריב הראשון על צעצוע. חמישה עקרונות שבונים את הבסיס לקשר טוב ביניהם.'),
 ('visut-regashi.html', 'ויסות רגשי: 5 דברים שאפשר ללמד כבר בגיל הרך',
  'איך עוזרים לילדים להגיד מה הם מרגישים במקום לצעוק, להרביץ או להיסגר, ולשמוע ״לא״ בלי להתפרק.'),
 ('bitachon-atzmi.html', 'איך מחזקים ביטחון עצמי בגיל הרך',
  'איך עוזרים לילדים להגיד מה הם רוצים, לא לוותר רק כדי שיהיה שקט, ולבקש עזרה כשקשה להם.'),
 ('tiyugim.html', '10 תיוגים שאנחנו נותנים לילדים, ומה אפשר להגיד במקום',
  '״עקשן״, ״דרמטית״, ״לא מקשיב״. עשרה משפטים שיוצאים לנו כמעט בלי לשים לב.'),
 ('hitnahaguyot-tzmudim.html', 'התנהגויות אצל צמודים ואיך להגיב אליהן',
  'חמש סיטואציות שחוזרות כמעט בכל בית עם צמודים, ובכל אחת מה לעשות ומה אפשר להגיד.'),
 ('maavarim-tzmudim.html', 'מעברים ופרידות אצל צמודים',
  'פרידה ממוצץ, מעבר חדר או כניסה לגן: מתי לחכות בין שינויים, איך מכינים אותם, ולמה בודקים כל אחד בנפרד.'),
]

def post_row(u, t, d):
    return ('<tr><td style="padding:0 0 18px">'
            '<p style="margin:0 0 4px;font-family:\'Varela Round\',%s;font-size:18px;line-height:1.5;color:#3A3128">%s</p>'
            '<p style="margin:0;font-family:%s;font-size:15px;line-height:1.75;color:#5B5146">%s</p>'
            '</td></tr>') % (F, link(u, t), F, d)

body = ''.join([
    kicker('אמאל׳ה צמודים'),
    h1('״גם אני!״, קנאה ומריבות על אותו צעצוע: מה אפשר להגיד ברגע עצמו'),
    para('היי {$first_name|default(\'\')}'),
    para('אני יודעת כמה הימים האלה מלאים, אז בקצרה: בשבועות האחרונים כתבתי שישה מאמרים קצרים על הרגעים שחוזרים כמעט בכל בית עם ילדים קטנים. הם בבלוג החדש באתר, פתוחים לכולם. בכל אחד מהם מה קורה לילדים ברגע הזה, מה אפשר לעשות ומה אפשר להגיד.'),
    '<table role="presentation" width="100%%" cellspacing="0" cellpadding="0" border="0" style="margin:8px 0 6px">%s</table>' % ''.join(post_row(*p) for p in POSTS),
    btn('לבלוג', blog('blog.html'), '#7A8B6F'),
    divider(),
    h2('וכששניהם צריכים אתכם בבת אחת'),
    para('המאמרים עוזרים להבין מה קורה ומה אפשר להגיד. אבל רובנו לא מתמודדים עם ילד אחד בכל פעם. אחד בוכה והשני קורא לכם, ובסוף היום נשארת השאלה אם הספקתם לתת מספיק לכל אחד. אני מכירה את זה מהבית שלי.'),
    para('בשביל הרגעים האלה כתבתי את ״הורות בדאבל״: להבין מה כל אחד מהם צריך, ולדעת מה לעשות גם כשהכול קורה יחד.'),
    kicker('הודעה שקיבלתי השבוע'),
    wa(TESTIMONIAL, '22:40'),
    para('ומשהו שחשוב לי שתדעו: מחיר ההשקה, 99 ₪ במקום 149 ₪, מסתיים במוצאי שבת. מיום ראשון המדריך חוזר למחיר המלא. אם חשבתם עליו, זה זמן טוב להחליט.'),
    btn('למדריך ״הורות בדאבל״', DOUBLE),
    small('עד מוצאי שבת 99 ₪, אחר כך 149 ₪.'),
    para('שיהיה לכם סוף שבוע רגוע.'),
    signature(),
    ps('נ.ב. יש שאלה? פשוט השיבו למייל הזה.'),
])

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    html_out = shell(SUBJECT, body, PREHEADER)
    html_out = html_out.replace('href="%s"' % SITE, 'href="%s%s"' % (SITE, UTM))
    open(os.path.join(OUT, 'double-launch-end.html'), 'w', encoding='utf-8').write(html_out)
    open(os.path.join(OUT, 'double-launch-end.subject.txt'), 'w', encoding='utf-8').write(SUBJECT + '\n' + PREHEADER + '\n')
    print('built', len(html_out), 'bytes')
