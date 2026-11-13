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

fig,ax=canvas(74)
box(ax,2,58,22,12,'fixe',label=r'$0{,}8660$')
arrow(ax,(26,64),(42,64),'varie')
text(ax,34,60.2,'retourner','varie','s')
box(ax,44,58,42,12,'sujet',label=r'$1/0{,}8660 = 1{,}1547$',size='s')
box(ax,2,34,32,12,'fixe',label=r'$4\ /\ 0{,}8660$')
box(ax,38,36,32.33,8,'resultat',label='4,6189',size='m')
box(ax,2,12,32,12,'sujet',label=r'$4\times 1{,}1547$')
box(ax,38,14,32.33,8,'resultat',label='4,6188',size='m')
text(ax,54,29,r'$\approx$','encre','l')
save(fig,'31-049')
