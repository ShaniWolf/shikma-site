"""כיפור: מאמר (kippur.html) + עמוד הורדה לדף ההיערכות (thanks-kippur.html).
הטקסט של המאמר = הטקסט של שקמה מהמסמך, מילה במילה. השלד (head/header/footer) נלקח מ-chag.html.
"""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = (ROOT / 'chag.html').read_text(encoding='utf-8')

PDF = 'assets/d/699e8b5a37ac1316/kippur-mi-ose-ma.pdf'
FORM_EP = 'https://assets.mailerlite.com/jsonp/2618157/forms/198613248576062729/subscribe'
CHAGIM_PAY = 'https://pay360.isracard.co.il/CustomerPayment/GenericURL?SaleId=4bc33c76-8f0d-c8d0-6faa-5de4d97472ad'
COMMUNITY = 'https://chat.whatsapp.com/Fju9PGJPgFhL8h99M1mnX0'

head_start = SRC.index('<head>')
head_end = SRC.index('<script type="application/ld+json">')
header = SRC[SRC.index('<a class="skip"'):SRC.index('<div class="wrap" id="main">')]
footer = SRC[SRC.index('<footer>'):SRC.index('</footer>') + len('</footer>')]
tracker = SRC[SRC.index('<script>\ndocument.addEventListener'):SRC.index('</body>')]
tracker = tracker.replace("} else if(h.indexOf('lev.html') > -1){\n    gtag('event', 'click_magnet', {page_path: location.pathname});",
                          "} else if(h.indexOf('kippur-mi-ose-ma.pdf') > -1){\n    gtag('event', 'guide_download', {guide: 'kippur', page_path: location.pathname});")


def head(title, desc, url, noindex=False, ld=''):
    h = SRC[head_start:head_end]
    old_title = re.search(r'<title>(.*?)</title>', h).group(1)
    old_desc = re.search(r'<meta name="description" content="(.*?)">', h).group(1)
    h = h.replace(old_title, title).replace(old_desc, desc).replace('https://imale.co/chag.html', url)
    if noindex:
        h = h.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex">')
    return h + ld + '</head>\n'


def form(idp, btn):
    return f'''<form class="mform" id="{idp}" novalidate>
      <label for="{idp}-name">איך לפנות אליכם? (לא חובה)</label>
      <input type="text" id="{idp}-name" name="name" autocomplete="given-name" placeholder="שם פרטי">
      <label for="{idp}-email">כתובת מייל</label>
      <input type="email" id="{idp}-email" name="email" autocomplete="email" required placeholder="name@example.com">
      <button type="submit">{btn}</button>
      <p class="err" role="alert"></p>
      <p class="consent">הדף מגיע מיד לעמוד ההורדה ולמייל. אשלח גם תכנים וכלים להורים לצמודים מדי פעם, ואפשר להסיר את הכתובת בלחיצה אחת בכל הודעה. פרטים ב<a href="privacy.html">מדיניות הפרטיות</a>.</p>
    </form>'''


FORM_JS = '''<script>
document.querySelectorAll('form.mform[data-kippur]').forEach(function(f){
  var btn=f.querySelector('button'), err=f.querySelector('.err'), label=btn.textContent;
  f.addEventListener('submit', function(e){
    e.preventDefault();
    var email=f.querySelector('input[type=email]').value.trim();
    var nameEl=f.querySelector('input[type=text]'), name=nameEl?nameEl.value.trim():'';
    if(!email || email.indexOf('@')<1 || email.indexOf('.')<0){ err.textContent='צריך כתובת מייל תקינה כדי לשלוח את הדף'; return; }
    err.textContent=''; btn.disabled=true; btn.textContent='רגע, שולחת...';
    var done=false;
    function finish(){
      if(done) return; done=true;
      if(typeof gtag==='function'){ gtag('event','magnet_signup',{magnet:'kippur',page_path:location.pathname}); }
      location.href='thanks-kippur.html';
    }
    var body='fields%5Bemail%5D='+encodeURIComponent(email)+(name?'&fields%5Bname%5D='+encodeURIComponent(name)+'&fields%5Bfirst_name%5D='+encodeURIComponent(name.split(' ')[0]):'')+'&ml-submit=1&anticsrf=true';
    fetch('EP',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:body}).then(finish).catch(finish);
    setTimeout(finish, 6000);
  });
});
</script>
'''.replace("'EP'", "'" + FORM_EP + "'")

ARTICLE_LD = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "יום כיפור עם צמודים: 5 דברים שכדאי לסגור מראש",
  "author": {"@type": "Person", "name": "שקמה דגרי", "url": "https://imale.co"},
  "datePublished": "2026-09-15",
  "inLanguage": "he"
}
</script>
'''

P = lambda *lines: '\n'.join(f'  <p>{l}</p>' for l in lines)

article = f'''<!DOCTYPE html>
<html lang="he" dir="rtl">
{head("יום כיפור עם צמודים: 5 דברים שכדאי לסגור מראש",
      "יום כיפור עם שני ילדים קטנים: איך מחלקים תפקידים כשאחד צם, מה מכינים לאכול, איך יוצאים לרחוב וחוזרים, ומה עושים כשכל ילד צריך משהו אחר. מאת שקמה דגרי, מדריכת הורים לצמודים.",
      "https://imale.co/kippur.html", ld=ARTICLE_LD)}<body class="sales">

{header}<div class="wrap" id="main">
  <div class="crumb"><a href="index.html">בית</a> › יום כיפור עם צמודים</div>

  <div class="hero">
    <div class="hero-cover">
      <div>
        <h1>יום כיפור עם צמודים: 5 דברים שכדאי לסגור מראש</h1>
        <p class="lead">יום כיפור אולי שקט בחוץ, אבל בבית עם צמודים הוא לא בהכרח יום שקט.</p>
        <p><a class="btn green" href="#daf">לדף ההיערכות: מי עושה מה ביום כיפור?</a></p>
      </div>
      <div class="cv"><div class="polaroid tall"><img src="assets/covers/kippur.png" alt="דף ההיערכות מי עושה מה ביום כיפור" width="220" height="311"></div></div>
    </div>
  </div>

{P("הרחובות שקטים, אין מסגרות והקצב בחוץ משתנה. אבל שני הילדים מתעוררים בבוקר עם אותם הצרכים: לאכול, לזוז, לשחק ולקבל מענה.",
   "יכול להיות ששניכם צמים, שרק אחד מכם צם או שאינכם צמים.<br>יכול להיות שתכננתם לצאת עם הילדים לרכוב, אבל אחד מהם כבר עייף והשני רק רוצה להמשיך.<br>ובתוך היום הארוך צריך לדאוג לארוחות, לשמור על עוגנים מהשגרה וגם למצוא רגע לנוח.",
   "ואז אתם עלולים למצוא את עצמכם נקרעים שוב ושוב בין שני צרכים - אם יוצאים לרחוב, אחד רוצה להמשיך והשני כבר מבקש ידיים. אם חוזרים הביתה, אחד זקוק למנוחה והשני משתעמם. ואם אחד ההורים מנסה לנוח, ההורה השני נשאר לבד עם שניהם.",
   "כל בחירה יכולה להרגיש כאילו היא באה על חשבון ילד אחר. אתם ממשיכים להגיב למה שקורה, לנחש מה יעזור ולקוות שהרגע הבא יהיה קל יותר.",
   "הקושי הוא לא שאין לכם תוכנית מושלמת.<br>הקושי הוא להעביר יום שלם בתחושה שאתם רק מכבים שריפות, ולסיים אותו עייפים עם המחשבה שאולי הייתם צריכים לפעול אחרת.",
   "כמה החלטות קטנות שתקבלו מראש יכולות לשנות את התחושה בתוך היום הזה.<br>לא מפני שהכול יתנהל כמתוכנן, אלא כי ככל שיש לכם יותר בהירות לגבי מה לעשות, יש בבית פחות צעקות, פחות ניחושים ופחות אשמה בסוף היום.")}

  <h2>1. החליטו איך תרצו שהיום ייראה</h2>
{P("לפני שמחלקים תפקידים או מתכננים פעילויות, התחילו מהתמונה הגדולה.",
   "האם תרצו להישאר בעיקר בבית? לצאת לרחוב בשעות מסוימות? לפגוש משפחה או חברים? האם חשוב לכם לשמור על זמני השינה או שהפעם מתאים להתגמש?",
   "אין דרך אחת נכונה לציין את יום כיפור עם ילדים. התוכנית צריכה להתאים לאופן שבו אתם מציינים את היום, לגיל הילדים ולכוחות שיהיו לכם.",
   "בחרו עוגן אחד או שניים שחשוב לכם לשמור עליהם. למשל: שנת הצהריים, ארוחה בשעה מוכרת או טקס השינה מהבית.",
   "לא חייבים לשמור על כל השגרה כדי לתת לילדים יציבות. עוגן אחד או שניים יכולים לעזור להם בתוך יום שנראה אחרת.")}

  <h2>2. חלקו תפקידים לפי המציאות שלכם</h2>
{P("בין אם שניכם צמים, רק אחד מכם צם או שאינכם צמים, כדאי לדבר מראש על חלוקת היום.",
   "בדקו מי צפוי להזדקק ליותר מנוחה, מי מוביל עם הילדים בכל חלק ביום ואיך מתחלפים כשהכוחות מתחילים להיגמר.",
   "אם שניכם צמים, אפשר לחלק את היום למשמרות קצרות כדי שכל אחד יקבל זמן לנוח. אם רק אחד מכם צם, חשוב לחשוב גם על הכוחות של ההורה שאינו צם ולא להשאיר אותו לבד עם האחריות לשני הילדים במשך כל היום.",
   "לא צריך לחלק הכול באופן שווה.<br>צריך למצוא חלוקה שמתאימה ליכולת של כל אחד מכם באותו היום.",
   "כדאי להתייחס גם לרגע שבו הילדים צריכים דברים שונים - מי יוצא עם הילד שזקוק לתנועה ומי נשאר עם הילד העייף? מי עוזר בהרדמה ומי נמצא עם הילד שעדיין ער?",
   "המטרה אינה לנהל לוח משמרות מדויק. המטרה היא למנוע את הרגע שבו שניכם כבר מותשים, שני הילדים זקוקים לכם ואף אחד לא יודע מי עושה מה.")}

  <div class="cnext rv" id="daf">
    <h2>מי עושה מה ביום כיפור?</h2>
    <p>דף היערכות קצר להורים לצמודים. חמש דקות של תיאום מראש יכולות למנוע את הרגע שבו שניכם כבר עייפים, שני הילדים צריכים אתכם ואף אחד לא יודע מה עושים עכשיו.</p>
    {form('kf1', 'שלחו לי את דף ההיערכות').replace('<form class="mform"', '<form class="mform" data-kippur')}
  </div>

  <h2>3. הכינו לילדים אוכל שקל להגיש</h2>
{P("רוב המשפחות ממילא נערכות מראש לאוכל ביום כיפור, במיוחד כאשר צמים או נמנעים מבישול ומהדלקת חשמל.",
   "עם שני ילדים קטנים, כדאי לחשוב לא רק מה הם יאכלו אלא גם כמה פשוט יהיה להגיש להם את האוכל ברגע האמת.",
   "הכינו מראש ארוחות ונשנושים שלא ידרשו מכם להתחיל לחפש, לחתוך או לבשל כשהכוחות אוזלים. סדרו אותם כך שיהיה ברור מה מיועד לכל חלק ביום, ודאגו לקחת מים ואוכל בכל יציאה מהבית.",
   "הרעב של הילדים לא תמיד יגיע בשעה שתכננתם. אוכל נגיש יכול למנוע את המפגש המוכר בין רעב, עייפות ושני ילדים שצריכים אתכם יחד.")}

  <h2>4. תכננו את היציאה לרחוב וגם את הדרך חזרה</h2>
{P("הרחוב הריק הוא אחד הדברים הסמלים ביום כיפור שילדים רבים מחכים להם. אבל כביש שנראה ריק אינו בהכרח כביש פנוי או בטוח.",
   "לצד כלי רכב ורכבי חירום, נמצאים עליו גם אופניים, קורקינטים וכלים חשמליים שנעים במהירות. לילדים קטנים לא תמיד קל להעריך מאיזה כיוון הם מגיעים או באיזו מהירות.",
   "בחרו מסלול קרוב לבית, התאימו את כלי הרכיבה לגיל הילדים, הקפידו על קסדה והשגחה וקחו איתכם מים ואוכל עבורם.",
   "חשבו גם על הדרך חזרה - יציאה קצרה יכולה להסתיים כשאחד הילדים רוצה להמשיך לרכוב והשני כבר עייף, מבקש ידיים או אינו מסוגל ללכת.",
   "לפני שיוצאים, החליטו כמה רחוק מתאים לכם להגיע ומה תעשו אם אחד הילדים ירצה לחזור לפני השני.",
   "המטרה אינה לצפות כל תרחיש, אלא לא למצוא את עצמכם רחוקים מהבית, עם ילד אחד על הידיים וילד שני שמסרב לסיים.")}

  <h2>5. החליטו מה עושים כשהם צריכים דברים שונים</h2>
{P("אחד הילדים יכול ליהנות מהרכיבה ומהמפגש ברחוב, בזמן שהשני כבר זקוק לבית ולמנוחה. אחד ירצה להמשיך לשחק, והשני יצטרך אתכם קרובים דווקא באותו הרגע.",
   "שוויון לא אומר ששני הילדים צריכים לעשות את אותו הדבר. הוא אומר שמנסים להבין מה כל אחד מהם צריך בתוך אותה הסיטואציה.",
   "אפשר להתפצל לזמן קצר, אם זה מתאים לכם. אפשר לקחת הפסקה ולבדוק אם הילד מסוגל לחזור. ואפשר גם להבין שהספיק להיום ולשנות את התוכנית.",
   "כדאי להחליט מראש מה יהיה הסימן שלכם לעצור:")}
  <ul>
    <li>כשאחד הילדים כבר אינו מצליח ליהנות.</li>
    <li>כשאתם משקיעים את כל הכוחות בניסיון להחזיק עוד קצת.</li>
    <li>כשהיציאה כבר גובה מכולם יותר ממה שהיא נותנת.</li>
  </ul>
{P("לשנות את התוכנית לא אומר שנכשלתם.<br>זה אומר שזיהיתם מה המשפחה שלכם צריכה ובחרתם בהתאם.",
   "יום כיפור עם צמודים לא חייב להתנהל בדיוק כפי שתכננתם כדי להרגיש אחרת.",
   "הילדים עדיין עשויים להתעייף בזמנים שונים. אחד ירצה לצאת כשהשני ירצה להישאר. יהיו רגעים שבהם שניהם יצטרכו אתכם יחד.",
   "ההבדל הוא שלא תצטרכו להתחיל לנחש בכל פעם מחדש.",
   "כשתדעו על אילו עוגנים חשוב לכם לשמור, איך להתחלק ומה לעשות כשהתוכנית כבר לא מתאימה, תוכלו להגיב מתוך יותר בהירות ופחות מתוך הלחץ של הרגע.")}

  <div class="pricebox">
    <div class="terms" style="font-size:1rem;color:var(--ink)">בדיוק בשביל הרגעים האלה יצרתי את המדריך הדיגיטלי ״חגים עם צמודים״.</div>
    <div class="terms">זהו מדריך קצר ומעשי שיעזור לכם להתכונן לשינויים בשינה ובשגרה, לחלק תפקידים, להציב גבולות גם מחוץ לבית ולהגיב כשכל ילד צריך משהו אחר.<br>במדריך מחכים לכם גם דף היערכות ובנק משפטים שאפשר לחזור אליהם לפני החג וברגע האמת.<br>המטרה אינה להוסיף לכם עוד משימה. אפשר לקרוא את המדריך תוך פחות משעה, לבחור מתוכו את מה שמתאים למשפחה שלכם ולהגיע לחגים עם פחות אלתורים ויותר בהירות.</div>
    <a class="btn" href="chagim.html">אני רוצה שנגיע לחגים מוכנים יותר</a>
  </div>
</div>

{footer}

{tracker}{FORM_JS}</body>
</html>
'''
(ROOT / 'kippur.html').write_text(article, encoding='utf-8')

thanks = f'''<!DOCTYPE html>
<html lang="he" dir="rtl">
{head("מי עושה מה ביום כיפור? דף ההיערכות שלכם",
      "דף היערכות קצר להורים לצמודים לקראת יום כיפור.",
      "https://imale.co/thanks-kippur.html", noindex=True)}<body class="sales">

{header}<div class="wrap" id="main">
  <div class="hero">
    <div class="hero-cover">
      <div>
        <h1>מי עושה מה ביום כיפור?</h1>
        <p class="lead">אין צורך למלא כל שורה. בחרו רק את ההחלטות שיכולות להקל על המשפחה שלכם.</p>
        <p><a class="btn" href="{PDF}" download="מי עושה מה ביום כיפור - שקמה דגרי.pdf">להורדת דף ההיערכות (PDF)</a></p>
      </div>
      <div class="cv"><div class="polaroid tall"><img src="assets/covers/kippur.png" alt="דף ההיערכות מי עושה מה ביום כיפור" width="220" height="311"></div></div>
    </div>
  </div>

  <div class="pain">
    <h3>מאיפה להתחיל</h3>
    <p>מהעמוד האחרון: ״גם אם לא תמלאו שום דבר אחר, איזו החלטה אחת תרצו לקבל מראש?״. משם ממשיכים לחלוקה של בוקר, צהריים, אחר הצהריים וערב, ולסימן שלכם לשנות את התוכנית.</p>
  </div>

  <div class="pricebox">
    <div class="price" style="font-size:1.5rem">רוצים להגיע גם לשאר החגים עם פחות אלתורים ויותר בהירות?</div>
    <div class="terms">במדריך ״חגים עם צמודים״ מחכים לכם כלים נוספים לשינה, גבולות, חלוקת תפקידים והרגע שבו כל ילד צריך משהו אחר.</div>
    <div class="price">36₪</div>
    <a class="btn" href="{CHAGIM_PAY}">להזמנת המדריך</a>
    <p class="btn-note">מדריך דיגיטלי, יורד מיד אחרי התשלום</p>
  </div>

  <div class="cnext rv">
    <h2>רוצים עוד ליווי בדרך, ללא עלות?</h2>
    <p>בקהילת ״אמאל׳ה צמודים״ בוואטסאפ אני עונה בעצמי לשאלות של הורים לצמודים, ותוכלו לפגוש עוד הורים שמבינים בדיוק מה עובר עליכם.</p>
    <a class="btn green" href="{COMMUNITY}" target="_blank" rel="noopener">להצטרפות לקהילה</a>
  </div>

  <p class="btn-note" style="text-align:center">רוצים לקרוא שוב את חמשת הדברים? <a href="kippur.html">יום כיפור עם צמודים: 5 דברים שכדאי לסגור מראש</a></p>
</div>

{footer}

{tracker}</body>
</html>
'''
(ROOT / 'thanks-kippur.html').write_text(thanks, encoding='utf-8')
print('ok')
