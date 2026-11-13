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
names=['(1)','(1 3)','(1 3)(2 5)','(2 5)']; fx=[5,3,1,3]; base=8; u=7
for i,(n,f) in enumerate(zip(names,fx)):
    cx=12.5+i*19; box(ax,cx-6,base,12,f*u,'sujet',r=0.8)
    text(ax,cx,base+f*u+2.5,str(f),'sujet','m'); text(ax,cx,3,n,'sujet','s')
line(ax,[(3,base+3*u),(85,base+3*u)],'resultat',lw=1.2,dash=True)
text(ax,50.5,base+6*u+2,'moyenne 3 = k','resultat','m')
save(fig,'49-206')
