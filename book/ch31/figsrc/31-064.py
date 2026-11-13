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

fig,ax=canvas(92)
text(ax,44,87,r'$\theta = 120^\circ$','encre','l')
rows=[(66,('cos','−0,5',-0.5),('sec','−2',-2)),(42,('sin','0,8660',0.8660),('cosec','1,1547',1.1547)),(18,('tan','−1,7321',-1.7321),('cotan','−0,5774',-0.5774))]
for y,a,b in rows:
    f=numberline(ax,8,80,y,-2.5,2.5,step=0.5,labels=False,arrow_right=False)
    text(ax,f(0),y-3.6,'0','fixe','s')
    dot(ax,(f(a[2]),y),'autre',1.4); dot(ax,(f(b[2]),y),'sujet',1.4)
    text(ax,f(a[2]),y+5,a[0]+' '+a[1],'autre','s')
    text(ax,f(b[2]),y-8,b[0]+' '+b[1],'sujet','s')
text(ax,10,3,'négatif','fixe','s',ha='left'); text(ax,78,3,'positif','fixe','s',ha='right')
save(fig,'31-064')
