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
fig, ax = canvas(100)
text(ax, 44, 93, 'chapitre 17 : une droite', 'fixe', 'm')
f = numberline(ax, 10, 70, 80, 0, 5, labels=False)
text(ax, f(2), 76.6, '2', 'fixe', 's'); text(ax, f(3), 76.6, '3', 'resultat', 's', weight='bold')
disc(ax, f(3), 80, 1.6, 'resultat')
arrow(ax, (f(0), 85), (f(3), 85), 'varie'); text(ax, f(1.5), 88.5, 'avance de 3', 'varie', 's')
text(ax, 44, 68, 'un nombre, un point', 'encre', 'm')
text(ax, 44, 59, 'ici : un couple', 'sujet', 'm')
m = mp(34, 14, 10); axes(ax, m, 4.5, 3.8)
arrow(ax, m(0, 0), m(1, 0), 'varie', lw=1.3); arrow(ax, m(1, 0), m(1, 1), 'varie', lw=1.3)
disc(ax, *m(1, 1), 1.6, 'resultat')
text(ax, m(0.5, 0)[0], 10.5, '1 pain', 'varie', 's'); text(ax, m(1, 0.5)[0] + 2.5, m(1, 0.5)[1] - 2, '1 gâteau', 'varie', 's', ha='left')
text(ax, m(1, 1)[0] + 3, m(1, 1)[1] + 1, r'$(1,\,1)$', 'resultat', 's', ha='left')
text(ax, 44, 3, 'un couple, un point du plan', 'encre', 'm')
save(fig, '20-037')
