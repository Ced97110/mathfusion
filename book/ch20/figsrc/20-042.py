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
for y, sg in [(52, '>'), (26, '=')]:
    text(ax, 11, y, '$y$', 'sujet', 'l'); text(ax, 20, y, '$' + sg + '$', 'varie', 'xl'); text(ax, 31, y, r'$x+1$', 'sujet', 'l')
arrow(ax, (22, 46), (22, 32), 'varie'); text(ax, 36, 39, 'seul le signe\nchange', 'varie', 's')
m = mp(60, 22, 5); axes(ax, m, 3.4, 4.2)
line(ax, [m(-2.4, -1.4), m(2.8, 3.8)], 'sujet', lw=1.6)
line(ax, [m(0, 1), m(1, 1), m(1, 2)], 'varie', lw=1.2)
disc(ax, *m(0, 1), 1.2, 'resultat')
text(ax, m(2.3, 1.0)[0], m(2.3, 1.0)[1], 'pente 1', 'varie', 's')
text(ax, 51, 35, 'hauteur 1', 'resultat', 's'); arrow(ax, (54.5, 33), (58.8, 27.8), 'resultat', lw=0.8)
save(fig, '20-042')
