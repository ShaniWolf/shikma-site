"""קידום המתנות של המשפך (25.9.2026): השאלון, הצ׳קליסט, שעת העומס ולהכין את הלב.
1. עמודה חדשה בפוטר של כל העמודים: ״כלים ללא עלות״.
2. הבלוק ״כלים ללא עלות שאפשר להתחיל מהם כבר היום״ (מועתק כמו שהוא מ-guides.html, הטקסט של שקמה)
   בעמוד הבית אחרי ״מה מעסיק אתכם עכשיו?״ ובעמודי התוכן לפני ״קראו עוד בנושא״.
3. style.css: הפוטר ל-5 עמודות. אידמפוטנטי (f-gifts)."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[2]

FOOT = '''      <div class="f-nav f-gifts">
        <h3 class="f-h">כלים ללא עלות</h3>
        <ul class="f-links">
          <li><a href="quiz.html">שאלון: איפה הדאבל פוגש אותך?</a></li>
          <li><a href="both-now.html">צ׳קליסט: כששניהם צריכים אותי עכשיו</a></li>
          <li><a href="rush-hour.html">שעת העומס בדאבל</a></li>
          <li><a href="lev.html">להכין את הלב</a></li>
        </ul>
      </div>
'''
g = (ROOT / 'guides.html').read_text(encoding='utf-8')
GSEC = re.search(r'  <section class="gsec rv".*?</section>\n', g, re.S).group(0)
assert 'quiz.html' in GSEC and 'rush-hour.html' in GSEC

for p in sorted(ROOT.glob('*.html')):
    s = p.read_text(encoding='utf-8'); orig = s
    if 'f-topics' in s and 'f-gifts' not in s:
        s, n = re.subn(r'(      <div class="f-nav f-topics">.*?\n      </div>\n)', lambda m: m.group(1) + FOOT, s, count=1, flags=re.S)
        assert n == 1, p.name
    if p.name in ('tantrums.html', 'gvulot.html', 'siblings.html', 'tantrum-gil-shnatayim.html') and 'class="gsec' not in s:
        s, n = re.subn(r'(\n)(  <div class="readmore rv">)', lambda m: m.group(1) + GSEC + m.group(2), s, count=1)
        assert n == 1, p.name
    if p.name == 'index.html' and 'class="gsec' not in s:
        s, n = re.subn(r'(<section id="guides">.*?</section>\n)', lambda m: m.group(1) + '\n<section>\n  <div class="wrap">\n' + GSEC.replace(' style="margin:30px 0 8px"', '') + '  </div>\n</section>\n', s, count=1, flags=re.S)
        assert n == 1
    if s != orig: p.write_text(s, encoding='utf-8'); print('patched', p.name)

css = ROOT / 'style.css'; c = css.read_text(encoding='utf-8')
c = c.replace('.f-grid{grid-template-columns:1.15fr .7fr 1fr 1fr}', '.f-grid{grid-template-columns:1.1fr .6fr 1fr .95fr .95fr}')
css.write_text(c, encoding='utf-8')
