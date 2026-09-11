# -*- coding: utf-8 -*-
"""One-off campaign: שנה טובה מאמאל׳ה צמודים (ערב ראש השנה תשפ״ז, 11.9.2026).
v5: Shikma's own text (her AI draft, tone she chose) + conversion structure: one primary CTA button,
one secondary text link, community block kept, P.S. reply hook. Audience = mixed legacy list."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_emails import shell, h1, kicker, para, small, ul, btn, sig, divider, OUT
import build_emails
UTM = '?utm_source=mailerlite&utm_medium=email&utm_campaign=shana-tova-5787'
SITE = build_emails.SITE
WA_OPEN = 'https://chat.whatsapp.com/J6S6s2Di4u950qPno6nBLf'  # הקבוצה הפתוחה, שם מתנהל השיח

SUBJECT = 'שקמה כאן: שנה חדשה, בית חדש להורים לצמודים'
PREHEADER = 'חמישה דברים קטנים לסגור לפני ארוחת החג, ומקום אחד לכל הכלים להורות בדאבל.'

def ps(t): return '<p style="margin:18px 0 0;padding-top:14px;border-top:1px dashed #ECE2D2;font-family:Rubik,Arial,Helvetica,sans-serif;font-size:15px;line-height:1.75;color:#3A3128">%s</p>' % t
def signature():
    return ('<p style="margin:18px 0 0;font-family:\'Varela Round\',Rubik,Arial,Helvetica,sans-serif;font-size:18px;line-height:1.5;color:#3A3128">שקמה דגרי</p>'
            '<p style="margin:2px 0 0;font-family:Rubik,Arial,Helvetica,sans-serif;font-size:14px;color:#7C7062">הדרכת הורים לגיל הרך | התמחות בצמודים</p>')

body = ''.join([
    kicker('אמאל׳ה צמודים | ערב ראש השנה'),
    h1('שנה חדשה, בית חדש להורים לצמודים'),
    para('היי {$first_name|default(\'לכם\')},'),
    para('רגע לפני שהשנה החדשה מתחילה, רציתי לאחל לכם שנה של יותר ביטחון בהורות, פחות ניחושים והרבה רגעים טובים עם הילדים.'),
    para('השנה אני נכנסת לחג עם התחדשות גדולה משלי: אתר חדש שנבנה במיוחד להורים לצמודים.'),
    para('בחודשים האחרונים חזרו שוב ושוב אותן שאלות: למי ניגשים קודם כששניהם בוכים? איך מציבים גבול לאחד כשהשני כבר צריך אותנו? איך נותנים מקום לקנאה, לעייפות ולשני צרכים שונים שמגיעים בדיוק באותו הרגע?'),
    para('השאלות האלה הזכירו לי שוב שהורות בדאבל דורשת כלים אחרים. מה שעובד עם ילד אחד לא תמיד עובד כשיש בבית שני קטנטנים שעדיין זקוקים לנו מאוד, ולא תמיד לאותו הדבר.'),
    para('<strong>מתוך המציאות הזאת נולד imale.co, בית מקצועי להורים לצמודים.</strong> באתר מחכים לכם תכנים וכלים על טנטרומים והתפרצויות, גבולות, הצטרפות של אח חדש, שינה והקשר שנבנה בין האחים. תוכלו למצוא בו גם את המדריכים הדיגיטליים, הליווי האישי וכל הדרכים להצטרף לקהילת ״אמאל׳ה צמודים״. הכול במקום אחד, כדי שתוכלו להתחיל ממה שמעסיק אתכם בבית עכשיו.'),
    btn('להיכנס לבית החדש להורים לצמודים', SITE + UTM),
    divider(),
    h1('ורגע לפני שנכנסים לחג'),
    para('כמה דברים קטנים שכדאי לסגור מראש:'),
    ul([
        'ספרו לילדים מה צפוי לקרות, בשפה שמתאימה לגילם.',
        'החליטו על עוגן אחד מהבית שחשוב לכם לשמור, כמו טקס השינה המוכר.',
        'דאגו לאוכל לפני שהרעב והעייפות נפגשים.',
        'חלקו ביניכם תפקידים למקרה שילד אחד ירצה להישאר והשני כבר יהיה עייף או מוצף.',
        'בדקו מראש איפה תוכלו לקחת הפסקה קצרה מההמולה.',
    ]),
    para('לא צריך לתכנן חג מושלם שבו הילדים יישבו, יאכלו ויירדמו בדיוק בזמן. המטרה היא להגיע עם יותר בהירות: לדעת מה חשוב לכם לשמור, איפה אפשר להתגמש ומתי התוכנית כבר לא מתאימה לילדים. גם החלטה אחת שמקבלים לפני שמגיע רגע העומס יכולה להקל על הערב כולו.'),
    para('טיפים וכלים נוספים לחגים עם שני ילדים קטנים מחכים לכם באתר: <a href="%schag.html%s" style="color:#B4694E;font-weight:500">לקריאת התוכן לקראת החג</a>' % (SITE, UTM)),
    divider(),
    para('במיוחד ברגעים כמו ערבי חג צריך קהילה. היום הקהילה פתוחה לשיתופים בלייב: כל רגע מצחיק, מעצבן, או כזה שפשוט בא לכם לשתף, מהסוג שרק הורים לצמודים מבינים. כנראה יהיה מעניין 😉'),
    btn('לשתף בקהילה עכשיו', WA_OPEN, '#7A8B6F'),
    para('מאחלת לכם שנה טובה, חג שמח ושנה שבה תרגישו בטוחים יותר בהורות שלכם, גם ברגעים שבהם שניהם צריכים אתכם יחד.'),
    signature(),
    ps('נ.ב. אם תנסו הערב משהו אחד מהרשימה ותרצו לספר איך היה, פשוט השיבו למייל הזה. אני קוראת הכל, גם בחג.'),
])

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    html_out = shell(SUBJECT, body, PREHEADER)
    html_out = html_out.replace('href="%s"' % SITE, 'href="%s%s"' % (SITE, UTM))  # header/footer hrefs only
    open(os.path.join(OUT, 'shana-tova.html'), 'w', encoding='utf-8').write(html_out)
    open(os.path.join(OUT, 'shana-tova.subject.txt'), 'w', encoding='utf-8').write(SUBJECT + '\n' + PREHEADER + '\n')
    print('built', len(html_out), 'bytes')
