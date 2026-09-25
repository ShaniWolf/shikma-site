"""שאלון (25.9.2026): ההרשמה עוברת מלפני השאלון לסוף שלו.
קודם עונים על 8 השאלות ורואים את התוצאה (הכותרת וההסבר). הכלים ״מה יכול לעזור לך כבר עכשיו?״
והמדריך נפתחים אחרי השארת פרטים. מי שכבר נרשמה בדפדפן הזה רואה הכול מיד.
עורך את quiz.html החי; אידמפוטנטי (qz-more)."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[2]
p = ROOT / 'quiz.html'; s = p.read_text(encoding='utf-8')
if 'qz-more' in s: print('skip quiz.html'); raise SystemExit

# 1. הכפתור בפתיחה מוביל ישר לשאלה הראשונה
s, a = re.subn(r'data-go="form">', 'data-go="q0">', s)

# 2. שלב הטופס יוצא מלפני השאלון והופך ל״שער״ שמופיע בתוך התוצאה
m = re.search(r'  <div class="qz-step" data-step="form" hidden>\n.*?\n  </div>\n(?=  <div class="qz-step" data-step="q0")', s, re.S)
form = re.search(r'    <form class="mform" id="mf".*?</form>\n', m.group(0), re.S).group(0)
form = form.replace('<button type="submit">מתחילות בשאלון</button>', '<button type="submit">לראות מה יכול לעזור לי</button>')
s = s[:m.start()] + s[m.end():]
gate = ('  <div class="qz-gate" id="qz-gate" hidden style="margin-top:22px;padding-top:18px;border-top:1px solid var(--line)">\n'
        '    <h3 style="margin-top:0">מה יכול לעזור לך כבר עכשיו?</h3>\n'
        '    <p>השאירי פרטים ותראי מיד את הכלים שמתאימים בדיוק לתוצאה שלך.</p>\n'
        + form + '  </div>\n')

# 3. בכל תוצאה: מה שמתחת לכותרת ״מה יכול לעזור...״ נעטף ונפתח רק אחרי ההרשמה
def wrap(mm):
    body = mm.group(2)
    i = body.index('    <h3>')
    inner = ''.join('  ' + ln + '\n' for ln in body[i:].rstrip('\n').split('\n'))
    return mm.group(1) + body[:i] + '    <div class="qz-more" hidden>\n' + inner + '    </div>\n  </div>\n'
s, b = re.subn(r'(  <div class="qz-step qz-res" data-step="res-[abcd]" hidden>\n)(.*?)  </div>\n(?=  <div class="qz-step qz-res"|  </div>\n  <div class="csec)', wrap, s, flags=re.S)
s, c = re.subn(r'(\n  </div>\n)(  <div class="csec rv")', lambda mm: '\n' + gate + '  </div>\n' + mm.group(2), s, count=1)

# 4. הסקריפט של השאלון
OLD_JS = re.search(r"  root\.querySelector\('\[data-go=form\]'\).*?\n  \}\); \}\);\n", s, re.S)
NEW_JS = """  var gate=document.getElementById('qz-gate'), cur=null;
  function seen(){ try{ return localStorage.getItem('imale_quiz_ok')==='1'; }catch(e){ return false; } }
  function open(){ gate.hidden=true; cur.querySelector('.qz-more').hidden=false; }
  root.querySelector('[data-go=q0]').addEventListener('click', function(){ show('q0'); ga('quiz_start'); });
  document.getElementById('mf').addEventListener('submit', function(e){ e.preventDefault();
    imaleSubmit(this, '199585225455436936', 'quiz', function(){ try{ localStorage.setItem('imale_quiz_ok','1'); }catch(e){} open(); }); });
  root.querySelectorAll('.qz-opt').forEach(function(b){ b.addEventListener('click', function(){
    score[b.getAttribute('data-cat')]++; qi++;
    if(qi<N){ show('q'+qi); return; }
    var k=['a','b','c'].sort(function(x,y){ return score[y]-score[x]; }), top=k[0];
    var res = (score[top]>=4 && score[top]-score[k[1]]>=2) ? top : 'd';
    show('res-'+res); ga('quiz_complete',{result:res});
    cur=root.querySelector('[data-step=res-'+res+']');
    if(seen()){ open(); return; }
    cur.insertBefore(gate, cur.querySelector('.qz-more')); gate.hidden=false; ga('quiz_gate',{result:res});
  }); });
"""
s = s[:OLD_JS.start()] + NEW_JS + s[OLD_JS.end():]
assert (a, b, c) == (1, 4, 1), (a, b, c)
p.write_text(s, encoding='utf-8'); print('patched quiz.html')
