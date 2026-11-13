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
fig,ax=canvas(84)
u=7
text(ax,44,79,'chaque ligne : total 4','encre','m')
rows=[[1,1,1,1],[2,1,1],[2,2],[3,1],[4]]
for n,r in enumerate(rows):
    y=62-n*10; text(ax,4,y+3,' + '.join(map(str,r)),'sujet','m',ha='left')
    x=40
    for v in r:
        box(ax,x,y,v*u-0.8,6,'sujet',r=0.4); x+=v*u
y=4
for k,r in enumerate([[1,3],[3,1]]):
    x0=12 if k==0 else 52; x=x0
    for v in r:
        box(ax,x,y,v*u-0.8,6,'autre',label=str(v),size='s',r=0.4); x+=v*u
text(ax,44,y+3,'=','resultat','xl')
text(ax,44,y+13,'l’ordre ne compte pas','resultat','s')
save(fig,'49-198')
