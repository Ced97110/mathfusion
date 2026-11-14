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
fig, ax = canvas(60)
text(ax, 44, 52, r'$y>x+1$', 'sujet', 'xl')
arrow(ax, (44, 47), (44, 37), 'varie'); text(ax, 48, 42, 'on enlève x des deux côtés', 'varie', 's', ha='left')
for x, s, r in [(18, r'$-x$', 'resultat'), (27, r'$+$', 'fixe'), (35, r'$y$', 'fixe'), (46, r'$>$', 'fixe'), (57, r'$1$', 'resultat')]:
    text(ax, x, 28, s, r, 'xl')
for x, s, xs in [(18, r'$a=-1$', 18), (35, r'$b=1$', 35), (57, r'$c=1$', 57)]:
    text(ax, x, 10, s, 'resultat', 'm'); arrow(ax, (x, 15), (xs, 23), 'fixe', lw=0.8)
save(fig, '20-034')
