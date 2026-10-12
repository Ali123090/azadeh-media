from weasyprint import HTML
OX="#3B0D11"; RED="#A4161A"; AMB="#E9A23B"; SUN="#F4B740"; CREAM="#FFF6EC"; PINK="#F7DCD6"; WHITE="#FFFFFF"; GRN="#1F7A4D"
CSS=f"""@page{{size:1080px 1350px;margin:0}} html,body{{margin:0}}
.f{{width:1080px;height:1350px;position:relative;overflow:hidden;background:{CREAM};font-family:Vazirmatn}}
.a{{position:absolute}} .L{{font-family:Lalezar;line-height:1.2;margin:0}}
.badge{{background:{AMB};color:{OX};font-family:Lalezar;font-size:40px;padding:6px 30px 2px;border-radius:40px}}
.card{{background:{WHITE};border-radius:34px;border:3px solid #F1E0CF;box-sizing:border-box}}
.hd{{font-weight:bold;font-size:28px;direction:ltr}}"""
def sun(cx,cy,r,rays=12,col=SUN):
    import math
    s="".join(f'<line x1="{cx+(r+16)*math.cos(i*2*math.pi/rays):.1f}" y1="{cy+(r+16)*math.sin(i*2*math.pi/rays):.1f}" x2="{cx+(r+52)*math.cos(i*2*math.pi/rays):.1f}" y2="{cy+(r+52)*math.sin(i*2*math.pi/rays):.1f}" stroke="{col}" stroke-width="14" stroke-linecap="round"/>' for i in range(rays))
    return s+f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}"/>'
def softgel(cx,cy,rot=-25,s=1):
    return f'<g transform="translate({cx},{cy}) rotate({rot}) scale({s})"><ellipse rx="70" ry="38" fill="{AMB}" stroke="{OX}" stroke-width="5"/><ellipse cx="-20" cy="-12" rx="28" ry="9" fill="{WHITE}" opacity=".55"/><text x="4" y="16" text-anchor="middle" font-family="Lalezar" font-size="46" fill="{OX}">D</text></g>'
def page(body,name):
    HTML(string=f'<html dir="rtl"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="f">{body}</div></body></html>').write_pdf(name+".pdf")

# ---------- Post 1: quiz ----------
water=f'''<svg width="300" height="230" viewBox="0 0 300 230"><circle cx="150" cy="115" r="105" fill="#E3F0F8"/>
<g transform="translate(95,40)"><path d="M0 0 H80 L72 150 Q71 160 61 160 H19 Q9 160 8 150 Z" fill="#BFE0F2" stroke="{OX}" stroke-width="5"/><path d="M0 0 H80 L78 30 H2 Z" fill="{WHITE}"/></g>
{softgel(215,170,-20,0.7)}</svg>'''
meal=f'''<svg width="300" height="230" viewBox="0 0 300 230"><circle cx="150" cy="115" r="105" fill="#FBE7CF"/>
<ellipse cx="140" cy="130" rx="95" ry="58" fill="{WHITE}" stroke="{OX}" stroke-width="5"/><ellipse cx="140" cy="130" rx="70" ry="40" fill="#F3EDE4"/>
<ellipse cx="115" cy="125" rx="30" ry="22" fill="{WHITE}" stroke="{OX}" stroke-width="3"/><circle cx="115" cy="125" r="11" fill="{SUN}"/>
<path d="M150 110 q22 -18 40 2 q-8 30 -40 22 z" fill="#7FB069" stroke="{OX}" stroke-width="3"/><circle cx="172" cy="118" r="8" fill="#8B5A2B"/>
{softgel(235,60,-20,0.7)}</svg>'''
b1=f'''<div class="a" style="top:0;left:0;right:0;height:470px;background:{OX}"></div>
<svg class="a" style="top:0;left:0" width="1080" height="470">{sun(170,190,70)}{softgel(170,190,-20,0.85)}</svg>
<div class="a badge" style="top:60px;right:80px">تست ۱۰ ثانیه‌ای</div>
<p class="a L" style="top:140px;right:80px;left:330px;color:{WHITE};font-size:82px">ویتامین D رو<br>کِی بخوریم که<br>بهتر جذب بشه؟</p>
<div class="a card" style="top:520px;right:60px;width:465px;height:520px;text-align:center;padding-top:20px">
<div class="L" style="font-size:96px;color:{AMB}">الف</div>{water}
<div class="L" style="font-size:42px;color:{OX};margin-top:8px">ناشتا، با یه لیوان آب</div></div>
<div class="a card" style="top:520px;left:60px;width:465px;height:520px;text-align:center;padding-top:20px">
<div class="L" style="font-size:96px;color:{AMB}">ب</div>{meal}
<div class="L" style="font-size:42px;color:{OX};margin-top:8px">همراه غذای چرب‌دار</div></div>
<div class="a" style="bottom:120px;left:60px;right:60px;height:110px;background:{RED};border-radius:56px"></div>
<p class="a L" style="bottom:150px;right:110px;color:{WHITE};font-size:46px">جواب درست: امروز ساعت ۴:۳۰ همین‌جا</p>
<svg class="a" style="bottom:140px;left:100px" width="80" height="80"><circle cx="40" cy="40" r="32" fill="none" stroke="{WHITE}" stroke-width="6"/><path d="M40 20 V40 L54 50" stroke="{WHITE}" stroke-width="6" fill="none" stroke-linecap="round"/></svg>
<div class="a hd" style="bottom:50px;left:80px;color:{OX}">@dr.azadehpharma</div>
<p class="a" style="bottom:44px;right:80px;margin:0;font-size:30px;color:#7a5a4a">بفرست برای کسی که مکمل ویتامین D می‌خوره</p>'''
page(b1,"post1")

# ---------- Post 2: self-check ----------
items=["خستگی مداومِ بی‌دلیل","درد استخوان یا کمر","ضعف یا گرفتگی عضلات","سرماخوردگی‌های مکرر","ریزش موی زیاد","بی‌حوصلگی و خلق پایین"]
rows=""
for i,t in enumerate(items):
    col = i%2; r = i//2
    top = 520 + r*170
    side = "right:60px" if col==0 else "left:60px"
    rows+=f'''<div class="a card" style="top:{top}px;{side};width:465px;height:145px"></div>
<svg class="a" style="top:{top+40}px;{'right:90px' if col==0 else 'right:555px'}" width="66" height="66"><rect x="4" y="4" width="58" height="58" rx="14" fill="{CREAM}" stroke="{AMB}" stroke-width="6"/></svg>
<p class="a L" style="top:{top+46}px;{'right:180px' if col==0 else 'right:645px'};font-size:33px;color:{OX};width:330px">{t}</p>'''
b2=f'''<div class="a" style="top:0;left:0;right:0;height:450px;background:{OX}"></div>
<svg class="a" style="top:0;left:0" width="1080" height="450"><circle cx="190" cy="220" r="150" fill="{RED}" opacity=".35"/>{sun(190,220,78)}
<text x="190" y="252" text-anchor="middle" font-family="Lalezar" font-size="96" fill="{OX}">D</text></svg>
<div class="a badge" style="top:60px;right:80px">خودت رو چک کن</div>
<p class="a L" style="top:140px;right:80px;left:400px;color:{WHITE};font-size:84px">چند تا از این‌ها<br>رو داری؟</p>
{rows}
<div class="a" style="top:1045px;left:60px;right:60px;height:150px;background:{PINK};border-radius:34px"></div>
<p class="a L" style="top:1068px;right:100px;left:100px;font-size:40px;color:{RED}">۳ تا یا بیشتر؟ وقتشه ویتامین D رو آزمایش بدی.</p>
<p class="a" style="top:1125px;right:100px;left:100px;margin:0;font-size:27px;color:{OX}">این علائم اختصاصی نیستن؛ فقط آزمایش خون مشخص می‌کنه کمبود داری یا نه.</p>
<div class="a hd" style="bottom:55px;left:80px;color:{OX}">@dr.azadehpharma</div>
<p class="a L" style="bottom:48px;right:80px;font-size:36px;color:{AMB}">پاییز = آفتاب کمتر = ویتامین D کمتر</p>'''
page(b2,"post2")

# ---------- Post 3: answer ----------
tips=[("با بزرگ‌ترین وعده‌ی غذایی","ویتامین D محلول در چربیه؛ کنار غذای چرب‌دار بهتر جذب می‌شه"),
      ("دوز بالا فقط با تجویز پزشک","دوز بالای خودسرانه (مثل ۵۰ هزار واحد) خطر مسمومیت داره"),
      ("اول آزمایش، بعد مکمل","آزمایش «۲۵-هیدروکسی ویتامین D» میزان واقعی رو نشون می‌ده")]
tr=""
for i,(t,s) in enumerate(tips):
    top=560+i*175
    tr+=f'''<div class="a card" style="top:{top}px;right:60px;left:60px;height:150px"></div>
<div class="a L" style="top:{top+38}px;right:95px;width:76px;height:76px;border-radius:38px;background:{AMB};color:{OX};font-size:52px;text-align:center;line-height:84px">{"۱۲۳"[i]}</div>
<p class="a L" style="top:{top+22}px;right:200px;left:90px;font-size:44px;color:{OX}">{t}</p>
<p class="a" style="top:{top+86}px;right:200px;left:90px;margin:0;font-size:29px;color:#6b4a4d">{s}</p>'''
b3=f'''<div class="a" style="top:0;left:0;right:0;height:500px;background:{OX}"></div>
<svg class="a" style="top:0;left:0" width="1080" height="500">{sun(180,250,66)}{softgel(180,250,-20,0.8)}</svg>
<div class="a badge" style="top:60px;right:80px">جواب تست صبح</div>
<p class="a L" style="top:140px;right:80px;color:{WHITE};font-size:150px">گزینه‌ی <span style="color:{AMB}">ب</span></p>
<p class="a L" style="top:340px;right:80px;left:330px;color:#FFD9C2;font-size:48px">همراه غذای چرب‌دار ✓</p>
{tr}
<div class="a" style="bottom:110px;left:60px;right:60px;height:110px;background:{RED};border-radius:56px"></div>
<p class="a L" style="bottom:138px;right:110px;color:{WHITE};font-size:44px">درست جواب دادی؟ برای دوستت هم بفرست</p>
<div class="a hd" style="bottom:45px;left:80px;color:{OX}">@dr.azadehpharma</div>'''
page(b3,"post3")
