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
fig,ax=canvas(64)
text(ax,20,58,'256 colorations','fixe','m')
for i in range(256): box(ax,4+(i%16)*2,10+(i//16)*2,1.6,1.6,'fixe',r=0.2,lw=0.3)
box(ax,46,44,40,10,'autre',label='groupe de 8 symétries',size='s')
arrow(ax,(66,43),(66,28),'varie'); text(ax,68,35.5,'sans lister','varie','s',ha='left')
box(ax,46,16,40,10,'resultat',label='55 orbites',size='l')
save(fig,'49-202')
