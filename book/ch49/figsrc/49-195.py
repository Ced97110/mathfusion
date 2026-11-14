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
fig,ax=canvas(80)
text(ax,18,75,'permutation','fixe','s'); text(ax,70,75,'forme','sujet','s')
box(ax,3,62,30,8,'fixe',label='(1 2)(3 4)',size='m'); box(ax,3,42,30,8,'fixe',label='(1 3)(2 4)',size='m')
box(ax,55,52,30,8,'sujet',label='2 + 2',size='m')
arrow(ax,(34,66),(54,58),'varie'); arrow(ax,(34,46),(54,54),'varie')
text(ax,44,34,'deux permutations, une forme','resultat','s')
box(ax,3,14,30,8,'fixe',label='(1 2 3)',size='m'); box(ax,55,14,30,8,'sujet',label='3 + 1',size='m')
arrow(ax,(34,18),(54,18),'varie')
text(ax,44,6,'le 4 compte : cycle de 1','sujet','s')
save(fig,'49-195')
