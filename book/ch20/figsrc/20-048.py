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
fig, ax = canvas(62)
m1 = mp(22, 30, 5.5); m2 = mp(66, 30, 5.5)
region(ax, m2, UP, 'resultat')
for m in (m1, m2):
    frame(ax, m, -3, 3, -3, 3); line(ax, [m(-3, -2), m(2, 3)], 'varie', lw=1.5, dash=True)
disc(ax, *m2(0, 0), 1.1, 'limite'); text(ax, *m2(1.5, -1.2), r'$(0,\,0)$', 'limite', 's')
text(ax, *m2(-1.5, 2.2), 'solutions', 'resultat', 's')
text(ax, 22, 54, 'temps 1 : la frontière', 'varie', 's'); text(ax, 66, 54, 'temps 2 : le côté', 'resultat', 's')
text(ax, 22, 7, 'droite en pointillés', 'varie', 's'); text(ax, 66, 7, r'$0>1$ : faux, autre côté', 'limite', 's')
arrow(ax, (40, 30), (48, 30), 'fixe')
save(fig, '20-048')
