import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle
def mp(ox, oy, u): return lambda x, y: (ox + x * u, oy + y * u)
def frame(ax, m, x0, x1, y0, y1):
    line(ax, [m(x0, y0), m(x1, y0), m(x1, y1), m(x0, y1), m(x0, y0)], 'fixe', lw=0.5)
    line(ax, [m(x0, 0), m(x1, 0)], 'fixe', lw=0.4); line(ax, [m(0, y0), m(0, y1)], 'fixe', lw=0.4)
def region(ax, m, pts, role): ax.add_patch(Polygon([m(*p) for p in pts], closed=True, ec='none', fc=FILL[role], zorder=1))
def axes(ax, m, x1, y1):
    arrow(ax, m(0, 0), m(x1, 0), 'fixe', lw=0.6); arrow(ax, m(0, 0), m(0, y1), 'fixe', lw=0.6)
UP = [(-3, -2), (2, 3), (-3, 3)]
DOWN = [(-3, -2), (2, 3), (3, 3), (3, -3), (-3, -3)]
fig, ax = canvas(70)
m = mp(34, 34, 9)
region(ax, m, UP, 'sujet'); frame(ax, m, -3, 3, -3, 3)
line(ax, [m(-3, -2), m(2, 3)], 'varie', lw=1.6, dash=True)
disc(ax, *m(1, 2), 1.4, 'limite')
text(ax, 34, 66, r'$y>x+1$', 'sujet', 'l')
text(ax, 77, 60, 'pointillés', 'varie', 's'); arrow(ax, (70, 58.5), (48.5, 56.8), 'varie', lw=0.8)
text(ax, 75, 46, r'$(1,\,2)$', 'limite', 's'); arrow(ax, (70.5, 46.5), (44.8, 51.5), 'limite', lw=0.8)
text(ax, 75, 22, r'$2>2$ : faux', 'limite', 's')
save(fig, '20-045')
