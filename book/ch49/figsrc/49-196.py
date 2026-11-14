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
fig,ax=canvas(52)
cs=[16,44,72]; names=['(1 2)','(1 3)','(2 3)']
for cx,nm,(i,j) in zip(cs,names,[(0,1),(0,2),(1,2)]):
    P=[(cx,36),(cx-8,24),(cx+8,24)]
    link(ax,P[i],P[j],3,'varie',both=True)
    for k,p in enumerate(P): disc(ax,p[0],p[1],3,'sujet' if k in (i,j) else 'fixe',label=str(k+1))
    text(ax,cx,45,nm,'sujet','m')
brace(ax,5,83,16,'sujet',label='même forme : même classe',depth=2)
save(fig,'49-196')
