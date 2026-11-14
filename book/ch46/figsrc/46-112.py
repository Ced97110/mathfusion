import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cp(cx,cy,R,n,k):
    a=math.radians(90-360*k/n); return (cx+R*math.cos(a), cy+R*math.sin(a))
def sh(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); return (p[0]+dx/L*d,p[1]+dy/L*d),(q[0]-dx/L*d,q[1]-dy/L*d)

fig,ax=canvas(80)
text(ax,43.5,66,'2','sujet','xl',ha='right'); text(ax,44.5,66,r'$\mathbb{Z}$','varie','xl',ha='left')
arrow(ax,(40,60),(26,50),'sujet'); arrow(ax,(50,60),(64,50),'varie')
text(ax,26,45,'le facteur','sujet','s'); text(ax,66,45,'un entier relatif','varie','s')
f=numberline(ax,8,64,20,-4,6,labels=True,every=2,arrow_right=True,size='s')
for v in range(-4,7):
    if v%2==0: disc(ax,f(v),20,1.5,'sujet')
text(ax,44,6,'les multiples de 2','resultat','m')
save(fig,'46-112')
