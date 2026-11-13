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
text(ax,44,58,r'$\sum_{g\in G}$','sujet','xl')
text(ax,44,47,r'un terme par élément de $G$','sujet','s')
text(ax,9,41,r'$G$ a 4 éléments','fixe','s',ha='left')
for i,v in enumerate([5,3,1,3]): box(ax,9+i*9,29,7,8,'sujet',label=str(v),size='s',r=0.5)
text(ax,9,23,r'$G$ a 8 éléments','fixe','s',ha='left')
for i in range(8): box(ax,9+i*9,11,7,8,'sujet',r=0.5)
text(ax,44,4,'même écriture pour les deux','resultat','s')
save(fig,'49-207')
