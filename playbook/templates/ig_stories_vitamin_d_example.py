import base64, math
from weasyprint import HTML
OX="#3B0D11"; RED="#A4161A"; AMB="#E9A23B"; SUN="#F4B740"; CREAM="#FFF6EC"; PINK="#F7DCD6"; WHITE="#FFFFFF"; BALE="#00A884"
CSS=f"""@page{{size:1080px 1920px;margin:0}} html,body{{margin:0}}
.f{{width:1080px;height:1920px;position:relative;overflow:hidden;background:{CREAM};font-family:Vazirmatn}}
.a{{position:absolute}} .L{{font-family:Lalezar;line-height:1.2;margin:0}}
.badge{{background:{AMB};color:{OX};font-family:Lalezar;font-size:46px;padding:8px 34px 2px;border-radius:44px}}
.card{{background:{WHITE};border-radius:38px;border:3px solid #F1E0CF;box-sizing:border-box}}
.hd{{font-weight:bold;font-size:32px;direction:ltr}}"""
def sun(cx,cy,r,col=SUN):
    s="".join(f'<line x1="{cx+(r+16)*math.cos(i*math.pi/6):.1f}" y1="{cy+(r+16)*math.sin(i*math.pi/6):.1f}" x2="{cx+(r+54)*math.cos(i*math.pi/6):.1f}" y2="{cy+(r+54)*math.sin(i*math.pi/6):.1f}" stroke="{col}" stroke-width="15" stroke-linecap="round"/>' for i in range(12))
    return s+f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}"/>'
def softgel(cx,cy,rot=-25,s=1):
    return f'<g transform="translate({cx},{cy}) rotate({rot}) scale({s})"><ellipse rx="70" ry="38" fill="{AMB}" stroke="{OX}" stroke-width="5"/><ellipse cx="-20" cy="-12" rx="28" ry="9" fill="{WHITE}" opacity=".55"/><text x="4" y="16" text-anchor="middle" font-family="Lalezar" font-size="46" fill="{OX}">D</text></g>'
def page(body,name):
    HTML(string=f'<html dir="rtl"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="f">{body}</div></body></html>').write_pdf(name+".pdf")
handle=f'<div class="a hd" style="top:1690px;left:0;right:0;text-align:center;color:{OX}">@dr.azadehpharma</div>'

water=f'''<svg width="250" height="210" viewBox="0 0 300 230"><circle cx="150" cy="115" r="105" fill="#E3F0F8"/>
<g transform="translate(95,40)"><path d="M0 0 H80 L72 150 Q71 160 61 160 H19 Q9 160 8 150 Z" fill="#BFE0F2" stroke="{OX}" stroke-width="5"/><path d="M0 0 H80 L78 30 H2 Z" fill="{WHITE}"/></g>{softgel(215,170,-20,0.7)}</svg>'''
meal=f'''<svg width="250" height="210" viewBox="0 0 300 230"><circle cx="150" cy="115" r="105" fill="#FBE7CF"/>
<ellipse cx="140" cy="130" rx="95" ry="58" fill="{WHITE}" stroke="{OX}" stroke-width="5"/><ellipse cx="140" cy="130" rx="70" ry="40" fill="#F3EDE4"/>
<ellipse cx="115" cy="125" rx="30" ry="22" fill="{WHITE}" stroke="{OX}" stroke-width="3"/><circle cx="115" cy="125" r="11" fill="{SUN}"/>
<path d="M150 110 q22 -18 40 2 q-8 30 -40 22 z" fill="#7FB069" stroke="{OX}" stroke-width="3"/><circle cx="172" cy="118" r="8" fill="#8B5A2B"/>{softgel(235,60,-20,0.7)}</svg>'''

# ---- Story 1: quiz ----
def opt(top,letter,svg,text):
    return f'''<div class="a card" style="top:{top}px;right:70px;left:70px;height:290px"></div>
<div class="a L" style="top:{top+70}px;right:115px;width:130px;height:130px;border-radius:65px;background:{AMB};color:{OX};font-size:84px;text-align:center;line-height:150px">{letter}</div>
<p class="a L" style="top:{top+95}px;right:280px;font-size:56px;color:{OX}">{text}</p>
<div class="a" style="top:{top+40}px;left:100px">{svg}</div>'''
s1=f'''<div class="a" style="top:0;left:0;right:0;height:820px;background:{OX}"></div>
<svg class="a" style="top:0;left:0" width="1080" height="820">{sun(190,520,90)}{softgel(190,520,-20,1.1)}</svg>
<div class="a badge" style="top:270px;right:80px">تست ۱۰ ثانیه‌ای ☀️</div>
<p class="a L" style="top:370px;right:80px;left:330px;color:{WHITE};font-size:92px">ویتامین D رو<br>کِی بخوریم<br>بهتر جذب بشه؟</p>
{opt(880,"الف",water,"ناشتا، با آب")}
{opt(1200,"ب",meal,"با غذای چرب‌دار")}
<div class="a" style="top:1505px;left:70px;right:70px;height:100px;background:{RED};border-radius:50px"></div>
<p class="a L" style="top:1525px;right:0;left:0;text-align:center;color:{WHITE};font-size:50px">جوابتو دایرکت کن: الف یا ب؟</p>
<p class="a L" style="top:1625px;right:0;left:0;text-align:center;color:{OX};font-size:40px">جواب درست: امشب ساعت ۹</p>'''+handle.replace('top:1690px','top:1710px')
page(s1,"s1")

# ---- Story 2: self-check ----
items=["خستگی مداومِ بی‌دلیل","درد استخوان یا کمر","ضعف یا گرفتگی عضلات","سرماخوردگی‌های مکرر","ریزش موی زیاد","بی‌حوصلگی و خلق پایین"]
rows=""
for i,t in enumerate(items):
    top=760+i*118
    rows+=f'''<div class="a card" style="top:{top}px;right:70px;left:70px;height:100px"></div>
<svg class="a" style="top:{top+22}px;right:100px" width="58" height="58"><rect x="4" y="4" width="50" height="50" rx="12" fill="{CREAM}" stroke="{AMB}" stroke-width="6"/></svg>
<p class="a L" style="top:{top+26}px;right:185px;font-size:46px;color:{OX}">{t}</p>
<p class="a L" style="top:{top+22}px;left:110px;font-size:50px;color:#E8CDB8">{"۱۲۳۴۵۶"[i]}</p>'''
s2=f'''<div class="a" style="top:0;left:0;right:0;height:700px;background:{OX}"></div>
<svg class="a" style="top:0;left:0" width="1080" height="700"><circle cx="210" cy="470" r="150" fill="{RED}" opacity=".35"/>{sun(210,470,80)}
<text x="210" y="505" text-anchor="middle" font-family="Lalezar" font-size="100" fill="{OX}">D</text></svg>
<div class="a badge" style="top:270px;right:80px">خودت رو چک کن</div>
<p class="a L" style="top:370px;right:80px;left:430px;color:{WHITE};font-size:92px">چند تا از<br>این‌ها رو داری؟</p>
{rows}
<div class="a" style="top:1480px;left:70px;right:70px;height:100px;background:{RED};border-radius:50px"></div>
<p class="a L" style="top:1500px;right:0;left:0;text-align:center;color:{WHITE};font-size:50px">عددش رو برام دایرکت کن 👇</p>
<p class="a" style="top:1595px;right:90px;left:90px;margin:0;text-align:center;font-size:28px;color:#6b4a4d;line-height:1.6">این علائم اختصاصی نیستن؛ فقط آزمایش خون مشخص می‌کنه کمبود داری یا نه.</p>{handle}'''
page(s2,"s2")

# ---- Story 3: answer ----
tips=[("با بزرگ‌ترین وعده‌ی غذایی","ویتامین D محلول در چربیه"),
      ("دوز بالا فقط با تجویز پزشک","مصرف خودسرانه خطر مسمومیت داره"),
      ("اول آزمایش، بعد مکمل","آزمایش «۲۵-هیدروکسی ویتامین D»")]
tr=""
for i,(t,s) in enumerate(tips):
    top=850+i*215
    tr+=f'''<div class="a card" style="top:{top}px;right:70px;left:70px;height:185px"></div>
<div class="a L" style="top:{top+48}px;right:105px;width:90px;height:90px;border-radius:45px;background:{AMB};color:{OX};font-size:60px;text-align:center;line-height:100px">{"۱۲۳"[i]}</div>
<p class="a L" style="top:{top+34}px;right:230px;left:100px;font-size:52px;color:{OX}">{t}</p>
<p class="a" style="top:{top+110}px;right:230px;left:100px;margin:0;font-size:34px;color:#6b4a4d">{s}</p>'''
s3=f'''<div class="a" style="top:0;left:0;right:0;height:790px;background:{OX}"></div>
<svg class="a" style="top:0;left:0" width="1080" height="790">{sun(200,520,80)}{softgel(200,520,-20,1)}</svg>
<div class="a badge" style="top:270px;right:80px">جواب تست ظهر</div>
<p class="a L" style="top:370px;right:80px;color:{WHITE};font-size:170px">گزینه‌ی <span style="color:{AMB}">ب</span></p>
<p class="a L" style="top:600px;right:80px;color:#FFD9C2;font-size:58px">همراه غذای چرب‌دار ✓</p>
{tr}
<div class="a" style="top:1530px;left:70px;right:70px;height:100px;background:{RED};border-radius:50px"></div>
<p class="a L" style="top:1550px;right:0;left:0;text-align:center;color:{WHITE};font-size:50px">درست گفتی؟ برای دوستت بفرست</p>{handle}'''
page(s3,"s3")

# ---- Story 4: Bale invite with fanned thumbnails ----
def b64(p): return "data:image/png;base64,"+base64.b64encode(open(p,'rb').read()).decode()
th=["/home/claude/d/post3.png","/home/claude/d/post2.png","/home/claude/d/post1.png"]
fan=""
for i,(p,rot,l) in enumerate(zip(th,[-10,0,10],[150,330,510])):
    fan+=f'<img class="a" src="{b64(p)}" style="top:{380+abs(rot)*3}px;left:{l}px;width:400px;height:500px;border-radius:26px;transform:rotate({rot}deg);box-shadow:0 18px 40px rgba(0,0,0,.35)"/>'
s4=f'''<div class="a" style="top:0;left:0;right:0;height:1080px;background:{OX}"></div>
<svg class="a" style="top:0;left:0" width="1080" height="1080"><circle cx="540" cy="640" r="380" fill="{RED}" opacity=".3"/></svg>
<div class="a badge" style="top:265px;right:370px;left:370px;text-align:center">کانال بله‌ی ما</div>
{fan}
<p class="a L" style="top:1140px;right:80px;left:80px;text-align:center;color:{OX};font-size:84px">نکته‌های روزانه‌ی داروساز<br>هر روز، تو کانال بله</p>
<p class="a" style="top:1380px;right:100px;left:100px;margin:0;text-align:center;font-size:36px;color:#6b4a4d;line-height:1.6">تست، چک‌لیست، تداخل‌های دارویی و جواب سؤال‌هات</p>
<div class="a" style="top:1490px;left:120px;right:120px;height:120px;background:{BALE};border-radius:60px"></div>
<p class="a" style="top:1518px;right:0;left:0;margin:0;text-align:center;color:{WHITE};font-weight:bold;font-size:52px;direction:ltr">@Drazadehpharma</p>
<p class="a" style="top:1640px;right:0;left:0;margin:0;text-align:center;color:{OX};font-size:34px;direction:ltr">ble.ir/Drazadehpharma</p>'''
page(s4,"s4")
