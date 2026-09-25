"""טפסי ההרשמה (25.9.2026): שם פרטי, שם משפחה ומייל — שלושתם חובה.
עורך את ה-HTML החי ואת page_magnets.py; אידמפוטנטי (last_name)."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[2]

LABEL = re.compile(r'<label for="([\w-]+)-name">איך לפנות אליכם\? \(לא חובה\)</label>\n(\s*)<input type="text" id="\1-name" name="name" autocomplete="given-name" placeholder="שם פרטי">')
def fields(m):
    i, ind = m.group(1), m.group(2)
    return ('<label for="%s-name">שם פרטי</label>\n%s<input type="text" id="%s-name" name="name" autocomplete="given-name" required placeholder="שם פרטי">\n'
            '%s<label for="%s-last">שם משפחה</label>\n%s<input type="text" id="%s-last" name="last_name" autocomplete="family-name" required placeholder="שם משפחה">') % (i, ind, i, ind, i, ind, i)

CHECK = "    var last=(f.querySelector('input[name=last_name]')||{value:''}).value.trim();\n    if(!name || !last){ err.textContent='צריך שם פרטי ושם משפחה'; return; }\n"
BODY_OLD = re.compile(r"\(name\?'&fields%%5Bname%%5D='\+encodeURIComponent\(name\)\+'&fields%%5Bfirst_name%%5D='\+encodeURIComponent\(name\.split\(' '\)\[0\]\):''\)".replace('%%', '%'))
BODY_NEW = "'&fields%5Bname%5D='+encodeURIComponent(name)+'&fields%5Bfirst_name%5D='+encodeURIComponent(name)+'&fields%5Blast_name%5D='+encodeURIComponent(last)"

def patch_text(s, js_pct=False):
    s, a = LABEL.subn(fields, s)
    body_old = BODY_OLD if not js_pct else re.compile(BODY_OLD.pattern.replace('%', '%%'))
    body_new = BODY_NEW if not js_pct else BODY_NEW.replace('%', '%%')
    s, b = body_old.subn(lambda m: body_new, s)
    s, c = re.subn(r"(\n)(    if\(!email \|\| email\.indexOf)", lambda m: m.group(1) + CHECK + m.group(2), s, count=1)
    return s, (a, b, c)

for name in ['lev.html', 'kippur.html', 'checklist.html', 'omes.html']:
    p = ROOT / name; s = p.read_text(encoding='utf-8')
    if 'last_name' in s: print('skip', name); continue
    s, r = patch_text(s); assert r == (1, 1, 1), (name, r)
    p.write_text(s, encoding='utf-8'); print('patched', name)

p = ROOT / 'spec/build/page_magnets.py'; s = p.read_text(encoding='utf-8')
if 'last_name' not in s:
    s, r = patch_text(s, js_pct=True); assert r == (1, 1, 1), ('page_magnets', r)
    p.write_text(s, encoding='utf-8'); print('patched page_magnets.py')
