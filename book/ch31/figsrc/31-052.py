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

fig,ax=canvas(72)
text(ax,14,67,'angle','sujet','m'); text(ax,74,67,'nombre','autre','m')
for yc,a,n in [(51,'30°','0,5'),(19,'60°','0,8660')]:
    box(ax,3,yc-7,22,14,'sujet',label=a,size='l')
    box(ax,63,yc-7,22,14,'autre',label=n,size='l')
    arrow(ax,(26,yc+3),(62,yc+3),'fixe')
    text(ax,44,yc+7.5,'sin','fixe','m')
    arrow(ax,(62,yc-3),(26,yc-3),'sujet')
    text(ax,44,yc-7.5,r'arcsin ($\sin^{-1}$)','sujet','s')
save(fig,'31-052')
