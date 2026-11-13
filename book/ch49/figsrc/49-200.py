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
text(ax,4,56,'forme','fixe','s',ha='left'); text(ax,36,56,'éléments de la classe','fixe','s',ha='left')
rows=[('1+1+1+1',1),('2+1+1',6),('2+2',3),('3+1',8),('4',6)]
for n,(f,c) in enumerate(rows):
    y=43-n*8; text(ax,4,y+2.5,f,'sujet','m',ha='left')
    for i in range(c): box(ax,36+i*3,y,2.6,5,'sujet',r=0.3,lw=0.5)
    text(ax,36+c*3+1.5,y+2.5,str(c),'sujet','m',ha='left')
text(ax,44,5,'24 = 1 + 6 + 3 + 8 + 6','resultat','l')
save(fig,'49-200')
