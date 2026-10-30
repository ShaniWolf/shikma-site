# -*- coding: utf-8 -*-
"""30.10: אירוע purchase חוזר לאנליטיקס, אבל רק במקום שבו יש קונה אמיתית.

ב-11.9 הורדנו את purchase מעמודי התודה כי הוא נורה בכל כניסה לעמוד (כולל הבדיקות שלנו),
וכל ביקור נספר כהכנסה. אין כתובת חזרה ב-pay360, אז אף אחת לא מגיעה לעמוד התודה אחרי תשלום.

מה שכן קורה: הקונה מקבלת מייל מסירה עם קישור ל-thanks-double.html ולוחצת ״להורדה״.
הקישור הזה נמצא רק במייל שנשלח לקבוצה ״רכשו: הורות בדאבל״, כלומר רק לקונות.
לכן purchase נורה עכשיו רק בלחיצה על ההורדה, פעם אחת לכל מכשיר (localStorage),
עם transaction_id ייחודי (GA4 מסנן כפילויות לפי זה), ולא כשיש ?test בכתובת.

מגבלות: קונה שלא פתחה את המייל לא נספרת. קונה שהורידה משני מכשירים נספרת פעמיים.
המחיר (99) הוא מחיר ההשקה; כשהוא משתנה מעדכנים כאן ומריצים שוב.
"""
import pathlib
P = pathlib.Path(__file__).resolve().parents[2] / 'thanks-double.html'
PRICE = 99
OLD = "  if(h.indexOf('double-full.pdf') > -1 && typeof gtag === 'function'){ gtag('event','guide_download',{guide:'double-full',page_path:location.pathname}); }\n"
NEW = """  if(h.indexOf('double-full.pdf') > -1 && typeof gtag === 'function'){
    gtag('event','guide_download',{guide:'double-full',page_path:location.pathname});
    var k='imale_purchase_double', done=false;
    try{ done=!!localStorage.getItem(k); }catch(err){}
    if(!done && location.search.indexOf('test')<0){
      var tid='dbl-'+Date.now().toString(36)+Math.random().toString(36).slice(2,7);
      gtag('event','purchase',{transaction_id:tid,value:%d,currency:'ILS',items:[{item_id:'double',item_name:'הורות בדאבל',price:%d,quantity:1}]});
      try{ localStorage.setItem(k,tid); }catch(err){}
    }
  }
""" % (PRICE, PRICE)
h = P.read_text(encoding='utf-8')
if "gtag('event','purchase'" in h:
    print('already there'); raise SystemExit
assert h.count(OLD) == 1
P.write_text(h.replace(OLD, NEW), encoding='utf-8')
print('ok')
