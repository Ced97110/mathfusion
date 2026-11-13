import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(cx,cy,R,d): return (cx+R*math.cos(math.radians(d)), cy+R*math.sin(math.radians(d)))
def uc(ax,cx,cy,R,e=4):
    disc(ax,cx,cy,R,"fixe",fill=False)
    line(ax,[(cx-R-e,cy),(cx+R+e,cy)],"fixe",lw=0.6); line(ax,[(cx,cy-R-e),(cx,cy+R+e)],"fixe",lw=0.6)
fig,ax=canvas(78); cx,cy,R=34,50,22; uc(ax,cx,cy,R,3)
th=50; arcp=[pt(cx,cy,R,d) for d in range(0,th+1)]
line(ax,arcp,"varie",lw=2.0)
P=pt(cx,cy,R,th); A=(cx+R,cy); line(ax,[(cx,cy),P],"sujet",lw=0.8); line(ax,[(cx,cy),A],"sujet",lw=0.8)
disc(ax,*A,1.3,"sujet"); disc(ax,*P,1.3,"sujet")
text(ax,A[0]+3,A[1]+3,r"$A$","sujet"); text(ax,P[0]+3,P[1]+3,r"$P$","sujet"); text(ax,cx-3,cy-3,r"$O$","encre")
text(ax,cx+R/2,cy-3,"1","sujet","m"); text(ax,cx+9,cy+3.5,r"$\theta$","varie")
L=R*math.radians(th); y0=20
line(ax,[A,(A[0],y0)],"fixe",lw=0.6,dash=True)
line(ax,[(A[0],y0),(A[0]+L,y0)],"varie",lw=2.0)
for x in (A[0],A[0]+L): line(ax,[(x,y0-1.5),(x,y0+1.5)],"varie",lw=0.9)
text(ax,A[0]+L/2,14,"longueur de l’arc","varie","m")
text(ax,44,5,"tour entier ≈ 6,28","encre","m")
save(fig,"28-141")
