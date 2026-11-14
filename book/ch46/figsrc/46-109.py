import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cp(cx,cy,R,n,k):
    a=math.radians(90-360*k/n); return (cx+R*math.cos(a), cy+R*math.sin(a))
def sh(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); return (p[0]+dx/L*d,p[1]+dy/L*d),(q[0]-dx/L*d,q[1]-dy/L*d)

fig,ax=canvas(65)
f=numberline(ax,8,70,32,0,12,labels=True,every=3,arrow_right=False,size='m')
for v in range(13):
    if v%3==0: disc(ax,f(v),32,1.8,'resultat' if v else 'fixe')
    else: disc(ax,f(v),32,0.8,'fixe')
for v in (0,3,6,9):
    p,q=sh((f(v),35),(f(v+3),35),0.8); arrow(ax,p,q,'varie',lw=0.8,curve=-0.5)
text(ax,f(1.5),46,r'$r=3$','varie','m')
text(ax,44,58,r'$a^m=e$ seulement ici','resultat','m')
text(ax,44,14,r'$m$ : 3, 6, 9, 12','resultat','s')
text(ax,44,6,r'$r$ divise $m$','sujet','m')
save(fig,'46-109')
