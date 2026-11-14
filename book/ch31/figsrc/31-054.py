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

fig,ax=canvas(62)
S=40; x0,y0=4,8
box(ax,x0,y0,S,S,'fixe',r=0.01)
box(ax,x0,y0,S/2,S/2,'sujet',label='0,25',size='m',r=0.01)
text(ax,x0+S/4,y0-3.2,'0,5','sujet','s')
text(ax,x0-2.2,y0+S/4,'0,5','sujet','s',rot=90)
text(ax,x0+S/2+S/4,y0+S/2+S/4,'1 × 1','fixe','m')
text(ax,68,46,r'$\sin^2 30^\circ$','sujet','l')
text(ax,68,38,r'$= (\sin 30^\circ)^2$','sujet','m')
text(ax,68,30,r'$= 0{,}5\times 0{,}5$','sujet','m')
text(ax,68,22,r'$= 0{,}25$','resultat','l')
text(ax,68,13,'le carré du sinus','encre','s')
save(fig,'31-054')
