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
fig,ax=canvas(56)
text(ax,44,50,r'conjugué de $\sigma$ par $\tau$','sujet','m')
xs=[22,44,66]; syms=[r'$\tau$',r'$\sigma$',r'$\tau^{-1}$']; rl=['varie','sujet','varie']; ords=['agit en 3e','agit en 2e','agit en 1er']
for x,s,r,o in zip(xs,syms,rl,ords):
    box(ax,x-8,26,16,14,r,label=s,size='xl'); text(ax,x,19,o,r,'s')
arrow(ax,(57,33),(53,33),'fixe'); arrow(ax,(35,33),(31,33),'fixe')
text(ax,44,8,'on lit de droite à gauche','fixe','s')
save(fig,'49-197')
