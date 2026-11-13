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
tA=text(ax,30,48,r'$(\sin 30^\circ)$','sujet','xl')
fig.canvas.draw(); r=fig.canvas.get_renderer(); bb=tA.get_window_extent(r)
k=25.4/fig.dpi
x0=bb.x0*k; x1=bb.x1*k
tB=text(ax,x1+0.5,54,r'$^{-1}$','varie','xl',ha='left')
brace(ax,x0,x1,40,'sujet',label=None)
text(ax,(x0+x1)/2,30,r'$\sin 30^\circ = 0{,}5$ en premier','sujet','s')
arrow(ax,(x1+4,44),(x1-1,37.5),'varie',curve=-0.3)
text(ax,64,33,'exposant sur le tout','varie','s')
box(ax,6,6,76,12,'resultat',label=r'$(0{,}5)^{-1} = 1/0{,}5 = 2$ : un nombre')
save(fig,'31-053')
