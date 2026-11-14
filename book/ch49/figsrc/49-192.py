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
xs=[12,33,55,76]; y=34
for x,l,r in zip(xs,['4','1','2','2'],['autre','sujet','sujet','resultat']): disc(ax,x,y,5,r,label=l,size='l')
rl=['varie','sujet','varie']; lb=[r'$\tau^{-1}$',r'$\sigma$',r'$\tau$']
for i in range(3):
    link(ax,(xs[i],y),(xs[i+1],y),5,rl[i],lw=2.4 if i==0 else 1.0)
    text(ax,(xs[i]+xs[i+1])/2,y+5.5,lb[i],rl[i],'l')
text(ax,44,50,'on suit le point 4','encre','l')
text(ax,12,23,'départ','autre','s'); text(ax,76,23,'arrivée','resultat','s')
text(ax,44,23,r'$\sigma$ : cycle (1 2 3)','sujet','s')
line(ax,[(22.5,31),(22.5,16.5)],'varie',dash=True); text(ax,22.5,13.5,'étape décisive','varie','s')
save(fig,'49-192')
