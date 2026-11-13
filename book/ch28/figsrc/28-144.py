import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(cx,cy,R,d): return (cx+R*math.cos(math.radians(d)), cy+R*math.sin(math.radians(d)))
def uc(ax,cx,cy,R,e=4):
    disc(ax,cx,cy,R,"fixe",fill=False)
    line(ax,[(cx-R-e,cy),(cx+R+e,cy)],"fixe",lw=0.6); line(ax,[(cx,cy-R-e),(cx,cy+R+e)],"fixe",lw=0.6)
fig,ax=canvas(68); cx,cy,R=44,34,22; uc(ax,cx,cy,R)
yy=cy+R/2; line(ax,[(cx-R-2,yy),(cx+R+2,yy)],"resultat",lw=0.8,dash=True)
text(ax,cx,yy+3.5,r"$\sin\theta=\frac{1}{2}$","resultat","m")
for d,role,lab,ha in [(30,"sujet","30°, 390°, …","left"),(150,"varie","150°, 510°, …","right")]:
    x,y=pt(cx,cy,R,d); line(ax,[(cx,cy),(x,y)],role,lw=0.7); disc(ax,x,y,1.5,role)
    text(ax,x+(3 if ha=="left" else -3),y+4,lab,role,"m",ha=ha)
text(ax,44,6,"une infinité d’angles","varie","m")
save(fig,"28-144")
