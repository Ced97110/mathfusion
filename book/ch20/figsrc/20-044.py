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
m1 = mp(6, 18, 5); m2 = mp(52, 16, 6)
axes(ax, m1, 7, 5); axes(ax, m2, 4.2, 5.2)
line(ax, [m1(6, 0), m1(0, 4)], 'sujet', lw=1.4); line(ax, [m2(0, 1), m2(4, 5)], 'sujet', lw=1.4)
disc(ax, *m1(3, 2), 1.3, 'resultat'); disc(ax, *m2(1, 2), 1.3, 'limite')
text(ax, 22, 56, r'$2x+3y\leq12$', 'sujet', 'm'); text(ax, 66, 56, r'$y>x+1$', 'sujet', 'm')
text(ax, 30, 36, r'$(3,\,2)$', 'resultat', 's'); text(ax, 69, 26, r'$(1,\,2)$', 'limite', 's')
text(ax, 22, 8, r'$12\leq12$ : permis', 'resultat', 's'); text(ax, 66, 8, r'$2>2$ : refusé', 'limite', 's')
save(fig, '20-044')
