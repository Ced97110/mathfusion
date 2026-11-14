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
fig,ax=canvas(76)
text(ax,22,70,'16 colorations','fixe','m')
for i in range(16): disc(ax,8+(i%4)*9,56-(i//4)*9,3,'fixe')
text(ax,66,70,'orbites à trouver','sujet','m')
for k in range(6):
    y=58-k*10; box(ax,50,y,32,7,'sujet',label=f'orbite {k+1}',size='m')
    if k<5: arrow(ax,(66,y-0.2),(66,y-2.8),'varie')
text(ax,66,4,'une orbite à la fois','varie','s')
save(fig,'49-201')
