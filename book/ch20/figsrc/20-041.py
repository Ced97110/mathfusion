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
fig, ax = canvas(66)
for y, sg in [(56, r'\leq'), (30, '=')]:
    text(ax, 13, y, r'$2x+3y$', 'sujet', 'l'); text(ax, 28, y, '$' + sg + '$', 'varie', 'xl'); text(ax, 36, y, '$12$', 'sujet', 'l')
arrow(ax, (24, 50), (24, 36), 'varie'); text(ax, 36, 43, 'on remplace\n≤ par =', 'varie', 's')
m = mp(52, 16, 4.5); axes(ax, m, 6.7, 4.8)
line(ax, [m(6, 0), m(0, 4)], 'sujet', lw=1.6)
arrow(ax, (42, 30), (57, 30), 'fixe', lw=0.8)
text(ax, m(6, 0)[0], 11, '6', 'fixe', 's'); text(ax, 48.5, m(0, 4)[1], '4', 'fixe', 's')
text(ax, 71, 42, 'droite', 'sujet', 's'); arrow(ax, (70, 39.5), (67.5, 24.5), 'sujet', lw=0.8)
save(fig, '20-041')
