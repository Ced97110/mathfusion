import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(cx,cy,R,d): return (cx+R*math.cos(math.radians(d)), cy+R*math.sin(math.radians(d)))
def uc(ax,cx,cy,R,e=4):
    disc(ax,cx,cy,R,"fixe",fill=False)
    line(ax,[(cx-R-e,cy),(cx+R+e,cy)],"fixe",lw=0.6); line(ax,[(cx,cy-R-e),(cx,cy+R+e)],"fixe",lw=0.6)
fig,ax=canvas(70); cx,cy,R=44,36,22; uc(ax,cx,cy,R)
line(ax,[(cx,cy-R-4),(cx,cy+R+4)],"fixe",lw=0.6,dash=True)
disc(ax,cx+R,cy,1.6,"sujet"); disc(ax,cx-R,cy,1.6,"autre")
text(ax,cx+R+3,cy+3.5,"0°","sujet",ha="left"); text(ax,cx+R+3,cy-3.5,"(1, 0)","sujet",ha="left")
text(ax,cx-R-3,cy+3.5,"180°","autre",ha="right"); text(ax,cx-R-3,cy-3.5,"(−1, 0)","autre",ha="right")
text(ax,44,66,r"$\sin(180°-\theta)=\sin\theta$","encre","m")
text(ax,44,8,"sin 180° = sin 0° = 0","resultat","l")
save(fig,"28-140")
