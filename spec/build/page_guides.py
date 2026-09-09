# -*- coding: utf-8 -*-
from common import *

TITLE = 'תוכן ומדריכים להורים לצמודים | שקמה דגרי'
DESC = 'כל התכנים והמדריכים הדיגיטליים להורים לילדים צמודים: טנטרומים, גבולות, אח חדש ויחסי אחים, חגים וליווי אישי. בכל נושא תוכן פתוח ומדריך מעשי לבית עם שני קטנים.'

html = head(TITLE, DESC, 'guides.html', ld=[crumbs_ld(('תוכן ומדריכים', SITE + 'guides.html'))], body_class='cpage')
html += header()
html += '<div class="wrap" id="main">\n' + crumb('תוכן ומדריכים')
html += '''
  <div class="hero">
    %s
    <span class="kicker">כל התכנים והמדריכים במקום אחד</span>
    <h1>המדריכים</h1>
    <p class="lead">בחרו את הנושא שמעסיק אתכם עכשיו וקבלו הסברים וכלים שמתאימים למציאות עם שני ילדים קטנים.</p>
    <p class="lead">כל התכנים והמדריכים באתר מבוססים על שיטת ״הורות בדאבל״: לא להגיב רק למה שרואים מבחוץ, אלא להבין מה כל ילד צריך ולדעת איך לפעול גם כשהצרכים שלהם נפגשים באותו הרגע.</p>
  </div>

  <div class="csec gcard rv">
    %s
    <div class="tx">
      <p class="eyeb">ללא עלות</p><h2>להכין את הלב</h2>
      <p>המדריך לקראת הצטרפות אח או אחות: מה עובר על הבכורה או הבכור, איך מכינים אותם עוד מההיריון, ואיך נראים המפגש הראשון והשבועות שאחריו. משאירים מייל והוא אצלכם.</p>
      <p><a class="btn green" href="lev.html">אני רוצה את המדריך</a></p>
      <p class="btn-note">לפני זה אפשר לקרוא את <a href="siblings.html">התוכן הפתוח על אח חדש ויחסים בין האחים</a>.</p>
    </div>
  </div>

  <div class="csec gcard rv">
    %s
    <div class="tx">
      <p class="eyeb">99 ₪</p><h2>כשהבית מתפוצץ</h2>
      <p>מדריך מעשי לטנטרומים והתפרצויות במשפחה עם ילדים צמודים: מה לעשות לפני ההתפרצות, בזמן ההתפרצות ואחריה, גם כשהבכי מתחיל להגיע משני הכיוונים.</p>
      <p><a class="btn" href="tantrums.html#guide">לפרטים על המדריך</a></p>
      <p class="btn-note">מתלבטים? <a href="tantrums.html">התוכן הפתוח על טנטרומים</a> מסביר קודם מה קורה לילד.</p>
    </div>
  </div>

  <div class="csec gcard rv">
    %s
    <div class="tx">
      <p class="eyeb">99 ₪</p><h2>גבולות מתוך חיבור</h2>
      <p>מדריך מעשי להורים שרוצים להציב גבולות ברורים, להפחית מאבקי כוח ולבנות יותר שיתוף פעולה בלי לוותר על הקשר עם הילדים, כולל התאמות לבית עם שני קטנים.</p>
      <p><a class="btn" href="gvulot.html#guide">לפרטים על המדריך</a></p>
      <p class="btn-note">מתלבטים? <a href="gvulot.html">התוכן הפתוח על גבולות</a> מסביר קודם למה הם לא פשוט מקשיבים.</p>
    </div>
  </div>

  <div class="csec gcard rv">
    %s
    <div class="tx">
      <p class="eyeb">149 ₪</p><h2>לגדול ביחד</h2>
      <p>מסלול אחד, מההיריון ועד היחסים בין האחים: להכין את הבכור, לעבור מילד אחד לשניים, לתת מקום לקנאה ולתווך את המריבות בלי לבחור צד.</p>
      <p><a class="btn" href="siblings.html#guide">לפרטים על המדריך</a></p>
      <p class="btn-note">מתלבטים? <a href="siblings.html">התוכן הפתוח על אח חדש ויחסי אחים</a> מסביר קודם מה עובר על הבכור.</p>
    </div>
  </div>

  <div class="csec gcard rv">
    %s
    <div class="tx">
      <p class="eyeb">36 ₪</p><h2>חגים עם צמודים</h2>
      <p>מדריך קצר וממוקד להיערכות לחגים עם שני ילדים קטנים: מה שומרים, איפה מתגמשים ומה עושים כשהתוכנית כבר לא מתאימה לילדים. נקרא תוך שעה.</p>
      <p><a class="btn" href="chagim.html">לפרטים על המדריך</a></p>
    </div>
  </div>

  <div class="csec gcard rv">
    %s
    <div class="tx">
      <p class="eyeb">ליווי אישי</p><h2>צמודים בדרך שלכם</h2>
      <p>ליווי אישי של חודשיים בשיטת ״הורות בדאבל״: נסתכל יחד על מה שקורה אצלכם בבית ונבנה צעדים שמתאימים לילדים, להורים ולמציאות המשפחתית. בכל חודש נפתחים מספר מצומצם של מקומות.</p>
      <p><a class="btn" href="livuy.html">לפרטים על הליווי</a></p>
    </div>
  </div>

</div>
''' % (
  pola_side('shk-grass', 'יובל ותום עומדים זה מול זה על הדשא'),
  polaroid_cover('assets/covers/lev.png', 'כריכת המדריך להכין את הלב'),
  polaroid('pola-tantrums', 'אמא מחבקת שני ילדים קטנים במיטה', cls=''),
  polaroid('pola-gvulot', 'שני ילדים קטנים שוכבים על המיטה', cls='r'),
  polaroid('pola-siblings', 'פעוט שותה מבקבוק לצד אחותו התינוקת', cls=''),
  polaroid_cover('assets/covers/chagim.png', 'כריכת המדריך חגים עם צמודים'),
  polaroid('pola-livuy', 'אמא מחזיקה תינוק ופעוט נשען עליה', cls='r'),
)
html += footer() + CLICK_JS
write('guides.html', html)
