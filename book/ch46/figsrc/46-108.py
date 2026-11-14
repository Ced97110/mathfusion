import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cp(cx,cy,R,n,k):
    a=math.radians(90-360*k/n); return (cx+R*math.cos(a), cy+R*math.sin(a))
def sh(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); return (p[0]+dx/L*d,p[1]+dy/L*d),(q[0]-dx/L*d,q[1]-dy/L*d)

fig,ax=canvas(72)
f=numberline(ax,8,70,36,0,8,labels=True,arrow_right=False,size='m')
rl={0:'fixe',1:'sujet',2:'varie'}
for v in range(9): disc(ax,f(v),36,1.6,rl[v%3])
arrow(ax,(f(1),39),(f(7),39),'resultat',curve=-0.35,both=True)
text(ax,f(4),56,'écart 6 : multiple de 3','resultat','s')
arrow(ax,(f(1),28.5),(f(5),28.5),'limite',curve=0.35,both=True)
text(ax,f(3),14,'écart 4 : non','limite','s')
text(ax,4,6,'heure 0','fixe','s',ha='left'); text(ax,44,6,'heure 4','sujet','s'); text(ax,84,6,'heure 8','varie','s',ha='right')
save(fig,'46-108')
