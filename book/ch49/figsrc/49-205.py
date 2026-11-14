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
fig,ax=canvas(62)
box(ax,6,28,76,22,'fixe',fill=False,dash=True)
text(ax,44,56,r'$S/G$ : ensemble des orbites','fixe','m')
for i in range(6): disc(ax,15+i*11.6,39,4,'sujet')
text(ax,44,32,'un disque = une orbite','sujet','s')
brace(ax,6,82,25,'varie',label='6 éléments',depth=2)
box(ax,20,2,48,9,'resultat',label=r'$k = |S/G| = 6$',size='m')
save(fig,'49-205')
