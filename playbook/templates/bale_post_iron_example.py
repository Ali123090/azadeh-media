from weasyprint import HTML
OX="#3B0D11"; RED="#A4161A"; TEA="#C8771E"; TEAL="#E9A23B"; PINK="#F7DCD6"; ORA="#F28C28"; WHITE="#FFFFFF"; OK="#1F7A4D"
def capsule(x,y,s,rot):
    return f'''<g transform="translate({x},{y}) rotate({rot}) scale({s})">
 <rect x="-130" y="-48" width="260" height="96" rx="48" fill="{WHITE}"/>
 <path d="M0 -48 H-82 A48 48 0 0 0 -82 48 H0 Z" fill="{RED}"/>
 <rect x="-112" y="-30" width="80" height="14" rx="7" fill="{WHITE}" opacity=".35"/>
 <rect x="-130" y="-48" width="260" height="96" rx="48" fill="none" stroke="{OX}" stroke-width="6"/></g>'''
ic_tea=f'''<svg width="110" height="110" viewBox="0 0 140 140"><ellipse cx="70" cy="126" rx="62" ry="10" fill="{OX}" opacity=".15"/>
<path d="M30 20 C30 20 32 70 48 90 C56 100 56 110 50 118 C46 126 52 130 70 130 C88 130 94 126 90 118 C84 110 84 100 92 90 C108 70 110 20 110 20 Z" fill="{TEA}" stroke="{OX}" stroke-width="5"/></svg>'''
ic_milk=f'''<svg width="110" height="110" viewBox="0 0 140 140"><path d="M38 20 H102 L96 124 Q95 132 86 132 H54 Q45 132 44 124 Z" fill="{WHITE}" stroke="{OX}" stroke-width="5"/><path d="M38 20 H102 L100 48 H40 Z" fill="#e9e1df"/></svg>'''
ic_ora=f'''<svg width="110" height="110" viewBox="0 0 140 140"><circle cx="70" cy="72" r="54" fill="{ORA}" stroke="{OX}" stroke-width="5"/><circle cx="70" cy="72" r="40" fill="#ffc27a"/>
<g stroke="{ORA}" stroke-width="5"><line x1="70" y1="32" x2="70" y2="112"/><line x1="30" y1="72" x2="110" y2="72"/><line x1="42" y1="44" x2="98" y2="100"/><line x1="98" y1="44" x2="42" y2="100"/></g><circle cx="70" cy="72" r="8" fill="{WHITE}"/></svg>'''
ic_thy=f'''<svg width="110" height="110" viewBox="0 0 140 140"><rect x="22" y="40" width="96" height="64" rx="10" fill="{WHITE}" stroke="{OX}" stroke-width="5"/><circle cx="50" cy="72" r="13" fill="#d7c9e8" stroke="{OX}" stroke-width="3"/><circle cx="90" cy="72" r="13" fill="#d7c9e8" stroke="{OX}" stroke-width="3"/></svg>'''
def row(icon,title,sub,good):
    mark = f'<span style="font-family:DejaVu Sans;color:{OK if good else RED};font-size:58px;font-weight:bold">{"✓" if good else "✗"}</span>'
    return f'''<div class="row"><div class="ic">{icon}</div><div class="tx"><div class="t">{title}</div><div class="s">{sub}</div></div><div class="mk">{mark}</div></div>'''
rows = row(ic_tea,"چای و قهوه","یکی دو ساعت با قرص آهن فاصله بنداز",False)+\
       row(ic_milk,"شیر، لبنیات و قرص کلسیم","جدا از آهن مصرف کن",False)+\
       row(ic_ora,"آب پرتقال یا ویتامین C","کنار آهن، جذبش رو بیشتر می‌کنه",True)+\
       row(ic_thy,"قرص تیروئید","حداقل ۴ ساعت با آهن فاصله داشته باشه",False)
html=f'''<html dir="rtl"><head><meta charset="utf-8"><style>
@page{{size:1080px 1350px;margin:0}} html,body{{margin:0}}
.f{{width:1080px;height:1350px;position:relative;overflow:hidden;background:{PINK};font-family:Vazirmatn}}
.top{{position:absolute;top:0;left:0;right:0;height:420px;background:{OX}}}
.h{{position:absolute;top:95px;right:80px;left:420px;text-align:right}}
.h p{{margin:0}}
.d{{font-family:Lalezar;color:{WHITE};font-size:104px;line-height:1.2}}
.k{{font-family:Lalezar;color:{TEAL};font-size:46px;margin-bottom:6px!important}}
.list{{position:absolute;top:470px;right:70px;left:70px}}
.row{{display:flex;align-items:center;background:{WHITE};border-radius:28px;padding:18px 26px;margin-bottom:22px;border:3px solid #ead0ca}}
.ic{{width:110px;height:110px;flex:none}}
.tx{{flex:1;padding:0 26px}}
.t{{font-family:Lalezar;font-size:50px;color:{OX};line-height:1.3}}
.s{{font-size:33px;color:#5b3a3d;line-height:1.5}}
.mk{{flex:none;width:70px;text-align:center}}
.foot{{position:absolute;bottom:52px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:center}}
.w{{font-family:Lalezar;font-size:44px;color:{RED}}}
.hd{{font-weight:bold;font-size:30px;color:{OX};direction:ltr}}
</style></head><body><div class="f">
<div class="top"></div>
<svg width="1080" height="420" style="position:absolute;top:0;left:0"><circle cx="190" cy="210" r="170" fill="{RED}" opacity=".35"/>{capsule(200,215,1.15,-28)}</svg>
<div class="h"><p class="k">نکته‌های داروساز</p><p class="d">قرص آهن رو<br>درست بخور</p></div>
<div class="list">{rows}</div>
<div style="position:absolute;bottom:50px;right:80px" class="w">اول آزمایش، بعد آهن</div><div style="position:absolute;bottom:60px;left:80px" class="hd">@dr.azadehpharma</div>
</div></body></html>'''
HTML(string=html).write_pdf("post_iron.pdf")
