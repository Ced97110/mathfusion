import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def shr(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); ux,uy=dx/L,dy/L
    return (p[0]+ux*d,p[1]+uy*d),(q[0]-ux*d,q[1]-uy*d)
def link(ax,p,q,nr,role="varie",both=False,lw=1.0,curve=0.0):
    a,b=shr(p,q,nr+0.6); arrow(ax,a,b,role,lw=lw,curve=curve,both=both)
def ring(ax,cx,cy,r,labs,role,nr=3.0,start=90):
    n=len(labs); pts=[(cx+r*math.cos(math.radians(start-360*i/n)),cy+r*math.sin(math.radians(start-360*i/n))) for i in range(n)]
    for i in range(n): link(ax,pts[i],pts[(i+1)%n],nr,"varie")
    for p,l in zip(pts,labs): disc(ax,p[0],p[1],nr,role,label=l)
    return pts
fig,ax=canvas(66)
ring(ax,22,38,11,['1','2','3','4'],'sujet')
for (a,b,yy) in [('1','2',48),('3','4',28)]:
    disc(ax,54,yy,3,'autre',label=a); disc(ax,70,yy,3,'autre',label=b)
    arrow(ax,(57.6,yy),(66.4,yy),'varie',both=True)
text(ax,22,18,'un cycle de 4','sujet','s'); text(ax,62,18,'deux cycles de 2','autre','s')
text(ax,43,38,r'$\neq$','limite','xl'); text(ax,44,5,'pas conjuguées','limite','m')
save(fig,'49-194')
