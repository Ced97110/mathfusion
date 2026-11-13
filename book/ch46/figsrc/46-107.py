import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cp(cx,cy,R,n,k):
    a=math.radians(90-360*k/n); return (cx+R*math.cos(a), cy+R*math.sin(a))
def sh(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); return (p[0]+dx/L*d,p[1]+dy/L*d),(q[0]-dx/L*d,q[1]-dy/L*d)

fig,ax=canvas(70)
xs=[16,44,72]
for x,(h,e) in zip(xs,[('0',r'$a^0=e$'),('4',r'$a^1$'),('8',r'$a^2$')]):
    box(ax,x-8,34,16,10,'sujet',label=h,size='l'); text(ax,x,28,e,'sujet','s')
arrow(ax,(xs[0],46),(xs[2],46),'limite',curve=-0.35,both=True)
text(ax,44,60,'égaux ?','limite','m')
text(ax,44,16,r'$a^2=8$, pas $e$ : non','limite','m')
text(ax,44,6,'trois puissances distinctes','resultat','m')
save(fig,'46-107')
