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
import numpy as np
fig, ax = canvas(62)
m1 = mp(22, 30, 5.5); m2 = mp(66, 30, 5.5)
region(ax, m1, UP, 'resultat'); frame(ax, m1, -3, 3, -3, 3)
line(ax, [m1(-3, -2), m1(2, 3)], 'sujet', lw=1.2, dash=True)
region(ax, m2, [(1/3, 3)] + [(x, 1/x) for x in np.linspace(1/3, 3, 40)] + [(3, 3)], 'resultat')
region(ax, m2, [(-1/3, -3)] + [(-x, -1/x) for x in np.linspace(1/3, 3, 40)] + [(-3, -3)], 'resultat')
frame(ax, m2, -3, 3, -3, 3)
for s in (1, -1):
    xs = np.linspace(1/3, 3, 60); line(ax, [m2(s * x, s / x) for x in xs], 'sujet', lw=1.2, dash=True)
disc(ax, *m2(2, 1), 1.0, 'resultat'); disc(ax, *m2(-2, -1), 1.0, 'resultat'); disc(ax, *m2(0, 0), 1.0, 'limite')
text(ax, *m2(1.9, 1.9), r'$(2,\,1)$', 'resultat', 's'); text(ax, *m2(-1.9, -1.9), r'$(-2,\,-1)$', 'resultat', 's')
text(ax, *m2(1.1, -1.0), r'$(0,\,0)$', 'limite', 's')
text(ax, 22, 54, r'linéaire : $y>x+1$', 'sujet', 's'); text(ax, 66, 54, r'pas linéaire : $xy>1$', 'autre', 's')
text(ax, 22, 7, 'une seule zone', 'resultat', 's'); text(ax, 66, 7, 'deux zones séparées', 'resultat', 's')
save(fig, '20-040')
