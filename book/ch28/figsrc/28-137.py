import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(cx,cy,R,d): return (cx+R*math.cos(math.radians(d)), cy+R*math.sin(math.radians(d)))
def uc(ax,cx,cy,R,e=4):
    disc(ax,cx,cy,R,"fixe",fill=False)
    line(ax,[(cx-R-e,cy),(cx+R+e,cy)],"fixe",lw=0.6); line(ax,[(cx,cy-R-e),(cx,cy+R+e)],"fixe",lw=0.6)
fig,ax=canvas(72); R=10; cy=38
for cx,d,nm,cnt,role in [(15,4,"sécante","2 points","fixe"),(44,14,"à l’écart","0 point","fixe"),(73,10,"tangente","1 point : A","sujet")]:
    disc(ax,cx,cy,R,"fixe",fill=False)
    line(ax,[(cx+d,cy-16),(cx+d,cy+16)],role,lw=1.3 if role=="sujet" else 0.9)
    text(ax,cx,66,nm,role,"m"); text(ax,cx,14,cnt,role,"m")
    if d==4:
        h=math.sqrt(R*R-d*d)
        for s in (1,-1): disc(ax,cx+d,cy+s*h,1.2,"varie")
    if d==10:
        disc(ax,cx+d,cy,1.4,"varie"); text(ax,cx+d+2.5,cy-3,"A","varie",ha="left")
text(ax,83,58,r"$x=1$","sujet")
save(fig,"28-137")
