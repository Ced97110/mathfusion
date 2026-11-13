import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(cx,cy,R,d): return (cx+R*math.cos(math.radians(d)), cy+R*math.sin(math.radians(d)))
def uc(ax,cx,cy,R,e=4):
    disc(ax,cx,cy,R,"fixe",fill=False)
    line(ax,[(cx-R-e,cy),(cx+R+e,cy)],"fixe",lw=0.6); line(ax,[(cx,cy-R-e),(cx,cy+R+e)],"fixe",lw=0.6)

fig,ax=canvas(74); cx,cy,R=44,38,22; uc(ax,cx,cy,R)
for d,role,lab in [(30,"sujet",r"$(c,\ a)$"),(150,"varie",r"$(-c,\ a)$"),(210,"varie",r"$(-c,\ -a)$"),(330,"varie",r"$(c,\ -a)$")]:
    x,y=pt(cx,cy,R,d); line(ax,[(cx,cy),(x,y)],role,lw=0.7,dash=True); disc(ax,x,y,1.4,role)
    s=1 if x>cx else -1
    text(ax,x+2.6*s,y+(3.5 if y>cy else -3.5),lab+"\n"+f"{d}°",role,"m",ha="left" if s>0 else "right")
text(ax,44,8,r"$a=0{,}5$ ;  $c\approx0{,}866$","encre","m")
save(fig,"28-129")
