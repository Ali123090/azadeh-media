from weasyprint import HTML
OX="#3B0D11"; RED="#A4161A"; TEAL="#E9A23B"; PINK="#F7DCD6"; CREAM="#FFF6F2"; WHITE="#FFFFFF"
def capsule(cx,cy,c,rot=-30,s=1):
    return f'''<g transform="translate({cx},{cy}) rotate({rot}) scale({s})"><rect x="-62" y="-24" width="124" height="48" rx="24" fill="{WHITE}" stroke="{OX}" stroke-width="5"/>
<path d="M0 -24 H-38 A24 24 0 0 0 -38 24 H0 Z" fill="{c}"/><rect x="-50" y="-14" width="34" height="8" rx="4" fill="{WHITE}" opacity=".45"/></g>'''
def tablet(cx,cy,c=WHITE,label=""):
    return f'''<g transform="translate({cx},{cy})"><ellipse cx="0" cy="8" rx="46" ry="14" fill="{OX}" opacity=".15"/><circle r="44" fill="{c}" stroke="{OX}" stroke-width="5"/><line x1="-30" y1="0" x2="30" y2="0" stroke="{OX}" stroke-width="4"/></g>'''
def milk(cx,cy):
    return f'''<g transform="translate({cx-40},{cy-70})"><path d="M8 34 L22 6 H58 L72 34 Z" fill="#dfe9f5" stroke="{OX}" stroke-width="5" stroke-linejoin="round"/>
<rect x="8" y="34" width="64" height="104" rx="6" fill="{WHITE}" stroke="{OX}" stroke-width="5"/><rect x="8" y="64" width="64" height="40" fill="#4A7FB5"/><path d="M22 84 Q40 70 58 84" stroke="{WHITE}" stroke-width="4" fill="none"/></g>'''
def grapefruit(cx,cy):
    seg="".join(f'<line x1="0" y1="0" x2="{round(52*__import__("math").cos(i*0.785),1)}" y2="{round(52*__import__("math").sin(i*0.785),1)}" stroke="#F2A07B" stroke-width="5"/>' for i in range(8))
    return f'''<g transform="translate({cx},{cy})"><circle r="66" fill="#F08A5D" stroke="{OX}" stroke-width="5"/><circle r="54" fill="#FFD3C0"/><circle r="52" fill="#F7A587"/>{seg}<circle r="9" fill="#FFE6DA"/></g>'''
def greens(cx,cy):
    return f'''<g transform="translate({cx},{cy})">
<path d="M-6 60 C-60 30 -62 -40 -20 -66 C0 -20 6 20 -6 60 Z" fill="#4E8F5C" stroke="{OX}" stroke-width="5"/>
<path d="M4 60 C60 30 64 -46 22 -70 C2 -24 -6 20 4 60 Z" fill="#6DB07A" stroke="{OX}" stroke-width="5"/>
<path d="M-8 56 C-24 20 -24 -20 -20 -56" stroke="{WHITE}" stroke-width="3" fill="none" opacity=".7"/><path d="M6 56 C22 20 24 -24 20 -60" stroke="{WHITE}" stroke-width="3" fill="none" opacity=".7"/>
<rect x="-14" y="56" width="28" height="18" rx="6" fill="#B5651D" stroke="{OX}" stroke-width="4"/></g>'''
def clash(cx,cy):
    return f'''<g transform="translate({cx},{cy})"><circle r="34" fill="{RED}" stroke="{CREAM}" stroke-width="7"/>
<line x1="-13" y1="-13" x2="13" y2="13" stroke="{WHITE}" stroke-width="8" stroke-linecap="round"/><line x1="13" y1="-13" x2="-13" y2="13" stroke="{WHITE}" stroke-width="8" stroke-linecap="round"/></g>'''
def card(left_svg,right_svg,title,sub,pos=""):
    return f'''<div class="card" style="{pos}"><svg width="440" height="190" viewBox="0 0 440 190">
<circle cx="120" cy="95" r="82" fill="{PINK}"/><circle cx="320" cy="95" r="82" fill="{PINK}"/>
{left_svg}{right_svg}{clash(220,95)}</svg>
<div class="t">{title}</div><div class="s">{sub}</div></div>'''
# RTL reading: right item first
cards = card(milk(120,100), capsule(320,95,"#4A7FB5"), "آنتی‌بیوتیک + لبنیات","با شیر، کلسیم یا آهن<br>بعضی آنتی‌بیوتیک‌ها جذب نمی‌شن","top:415px;right:50px") + \
        card(grapefruit(120,95), capsule(320,95,"#C0392B"), "داروی چربی خون + گریپ‌فروت","سطح دارو در خون<br>خطرناک بالا می‌ره","top:415px;left:50px") + \
        card(greens(120,92), capsule(320,95,"#E9A23B"), "وارفارین + سبزی برگ‌سبز","مقدارش رو ناگهانی<br>زیاد یا کم نکن","top:820px;right:50px") + \
        card(capsule(120,95,"#7A4FA0"), tablet(320,95), "آسپرین قلبی + ایبوپروفن","بدون مشورت نخور؛<br>اثر آسپرین کم می‌شه","top:820px;left:50px")
stripes = "".join(f'<polygon points="{x},0 {x+40},0 {x+10},34 {x-30},34" fill="{TEAL}"/>' for x in range(-40,1140,80))
html=f'''<html dir="rtl"><head><meta charset="utf-8"><style>
@page{{size:1080px 1350px;margin:0}} html,body{{margin:0}}
.f{{width:1080px;height:1350px;position:relative;overflow:hidden;background:{CREAM};font-family:Vazirmatn}}
.top{{position:absolute;top:0;left:0;right:0;height:360px;background:{OX}}}
.badge{{position:absolute;top:50px;right:80px;background:{TEAL};color:{OX};font-family:Lalezar;font-size:40px;padding:6px 30px 2px;border-radius:40px}}
.d{{position:absolute;top:118px;right:80px;left:310px;margin:0;font-family:Lalezar;color:{WHITE};font-size:100px;line-height:1.15;text-align:right}}
.grid{{position:absolute;top:415px;right:50px;left:50px;display:flex;flex-wrap:wrap;justify-content:space-between}}
.card{{position:absolute;width:470px;height:380px;background:{WHITE};border-radius:34px;margin-bottom:26px;text-align:center;box-sizing:border-box;padding-top:16px;border:3px solid #F0DCD6}}
.t{{font-family:Lalezar;font-size:40px;color:{OX};line-height:1.3;margin-top:8px;padding:0 14px}}
.s{{font-size:28px;color:#6b4a4d;line-height:1.55;margin-top:6px}}
.foot{{position:absolute;bottom:40px;right:50px;left:50px;height:90px;background:{RED};border-radius:46px;}}
.fw{{font-family:Lalezar;color:{WHITE};font-size:40px}}
.hd{{font-weight:bold;font-size:28px;color:#FFD9D2;direction:ltr}}
</style></head><body><div class="f">
<div class="top"></div>
<svg width="1080" height="380" style="position:absolute;top:0;left:0">
<circle cx="150" cy="170" r="130" fill="{RED}" opacity=".45"/><circle cx="150" cy="170" r="86" fill="{RED}"/>
<text x="150" y="222" text-anchor="middle" font-family="Lalezar" font-size="150" fill="{WHITE}">!</text>
<g transform="translate(0,346)">{stripes}</g></svg>
<div class="badge">تداخل‌های رایج</div>
<p class="d">این‌ها رو<br>با هم نخور</p>
{cards}
<div class="foot"></div><div class="fw" style="position:absolute;bottom:58px;right:100px">قبل از هر داروی جدید، از داروساز بپرس</div><div class="hd" style="position:absolute;bottom:72px;left:100px">@dr.azadehpharma</div>
</div></body></html>'''
HTML(string=html).write_pdf("post_inter2.pdf")
