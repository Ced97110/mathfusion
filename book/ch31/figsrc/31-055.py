import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def quad(ax, xo, yo, R, deg, ext=1.05):
    pts = [(xo + R*math.cos(math.radians(a)), yo + R*math.sin(math.radians(a))) for a in range(0, 91, 3)]
    line(ax, pts, 'fixe', lw=0.8)
    line(ax, [(xo - 2, yo), (xo + R*ext, yo)], 'fixe', lw=0.6)
    line(ax, [(xo, yo - 2), (xo, yo + R*ext)], 'fixe', lw=0.6)
    t = math.radians(deg)
    return (xo + R*math.cos(t), yo + R*math.sin(t))

def dot(ax, p, role='encre', r=0.8):
    ax.add_patch(Circle(p, r, fc=COL[role], ec=COL[role], zorder=6))

def tharc(ax, xo, yo, deg, r=9, role='varie'):
    line(ax, [(xo + r*math.cos(math.radians(deg*i/20)), yo + r*math.sin(math.radians(deg*i/20))) for i in range(21)], role, lw=1.0)

def tlab(ax, xo, yo, deg, r=13, s=r'$\theta$'):
    a = math.radians(deg/2); text(ax, xo + r*math.cos(a), yo + r*math.sin(a), s, 'varie', 'm')

fig,ax=canvas(96)
yA,yB,yN=76,18,47
text(ax,44,89,r'$\sin^2\theta$ : $\theta = 2$','sujet','m')
for x,l in [(3,'2'),(34,'0,9093'),(65,'0,8268')]:
    box(ax,x,yA-5,20,10,'resultat' if l=='0,8268' else 'sujet',label=l)
arrow(ax,(24,yA),(33,yA),'fixe'); text(ax,28.5,yA+4.5,'sin','fixe','s')
arrow(ax,(55,yA),(64,yA),'varie'); text(ax,59.5,yA+4.5,'carré','varie','s')
text(ax,44,31,r'$\sin(\theta^2)$ : $\theta = 2$','limite','m')
for x,l in [(65,'2'),(34,'4'),(3,'−0,7568')]:
    box(ax,x,yB-5,20,10,'limite' if l!='2' else 'fixe',label=l)
arrow(ax,(64,yB),(55,yB),'varie'); text(ax,59.5,yB+4.5,'carré','varie','s')
arrow(ax,(33,yB),(24,yB),'fixe'); text(ax,28.5,yB+4.5,'sin','fixe','s')
f=numberline(ax,8,76,yN,-1,1,labels=False,arrow_right=False)
text(ax,f(0),yN-4,'0','fixe','s')
dot(ax,(f(0.8268),yN),'resultat',1.4); dot(ax,(f(-0.7568),yN),'limite',1.4)
line(ax,[(74.5,yA-5),(f(0.8268),yN+1.5)],'resultat',dash=True)
line(ax,[(13,yB+5),(f(-0.7568),yN-1.5)],'limite',dash=True)
save(fig,'31-055')
