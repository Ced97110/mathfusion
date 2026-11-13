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
for x0,nm,moves in [(4,'e : 2 points fixes',False),(48,'a : 1 point fixe',True)]:
    text(ax,x0+18,60,nm,'sujet','m')
    for yy,l in [(48,'P'),(30,'Q')]:
        disc(ax,x0+4,yy,3.5,'sujet',label=l); disc(ax,x0+32,yy,3.5,'sujet',label=l)
    arrow(ax,(x0+8.1,48),(x0+27.9,48),'resultat')
    if moves: arrow(ax,(x0+7.9,30.6),(x0+28.1,47.4),'varie')
    else: arrow(ax,(x0+8.1,30),(x0+27.9,30),'resultat')
text(ax,44,16,r'$(2+1)\,/\,2 = 1{,}5$','limite','l')
text(ax,44,6,'pas entier : pas un groupe','limite','s')
save(fig,'49-203')
