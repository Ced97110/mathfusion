import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(cx,cy,R,d): return (cx+R*math.cos(math.radians(d)), cy+R*math.sin(math.radians(d)))
def uc(ax,cx,cy,R,e=4):
    disc(ax,cx,cy,R,"fixe",fill=False)
    line(ax,[(cx-R-e,cy),(cx+R+e,cy)],"fixe",lw=0.6); line(ax,[(cx,cy-R-e),(cx,cy+R+e)],"fixe",lw=0.6)
fig,ax=canvas(74); cx,cy,R=44,34,24; uc(ax,cx,cy,R)
line(ax,[(cx,cy-R),(cx,cy+R+4)],"varie",lw=1.6)
x,y=cx,cy+R; disc(ax,x,y,1.5,"sujet")
text(ax,x+3,y+4,r"$P=(0,\ 1)$","sujet",ha="left")
text(ax,24,52,r"$x<0$","fixe"); text(ax,64,52,r"$x>0$","fixe")
text(ax,cx+2,cy-6,r"$x=0$","varie",ha="left")
text(ax,44,6,r"0 n’a ni $+$ ni $-$","encre","m")
save(fig,"28-134")
