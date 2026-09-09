# -*- coding: utf-8 -*-
"""Branded HTML emails for the MailerLite automations (paste into ML's custom HTML editor).
Design mirrors imale.co: cream paper, white card, clay button, sage accents, polaroid cover."""
import os, html
OUT = os.path.join(os.path.dirname(__file__), 'out')
SITE = 'https://imale.co/'
WA = 'https://chat.whatsapp.com/Fju9PGJPgFhL8h99M1mnX0'

def btn(text, href, color='#B4694E'):
    return ('<table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center" style="margin:22px auto 6px">'
            '<tr><td align="center" bgcolor="%s" style="border-radius:999px;background:%s">'
            '<a href="%s" target="_blank" style="display:inline-block;padding:14px 34px;font-family:Rubik,Arial,Helvetica,sans-serif;font-size:17px;font-weight:500;color:#ffffff;text-decoration:none;border-radius:999px">%s</a>'
            '</td></tr></table>') % (color, color, href, html.escape(text))

def polaroid(src, alt, w=150):
    return ('<table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center" style="margin:0 auto 18px">'
            '<tr><td bgcolor="#ffffff" style="background:#ffffff;padding:10px 10px 22px;border:1px solid #ECE2D2;box-shadow:0 8px 22px rgba(58,49,40,.10)">'
            '<img src="%s" width="%d" alt="%s" style="display:block;width:%dpx;max-width:100%%;height:auto;border:0">'
            '</td></tr></table>') % (src, w, html.escape(alt), w)

def para(t): return '<p style="margin:0 0 14px;font-family:Rubik,Arial,Helvetica,sans-serif;font-size:17px;line-height:1.8;color:#3A3128">%s</p>' % t
def small(t): return '<p style="margin:0 0 10px;font-family:Rubik,Arial,Helvetica,sans-serif;font-size:14px;line-height:1.7;color:#7C7062">%s</p>' % t
def h1(t): return '<h1 style="margin:0 0 14px;font-family:\'Varela Round\',Rubik,Arial,Helvetica,sans-serif;font-weight:400;font-size:26px;line-height:1.35;color:#3A3128">%s</h1>' % t
def kicker(t): return '<p style="margin:0 0 8px;font-family:Rubik,Arial,Helvetica,sans-serif;font-size:13px;letter-spacing:.06em;color:#B4694E;font-weight:500">%s</p>' % t
def ul(items):
    return '<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%%" style="margin:4px 0 14px">%s</table>' % ''.join(
        '<tr><td width="22" valign="top" style="padding:4px 0 4px 10px;font-family:Arial,sans-serif;font-size:17px;color:#B4694E">&#9679;</td>'
        '<td valign="top" style="padding:4px 0;font-family:Rubik,Arial,Helvetica,sans-serif;font-size:16px;line-height:1.75;color:#3A3128">%s</td></tr>' % i for i in items)
def sig(): return '<p style="margin:18px 0 0;font-family:\'Varela Round\',Rubik,Arial,Helvetica,sans-serif;font-size:18px;color:#3A3128">שקמה</p>'
def divider(): return '<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin:16px 0"><tr><td style="border-top:1px dashed #ECE2D2;font-size:0;line-height:0">&nbsp;</td></tr></table>'

def shell(title, body, preheader=''):
    return '''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="x-apple-disable-message-reformatting">
<title>%s</title>
<link href="https://fonts.googleapis.com/css2?family=Varela+Round&family=Rubik:wght@400;500&display=swap" rel="stylesheet">
<style>
  body{margin:0;padding:0;background:#FBF7F0}
  a{color:#B4694E}
  @media (max-width:600px){ .wrap{width:100%% !important} .card{padding:26px 20px !important} }
</style>
</head>
<body style="margin:0;padding:0;background:#FBF7F0" dir="rtl">
<div style="display:none;max-height:0;overflow:hidden;font-size:1px;line-height:1px;color:#FBF7F0">%s</div>
<table role="presentation" width="100%%" cellspacing="0" cellpadding="0" border="0" bgcolor="#FBF7F0" style="background:#FBF7F0">
<tr><td align="center" style="padding:28px 14px 36px">
  <table role="presentation" class="wrap" width="560" cellspacing="0" cellpadding="0" border="0" style="width:560px;max-width:100%%">
    <tr><td align="center" style="padding:0 0 18px">
      <a href="%s" target="_blank" style="text-decoration:none">
        <img src="%sassets/logo.jpg" width="56" height="56" alt="" style="display:block;margin:0 auto 8px;border-radius:50%%;border:0">
        <span style="font-family:'Varela Round',Rubik,Arial,Helvetica,sans-serif;font-size:19px;color:#B4694E">אמאל׳ה צמודים</span>
      </a>
    </td></tr>
    <tr><td class="card" bgcolor="#ffffff" style="background:#ffffff;border:1px solid #ECE2D2;border-radius:18px;padding:34px 36px;text-align:right" dir="rtl">
%s
    </td></tr>
    <tr><td align="center" style="padding:22px 12px 0">
      <p style="margin:0 0 6px;font-family:Rubik,Arial,Helvetica,sans-serif;font-size:13px;line-height:1.7;color:#7C7062">שקמה דגרי · הדרכת הורים לגיל הרך · <a href="%s" style="color:#7A8B6F;text-decoration:none">imale.co</a></p>
      <p style="margin:0;font-family:Rubik,Arial,Helvetica,sans-serif;font-size:12px;line-height:1.7;color:#A39A8E">קיבלתם את המייל הזה כי השארתם את הכתובת באתר. <a href="{$unsubscribe}" style="color:#A39A8E">להסרה מהרשימה</a></p>
    </td></tr>
  </table>
</td></tr>
</table>
</body>
</html>''' % (html.escape(title), html.escape(preheader), SITE, SITE, body, SITE)

EMAILS = {}

# ---------- A. delivery emails ----------
# תוכן לפי מוצר: מה יש במדריך ומאיפה מתחילים בו
DL = {"tantrums": "assets/d/39a91ab01572795b/kshehabait-full.pdf", "gvulot": "assets/d/2dd2e209919cf00f/gvulot-full.pdf", "together": "assets/d/8c9fed897b0aec07/ligdol-full.pdf"}

DELIVERY = {
    'tantrums': dict(
        name='כשהבית מתפוצץ',
        lead='המדריך בנוי לפי הרגעים עצמם: מה מצטבר לפני ההתפרצות, מה עושים ומה אומרים בזמנה, למי ניגשים קודם כששניהם צריכים אתכם, ואיך חוזרים לחיבור אחרי שזה עבר.',
        pre='מה עושים ומה אומרים ברגע עצמו, ולמי ניגשים קודם',
        start=['אם הייתה התפרצות היום, פתחו בפרק ״בזמן״. יש שם מה לעשות ומה לומר כשהילד כבר מוצף ולא מצליח לשמוע הסבר.',
               'המשפטים הקצרים שבמדריך נכתבו גם לרגעים שבהם לכם כבר נגמרו המילים. בחרו שניים ונסו אותם השבוע.',
               'הפרק ״כששניהם צריכים אתכם״ נותן סדר פעולות לרגע שאחד מתפרץ והשני מצטרף, כולל מה לומר לילד שמחכה.'],),
    'gvulot': dict(
        name='גבולות מתוך חיבור',
        lead='המדריך ממשיך מהניסוח של הגבול למה שקורה אחריו: כשהילד עונה ״לא״, כשהוא בוכה, וכשהאח השני מצטרף להתנגדות.',
        pre='מה קורה אחרי שאמרתם את הגבול, והילד עונה ״לא״',
        start=['התחילו במערכת הרמזור. היא עוזרת לבחור אילו גבולות באמת חשובים לכם עכשיו ואיפה אפשר להתגמש.',
               'הפרק על בחירות מראה איך לתת לילד להשפיע על הדרך בזמן שההחלטה נשארת אצלכם. שם יורדים חלק ממאבקי המקלחת והמסך.',
               'במדריך יש משפטים קצרים למצבים שחוזרים כל יום: כיבוי מסך, יציאה מהבית, שעת הערב. בחרו אחד להערב.'],),
    'together': dict(
        name='לגדול ביחד',
        lead='המדריך מלווה את כל המסלול: ההכנה בהיריון, השבועות הראשונים בבית, הקנאה והרגרסיות כשהתינוק גדל, והמריבות שמתחילות כשהם כבר משחקים יחד.',
        pre='מאיפה להתחיל, לפי השלב שאתם נמצאים בו עכשיו',
        start=['פתחו בשלב שאתם נמצאים בו עכשיו. אם התינוק כבר בבית, הפרק על השבועות הראשונים רלוונטי יותר מפרקי ההיריון.',
               'הפרק על שינויים בהתנהגות מסביר איך להסתכל על היצמדות, בכי וחזרה להתנהגויות קודמות אחרי הלידה, ומה עוזר בתגובה.',
               'לרגעים ששניהם צריכים אתכם באותו הזמן יש דרך לבחור למי לגשת קודם, ומה לומר לילד שנשאר לחכות.'],),
}

HI = "היי {$first_name|default('לכם')},"

def delivery_drive(key):
    d = DELIVERY[key]; name = d['name']
    subject = '״%s״ אצלכם, ומאיפה כדאי להתחיל' % name
    body = (kicker('ההזמנה התקבלה') + h1('״%s״ אצלכם' % name) +
        para('%s<br>תודה שבחרתם ב״%s״. %s' % (HI, name, d['lead'])) +
        btn('להורדת המדריך (PDF)', SITE + DL[key]) +
        divider() + kicker('מאיפה להתחיל') + ul(d['start']) + divider() +
        small('הקובץ שלכם לתמיד, והקישור לא פג. שווה לשמור את המייל הזה.') +
        para('ואם משהו לא מסתדר אצלכם בבית, השיבו למייל הזה. אני קוראת הכל.') + sig())
    return subject, shell(subject, body, d['pre'])

for key in ('tantrums', 'gvulot', 'together'):
    EMAILS['delivery-%s' % key] = delivery_drive(key)

# chagim: direct PDF
body = (kicker('ההזמנה התקבלה') + h1('״החגים עם צמודים״ אצלכם') +
    polaroid(SITE+'assets/covers/chagim.png', 'כריכת המדריך החגים עם צמודים') +
    para(HI + '<br>תודה שבחרתם ב״החגים עם צמודים״. אפשר לקרוא אותו תוך שעה: אילו עוגנים שומרים בחג, איפה מתגמשים, מה עושים כשילד אחד נהנה והשני כבר מוצף, ואיך עוברים את הנסיעות והארוחות.') +
    btn('להורדת המדריך (PDF)', SITE+'assets/d/d66ca34652049b85/chagim-full.pdf') +
    divider() + kicker('מאיפה להתחיל') +
    ul(['מלאו את דף ההיערכות לפני הארוחה הראשונה. שלוש החלטות מראש, כולל מי מההורים מרדים ומי נשאר, חוסכות את רוב ההתלבטויות בתוך החג.',
        'הפרק על שינה מחוץ לשגרה מראה אילו עוגנים שווה לקחת גם לבית אחר, ומתי עדיף לשחרר.',
        'בנק המשפטים נכתב גם לרגעים מול המשפחה, כשמישהו אומר ״תמשכו אותו עוד קצת״.']) +
    small('הקישור נשאר בתוקף גם אחרי החגים.') + sig())
EMAILS['delivery-chagim'] = ('״החגים עם צמודים״ אצלכם, ושלוש החלטות לפני הארוחה הראשונה', shell('החגים עם צמודים', body, 'שלוש החלטות שכדאי לקבל לפני הארוחה הראשונה'))

# ---------- B. magnet drip ----------
body = (kicker('המדריך אצלכם') + h1('״להכין את הלב״ מחכה לכם כאן') +
    polaroid(SITE+'assets/covers/lev.png', 'כריכת המדריך להכין את הלב') +
    para(HI + '<br>הנה ״להכין את הלב״. המדריך עוסק בצעד הראשון של ההכנה הרגשית לאח החדש: איך מדברים על התינוק בגיל הזה, ומה עוזר במפגש הראשון ביניהם.') +
    btn('לפתיחת המדריך', SITE+'assets/lev.pdf') + divider() +
    para('דבר אחד להתחיל ממנו עוד היום: בחרו רגע שקט ותנו לילד לשמוע מכם משפט אחד על התינוק שבדרך, בלי הסברים ארוכים. ״בעוד כמה שבועות יגיע תינוק קטן, ואת תהיי האחות הגדולה.״ זה מספיק לפעם הראשונה. איך ממשיכים משם, בפרק הראשון.') +
    small('אני שקמה דגרי, מדריכת הורים ויועצת שינה לגיל הרך ואמא לצמודים, יובל ותום, בהפרש של שנה וחודש. בימים הקרובים אשלח לכם עוד שני דברים קצרים: למה הבכור חוזר פתאום להתנהג כמו תינוק, ומה קורה בשבועות הראשונים אחרי שהתינוק כבר בבית.') + sig())
EMAILS['drip-1'] = ('״להכין את הלב״ אצלכם, ודבר אחד להתחיל ממנו היום', shell('להכין את הלב', body, 'הקישור למדריך בפנים, ודבר אחד להתחיל ממנו היום'))

body = (kicker('יום 2') + h1('למה הבכור מתחיל פתאום להתנהג כמו תינוק') +
    para(HI + '<br>הרבה הורים מספרים לי על אותה תמונה: התינוק מגיע, והבכור, שכבר ישן לבד ואכל לבד, מבקש בקבוק, בוכה בלילה, נצמד. זה מבלבל, ובדרך כלל זה גם מפחיד.') +
    para('מה שקורה שם מבפנים פשוט יותר ממה שזה נראה: הילד בודק אם המקום שלו אצלכם נשאר. ההתנהגות התינוקית היא שאלה, ״גם אותי עוד רואים?״, והתשובה עוברת דרך תגובות קטנות וחוזרות, יותר מאשר דרך שיחה אחת.') +
    kicker('מה שעוזר ברוב הבתים') +
    ul(['לתת שם לרגש במקום לתקן את ההתנהגות: ״רצית שגם אותך יחזיקו עכשיו.״',
        'עשר דקות ביום שהן רק שלו, גם כשהתינוק בוכה ברקע. קצר וקבוע שווה יותר משעה מזדמנת.',
        'לא לבקש ממנו להיות ״הגדול״ יותר ממה שהוא יכול. הוא עדיין פעוט.']) +
    para('ב״להכין את הלב״ יש על זה פרק שלם, עם דוגמאות ניסוח שמתאימות לגילים שונים.') + sig())
EMAILS['drip-2'] = ('למה הבכור מתחיל פתאום להתנהג כמו תינוק', shell('למה הבכור מתחיל פתאום להתנהג כמו תינוק', body, 'מה קורה לילד מבפנים, ושלושה דברים שעוזרים'))

body = (kicker('יום 5') + h1('ומה קורה אחרי שהתינוק כבר בבית?') +
    para(HI + '<br>״להכין את הלב״ עוזר לפני. השאלות הגדולות מגיעות אחרי: הקנאה שמתעוררת בשבועות הראשונים, הרגרסיות, המריבות שמתחילות כשהתינוק גדל ומתחיל לקחת צעצועים, וחלוקת הקשב כששניהם צריכים אתכם באותו רגע.') +
    para('בשביל השלב הזה כתבתי את ״לגדול ביחד״: המדריך המלא מההיריון ועד היחסים שנבנים בין האחים.') +
    ul(['הכנה מדויקת יותר לפי גיל הבכור', 'השבועות הראשונים בבית עם ניו-בורן ופעוט', 'תגובה לקנאה ולרגרסיות', 'כלים למריבות ולחלוקת קשב']) +
    btn('לפרטים על ״לגדול ביחד״', SITE+'siblings.html#guide') +
    small('המדריך הדיגיטלי המלא: 149 ש״ח. הגישה נפתחת לכתובת שתשאירו אחרי הרכישה.') + sig())
EMAILS['drip-3'] = ('ומה קורה אחרי שהתינוק כבר בבית?', shell('ומה קורה אחרי שהתינוק כבר בבית?', body, 'השלב שאחרי ההכנה, והמדריך שנכתב בשבילו'))

body = (kicker('יום 9') + h1('הרגע שבו יובל שאל אם תום חוזר לבית חולים') +
    polaroid(SITE+'assets/photos/shk-sofa-420.jpg', 'שקמה על הספה בסלון עם יובל ותום', 190) +
    para(HI + '<br>כמה שבועות אחרי שתום נולד, יובל שאל אותי בקול הכי רגיל בעולם אם התינוק חוזר עכשיו לבית חולים. בלי כעס. בסקרנות. ובאותו רגע הבנתי שכל ההכנה שעשינו לפני הלידה הייתה רק ההתחלה, והעבודה האמיתית מתחילה בשגרה: מי מקבל אותי כשאני חוזרת הביתה, מי יושב עליי בסיפור, מה קורה כששניהם בוכים ואני לבד.') +
    para('מהרגע הזה נולד ״לגדול ביחד״. הוא לא מבטיח שלא תהיה קנאה. הוא נותן לכם דרך להגיב אליה כך ששני הילדים ירגישו שרואים אותם, גם כשיש רק זוג ידיים אחד.') +
    btn('לפרטים על ״לגדול ביחד״', SITE+'siblings.html#guide') +
    para('ואם יש שאלה על מה שקורה אצלכם בבית, אפשר להשיב למייל הזה. אני קוראת הכל.') + sig())
EMAILS['drip-4'] = ('הרגע שבו יובל שאל אם תום חוזר לבית חולים', shell('הרגע שבו יובל שאל אם תום חוזר לבית חולים', body, 'סיפור מהבית שלי, ומה נולד ממנו'))

body = (kicker('יום 14') + h1('הורים לצמודים, יותר מ-300, וטיפ כל שבת') +
    para(HI + '<br>לסיום הסדרה, הזמנה למקום שבו רוב הדברים אצלי קורים: קהילת ההורים לצמודים בוואטסאפ. יותר מ-300 הורים, טיפ קצר כל שבת בערב, וחלון התייעצות בכתב כל יום רביעי בין 20:00 ל-22:00, שבו אפשר לשאול על מה שקורה אצלכם בבית ולקבל תשובה באותו ערב.') +
    para('בלי רעש ובלי הודעות מיותרות. רק מה שעוזר.') +
    btn('להצטרפות לקהילה', WA, '#7A8B6F') +
    small('נ.ב. כל המדריכים והתכנים הפתוחים מחכים ב<a href="%sguides.html" style="color:#B4694E">תוכן ומדריכים</a> באתר.' % SITE) + sig())
EMAILS['drip-5'] = ('הורים לצמודים, יותר מ-300, וטיפ כל שבת', shell('הזמנה לקהילה', body, 'ההזמנה לקהילה, טיפ כל שבת וחלון של רביעי'))

os.makedirs(OUT, exist_ok=True)
for k, (subject, h) in EMAILS.items():
    open(os.path.join(OUT, k + '.html'), 'w', encoding='utf-8').write(h)
    open(os.path.join(OUT, k + '.subject.txt'), 'w', encoding='utf-8').write(subject)
    print(k, '|', subject, '|', len(h))
