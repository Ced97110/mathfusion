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
fig,ax=canvas(72)
names=['(1)','(1 3)','(1 3)(2 5)','(2 5)']; fx=[5,3,1,3]
for i,(n,f) in enumerate(zip(names,fx)):
    x=3+i*21; box(ax,x,52,19,8,'sujet',label=n,size='s')
    arrow(ax,(x+9.5,51.5),(x+9.5,43.5),'varie'); disc(ax,x+9.5,39.5,3.8,'varie',label=str(f),size='m')
text(ax,44,66,'points fixes de chaque élément','sujet','s')
brace(ax,12.5,75.5,34,'varie',label='5 + 3 + 1 + 3 = 12',depth=2)
arrow(ax,(44,22),(44,17),'varie'); text(ax,62,19.5,'divisé par 4 éléments','varie','s')
box(ax,24,5,40,10,'resultat',label=r'$k = 12 \div 4 = 3$',size='m')
save(fig,'49-204')
