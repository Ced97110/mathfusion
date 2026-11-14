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

fig,ax=canvas(66)
text(ax,18,58,r'$(\sin\theta)^2$','fixe','l')
arrow(ax,(32,58),(54,58),'varie'); text(ax,43,62,'écriture courte','varie','s')
text(ax,68,58,r'$\sin^2\theta$','sujet','l')
text(ax,44,43,r'$\sin^2\theta + \cos^2\theta$','sujet','l')
text(ax,44,30,r'à 35°',"encre",'s')
u=76; a=0.3290*u; b=0.6710*u
box(ax,6,8,a,10,'sujet',label='0,3290',size='s'); box(ax,6+a,8,b,10,'autre',label='0,6710',size='s')
text(ax,6+a/2,21.5,r'$\sin^2\theta$','sujet','s'); text(ax,6+a+b/2,21.5,r'$\cos^2\theta$','autre','s')
save(fig,'31-057')
