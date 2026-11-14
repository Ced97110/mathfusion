import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cp(cx,cy,R,n,k):
    a=math.radians(90-360*k/n); return (cx+R*math.cos(a), cy+R*math.sin(a))
def sh(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); return (p[0]+dx/L*d,p[1]+dy/L*d),(q[0]-dx/L*d,q[1]-dy/L*d)

fig,ax=canvas(80)
xs=[18,35,52,69]; top=[-1,0,1,2]; bot=['1/2','1','2','4']
for x,t,b in zip(xs,top,bot):
    disc(ax,x,62,4.2,'sujet',label=str(t),size='s'); disc(ax,x,22,4.2,'autre',label=b,size='s')
    arrow(ax,(x,57),(x,27),'resultat')
text(ax,23,42,r'$\varphi$','resultat','m')
arrow(ax,(xs[1]+1,67.5),(xs[2]-1,67.5),'varie',curve=-0.4); text(ax,(xs[1]+xs[2])/2,75,'+1','varie','s')
arrow(ax,(xs[1]+1,16.5),(xs[2]-1,16.5),'varie',curve=0.4); text(ax,(xs[1]+xs[2])/2,9,r'$\times 2$','varie','s')
text(ax,4,78,r'$\mathbb{Z}$ (addition)','sujet','s',ha='left')
text(ax,4,3,'puissances de 2 (produit)','autre','s',ha='left')
save(fig,'46-100')
