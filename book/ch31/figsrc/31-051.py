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

fig,ax=canvas(64)
text(ax,22,56,r'$\sin^{-1}(0{,}5)$','sujet','l')
text(ax,44,56,r'$\neq$','encre','l')
text(ax,66,56,r'$(\sin 30^\circ)^{-1}$','autre','l')
arrow(ax,(22,51),(22,43),'sujet'); arrow(ax,(66,51),(66,43),'autre')
O=(8,24); L=26
line(ax,[O,(O[0]+L,O[1])],'fixe',lw=1.0)
line(ax,[O,(O[0]+L*math.cos(math.radians(30)),O[1]+L*math.sin(math.radians(30)))],'sujet',lw=1.6)
tharc(ax,O[0],O[1],30,r=12,role='sujet')
text(ax,O[0]+17.5,O[1]+4,'30°','sujet','m')
text(ax,22,10,'un angle','sujet','m')
f=numberline(ax,48,78,26,0,3,arrow_right=False)
line(ax,[(f(0),26),(f(2),26)],'autre',lw=2.2)
dot(ax,(f(2),26),'autre',1.3)
text(ax,66,10,'un nombre','autre','m')
save(fig,'31-051')
