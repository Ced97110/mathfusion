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
box(ax, 6, 46, 52, 12, 'sujet', label=r'couple $(1,\,1)$')
box(ax, 6, 26, 52, 12, 'varie', label=r'$2\times1+3\times1=5$')
box(ax, 6, 6, 52, 12, 'resultat', label=r'$5\leq12$ : vrai')
arrow(ax, (32, 46), (32, 39), 'fixe'); arrow(ax, (32, 26), (32, 19), 'fixe')
text(ax, 61, 52, '1 pain, 1 gâteau', 'sujet', 's', ha='left')
text(ax, 61, 32, 'on remplace x et y', 'varie', 's', ha='left')
text(ax, 61, 12, 'phrase vraie', 'resultat', 's', ha='left')
save(fig, '20-035')
