import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
import math
cx,cy,R=18,34,12
pts=[(cx+R*math.cos(math.radians(a)),cy+R*math.sin(math.radians(a))) for a in (90,330,210)]
for i,p in enumerate(pts): disc(ax,p[0],p[1],4,'varie',label=str(i+1))
def edge(p,q,r=4.4):
    d=math.hypot(q[0]-p[0],q[1]-p[1]); ux,uy=(q[0]-p[0])/d,(q[1]-p[1])/d
    return (p[0]+ux*r,p[1]+uy*r),(q[0]-ux*r,q[1]-uy*r)
for i in range(3):
    a,b=edge(pts[i],pts[(i+1)%3]); arrow(ax,a,b,'varie',curve=-0.2)
text(ax,18,12,'ordre circulaire','varie','m')
fs=[('coordonnée 1',r'$u_2v_3-u_3v_2$'),('coordonnée 2',r'$u_3v_1-u_1v_3$'),('coordonnée 3',r'$u_1v_2-u_2v_1$')]
y=48
for n,f in fs:
    text(ax,62,y+11,n,'fixe','s')
    box(ax,38,y,48,8,'sujet',label=f)
    y-=16
text(ax,44,3.5,r'$(1,0,0)\times(0,1,0)=(0,0,1)$','resultat','s')
text(ax,44,60,'','fixe','s') if False else None
save(fig,'78-121')
