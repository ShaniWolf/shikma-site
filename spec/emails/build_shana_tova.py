# -*- coding: utf-8 -*-
"""One-off campaign: שנה טובה מאמאל׳ה צמודים (ערב ראש השנה תשפ״ז, 11.9.2026).
v5: Shikma's own text (her AI draft, tone she chose) + conversion structure: one primary CTA button,
one secondary text link, community block kept, P.S. reply hook. Audience = mixed legacy list."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_emails import shell as _shell, OUT
import build_emails, html as _html
F = "Rubik,Arial,Helvetica,sans-serif"
def para(x): return '<p style="margin:0 0 22px;font-family:%s;font-size:17px;line-height:1.9;color:#3A3128">%s</p>' % (F, x)
def h1(x): return '<h1 style="margin:0 0 20px;font-family:\'Varela Round\',%s;font-weight:400;font-size:25px;line-height:1.4;color:#3A3128">%s</h1>' % (F, x)
def kicker(x): return '<p style="margin:0 0 12px;font-family:%s;font-size:13px;letter-spacing:.06em;color:#B4694E;font-weight:500">%s</p>' % (F, x)
def divider(): return '<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin:30px 0"><tr><td style="border-top:1px dashed #ECE2D2;font-size:0;line-height:0">&nbsp;</td></tr></table>'
def ul(items):
    return '<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%%" style="margin:6px 0 24px">%s</table>' % ''.join(
        '<tr><td width="24" valign="top" style="padding:9px 0 9px 12px;font-family:Arial,sans-serif;font-size:16px;color:#B4694E">&#9679;</td>'
        '<td valign="top" style="padding:9px 0;font-family:%s;font-size:17px;line-height:1.8;color:#3A3128">%s</td></tr>' % (F, i) for i in items)
def btn(text, href, color='#B4694E'):
    return ('<table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center" class="btn" style="margin:30px auto 30px">'
            '<tr><td align="center" bgcolor="%s" style="border-radius:999px;background:%s">'
            '<a href="%s" target="_blank" style="display:inline-block;padding:16px 36px;font-family:%s;font-size:17px;font-weight:500;color:#ffffff;text-decoration:none;border-radius:999px">%s</a>'
            '</td></tr></table>') % (color, color, href, F, _html.escape(text))
def shell(title, body, preheader=''):
    out = _shell(title, body, preheader)
    return out.replace("@media (max-width:600px){ .wrap{width:100% !important} .card{padding:26px 20px !important} }",
        "@media (max-width:600px){ .wrap{width:100% !important} .card{padding:32px 22px !important} .btn{width:100% !important} .btn a{display:block !important;padding:17px 18px !important} h1{font-size:23px !important} p{font-size:17px !important} }")
UTM = '?utm_source=mailerlite&utm_medium=email&utm_campaign=shana-tova-5787'
SITE = build_emails.SITE
WA_OPEN = 'https://chat.whatsapp.com/J6S6s2Di4u950qPno6nBLf'  # הקבוצה הפתוחה, שם מתנהל השיח

SUBJECT = 'שקמה כאן: שנה חדשה, בית חדש להורים לצמודים'
PREHEADER = 'חמישה דברים קטנים לסגור לפני ארוחת החג, ומקום אחד לכל הכלים להורות בדאבל.'

def ps(t): return '<p style="margin:30px 0 0;padding-top:22px;border-top:1px dashed #ECE2D2;font-family:%s;font-size:16px;line-height:1.85;color:#3A3128">%s</p>' % (F, t)
def signature():
    return ('<p style="margin:26px 0 0;font-family:\'Varela Round\',Rubik,Arial,Helvetica,sans-serif;font-size:19px;line-height:1.5;color:#3A3128">שקמה דגרי</p>'
            '<p style="margin:4px 0 0;font-family:Rubik,Arial,Helvetica,sans-serif;font-size:14px;line-height:1.7;color:#7C7062">הדרכת הורים לגיל הרך | התמחות בצמודים</p>')

body = ''.join([
    kicker('אמאל׳ה צמודים | ערב ראש השנה'),
    h1('שנה חדשה, בית חדש להורים לצמודים'),
    para('היי {$first_name|default(\'\')}'),
    para('רגע לפני שהשנה החדשה מתחילה, רציתי לאחל לך שנה של יותר ביטחון בהורות, פחות ניחושים והרבה רגעים טובים עם הילדים.'),
    para('השנה אני נכנסת לחג עם התחדשות גדולה משלי: אתר חדש שנבנה במיוחד להורים לצמודים.'),
    para('בחודשים האחרונים חזרו שוב ושוב אותן שאלות: למי ניגשים קודם כששניהם בוכים? איך מציבים גבול לאחד כשהשני כבר צריך אותנו? איך נותנים מקום לקנאה, לעייפות ולשני צרכים שונים שמגיעים בדיוק באותו הרגע?'),
    para('השאלות האלה הזכירו לי שוב שהורות בדאבל דורשת כלים אחרים. מה שעובד עם ילד אחד לא תמיד עובד כשיש בבית שני קטנטנים שעדיין זקוקים לנו מאוד, ולא תמיד לאותו הדבר.'),
    para('<strong>מתוך המציאות הזאת נולד imale.co, בית מקצועי להורים לצמודים.</strong>'),
    para('באתר מחכים לך תכנים וכלים על טנטרומים והתפרצויות, גבולות, הצטרפות של אח חדש, שינה והקשר שנבנה בין האחים. אפשר למצוא בו גם את המדריכים הדיגיטליים, הליווי האישי וכל הדרכים להצטרף לקהילת ״אמאל׳ה צמודים״.'),
    para('הכול במקום אחד, כדי להתחיל ממה שמעסיק אותך בבית עכשיו.'),
    btn('להיכנס לבית החדש להורים לצמודים', SITE + UTM),
    divider(),
    h1('ורגע לפני שנכנסים לחג'),
    para('כמה דברים קטנים שכדאי לסגור מראש:'),
    ul([
        'לספר לילדים מה צפוי לקרות, בשפה שמתאימה לגילם.',
        'להחליט על עוגן אחד מהבית שחשוב לך לשמור, כמו טקס השינה המוכר.',
        'לדאוג לאוכל לפני שהרעב והעייפות נפגשים.',
        'לחלק תפקידים מראש עם מי שאיתך, למקרה שילד אחד ירצה להישאר והשני כבר יהיה עייף או מוצף.',
        'לבדוק מראש איפה אפשר לקחת הפסקה קצרה מההמולה.',
    ]),
    para('לא צריך לתכנן חג מושלם שבו הילדים יישבו, יאכלו ויירדמו בדיוק בזמן. המטרה היא להגיע עם יותר בהירות: לדעת מה חשוב לך לשמור, איפה אפשר להתגמש ומתי התוכנית כבר לא מתאימה לילדים.'),
    para('גם החלטה אחת שמקבלים לפני שמגיע רגע העומס יכולה להקל על הערב כולו.'),
    para('טיפים וכלים נוספים לחגים עם שני ילדים קטנים מחכים לך באתר: <a href="%schag.html%s" style="color:#B4694E;font-weight:500">לקריאת התוכן לקראת החג</a>' % (SITE, UTM)),
    divider(),
    para('במיוחד ברגעים כמו ערבי חג צריך קהילה. היום הקהילה פתוחה לשיתופים בלייב: כל רגע מצחיק, מעצבן, או כזה שפשוט בא לך לשתף, מהסוג שרק הורים לצמודים מבינים. כנראה יהיה מעניין 😉'),
    btn('לשתף בקהילה עכשיו', WA_OPEN, '#7A8B6F'),
    para('מאחלת לך חג שמח, ושנה שבה ההורות מרגישה בטוחה יותר, גם ברגעים שבהם שניהם צריכים אותך יחד.'),
    para('שנה טובה, {$first_name|default(\'ולהתראות באתר\')}.'),
    signature(),
    ps('נ.ב. אם משהו אחד מהרשימה נכנס הערב לשימוש ובא לך לספר איך היה, פשוט להשיב למייל הזה. אני קוראת הכל, גם בחג.'),
])

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    html_out = shell(SUBJECT, body, PREHEADER)
    html_out = html_out.replace('href="%s"' % SITE, 'href="%s%s"' % (SITE, UTM))  # header/footer hrefs only
    open(os.path.join(OUT, 'shana-tova.html'), 'w', encoding='utf-8').write(html_out)
    open(os.path.join(OUT, 'shana-tova.subject.txt'), 'w', encoding='utf-8').write(SUBJECT + '\n' + PREHEADER + '\n')
    print('built', len(html_out), 'bytes')
