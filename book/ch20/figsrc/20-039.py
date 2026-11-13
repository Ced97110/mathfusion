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
fig, ax = canvas(72)
m = mp(44, 34, 9)
region(ax, m, UP, 'fixe'); region(ax, m, DOWN, 'fixe'); frame(ax, m, -3, 3, -3, 3)
line(ax, [m(-3, -2), m(2, 3)], 'sujet', lw=2.4)
text(ax, *m(-1.6, 1.8), 'demi-plan', 'fixe', 's'); text(ax, *m(1.4, -1.6), 'demi-plan', 'fixe', 's')
text(ax, 68, 67, 'droite frontière', 'sujet', 's'); arrow(ax, (66, 65), (62.5, 61.8), 'sujet', lw=0.8)
save(fig, '20-039')
