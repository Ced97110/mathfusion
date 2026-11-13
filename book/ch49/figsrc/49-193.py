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
fig,ax=canvas(60)
cy=36
ring(ax,20,cy,10,['1','2','3'],'sujet'); ring(ax,68,cy,10,['4','2','3'],'autre')
arrow(ax,(35,cy),(53,cy),'varie',lw=1.6)
text(ax,44,cy+4.5,'renommer','varie','s'); text(ax,44,cy-4.5,r'$1\to4$','varie','m')
text(ax,20,15,'3 objets','sujet','m'); text(ax,68,15,'3 objets','autre','m')
text(ax,44,15,'=','resultat','xl')
text(ax,44,5,'même nombre d’objets','resultat','s')
save(fig,'49-193')
