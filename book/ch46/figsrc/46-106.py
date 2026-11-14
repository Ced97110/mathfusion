import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cp(cx,cy,R,n,k):
    a=math.radians(90-360*k/n); return (cx+R*math.cos(a), cy+R*math.sin(a))
def sh(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); return (p[0]+dx/L*d,p[1]+dy/L*d),(q[0]-dx/L*d,q[1]-dy/L*d)

fig,ax=canvas(75)
f=numberline(ax,10,70,42,0,7,labels=True,arrow_right=False,size='m')
for v in range(8): disc(ax,f(v),42,1.4,'varie' if v>6-1 else 'fixe')
brace(ax,f(0),f(3),46,'fixe',label='tour : 3 pas',down=False)
brace(ax,f(3),f(6),46,'fixe',label='tour : 3 pas',down=False)
brace(ax,f(6),f(7),46,'varie',label='reste 1',down=False)
text(ax,44,68,r'$7=2\times 3+1$','varie','l')
text(ax,44,22,r'$a^7=a^1$ : l’heure 4','resultat','m')
text(ax,44,12,'deux tours, puis un pas','encre','s')
save(fig,'46-106')
