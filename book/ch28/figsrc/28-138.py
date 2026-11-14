import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(cx,cy,R,d): return (cx+R*math.cos(math.radians(d)), cy+R*math.sin(math.radians(d)))
def uc(ax,cx,cy,R,e=4):
    disc(ax,cx,cy,R,"fixe",fill=False)
    line(ax,[(cx-R-e,cy),(cx+R+e,cy)],"fixe",lw=0.6); line(ax,[(cx,cy-R-e),(cx,cy+R+e)],"fixe",lw=0.6)
fig,ax=canvas(64); ox,oy,R=10,12,56
A=(ox+R,oy); T=(ox+R,oy+R*math.tan(math.radians(30))); P=pt(ox,oy,R,30); N=(P[0],oy); O=(ox,oy)
poly(ax,[O,A,T],"resultat"); poly(ax,[O,N,P],"autre")
line(ax,[(6,oy),(A[0]+10,oy)],"fixe",lw=0.6)
line(ax,[(A[0],oy-4),(A[0],54)],"sujet",lw=1.0)
line(ax,[A,T],"resultat",lw=2.0); line(ax,[O,T],"varie",lw=1.2)
line(ax,[pt(ox,oy,R,d) for d in range(0,41,2)],"fixe",lw=0.7)
for p,l,r in [(P,"P","autre"),(T,"T","resultat"),(A,"A","sujet")]: disc(ax,*p,1.2,r)
text(ax,6,8,r"$O$","encre"); text(ax,A[0],8,r"$A$","sujet"); text(ax,N[0],8,r"$N$","autre")
text(ax,P[0]-3,P[1]+3.5,r"$P$","autre"); text(ax,T[0]+3,T[1]+3,r"$T$","resultat")
text(ax,A[0]+3,(oy+T[1])/2,r"$\tan\theta$","resultat",ha="left")
text(ax,24,15.5,r"$\theta$","varie"); text(ax,A[0],58,r"$x=1$","sujet")
save(fig,"28-138")
