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
fig, ax = canvas(74)
text(ax, 44, 69, 'dépense exactement 12 €', 'sujet', 'm')
m = mp(14, 14, 9); axes(ax, m, 7.3, 4.8)
line(ax, [m(6, 0), m(0, 4)], 'sujet', lw=1.6)
for p in [(6, 0), (3, 2), (0, 4)]: disc(ax, *m(*p), 1.3, 'resultat')
text(ax, 40, 9.5, 'pains', 'fixe', 's'); text(ax, 14, 62, 'gâteaux', 'fixe', 's')
text(ax, m(6, 0)[0], 7.5, r'$2\times6=12$', 'resultat', 's')
text(ax, 57, 38, r'$2\times3+3\times2=12$', 'resultat', 's')
text(ax, 29, 56, r'$3\times4=12$', 'resultat', 's')
save(fig, '20-043')
