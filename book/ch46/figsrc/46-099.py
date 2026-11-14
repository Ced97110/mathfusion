import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cp(cx,cy,R,n,k):
    a=math.radians(90-360*k/n); return (cx+R*math.cos(a), cy+R*math.sin(a))
def sh(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); return (p[0]+dx/L*d,p[1]+dy/L*d),(q[0]-dx/L*d,q[1]-dy/L*d)

fig,ax=canvas(80)
box(ax,28,64,32,10,'sujet',label=r'$G=\langle a\rangle$',size='l')
arrow(ax,(36,64),(22,52),'varie'); arrow(ax,(52,64),(66,52),'varie')
text(ax,20,56,'ordre infini','varie','s',ha='right'); text(ax,68,56,'ordre $r$','varie','s',ha='left')
f=numberline(ax,6,38,38,-3,3,labels=False,arrow_right=False)
for v in range(-3,4): disc(ax,f(v),38,1.3,'sujet')
text(ax,22,28,r'$\mathbb{Z}$','sujet','l')
cx,cy,R=66,36,10
for k in range(8):
    p=cp(cx,cy,R,8,k); disc(ax,p[0],p[1],1.5,'autre')
text(ax,66,16,r'$\mathbb{Z}/r\mathbb{Z}$','autre','l')
text(ax,44,5,'une copie de l’un des deux','resultat','m')
save(fig,'46-099')
