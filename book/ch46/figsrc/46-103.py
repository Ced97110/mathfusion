import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cp(cx,cy,R,n,k):
    a=math.radians(90-360*k/n); return (cx+R*math.cos(a), cy+R*math.sin(a))
def sh(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); return (p[0]+dx/L*d,p[1]+dy/L*d),(q[0]-dx/L*d,q[1]-dy/L*d)

fig,ax=canvas(85)
text(ax,16,78,'départ','sujet','m'); text(ax,16,72,r'$\varphi(n)=a^n$','sujet','s')
text(ax,72,78,'arrivée','resultat','m'); text(ax,72,72,r'$\langle a\rangle$','resultat','s')
ys={1:58,4:44,7:30}
for n,y in ys.items(): disc(ax,16,y,4,'sujet',label=str(n),size='s')
tg={0:58,4:44,8:30}
for v,y in tg.items(): disc(ax,72,y,4,'resultat' if v==4 else 'fixe',label=str(v),size='s')
for n,y in ys.items():
    p,q=sh((16,y),(72,44),5); arrow(ax,p,q,'varie',lw=0.8)
text(ax,44,19,'étape clé : la division','varie','m')
text(ax,44,11,r'$7=2\times 3+1$ : reste 1','varie','s')
text(ax,44,4,'même image : 4','resultat','s')
save(fig,'46-103')
