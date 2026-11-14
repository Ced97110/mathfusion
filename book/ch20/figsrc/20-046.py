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
TRI = [(0, 0), (6, 0), (0, 4)]
for ox, dash, ok, hd, calc, rl in [(6, False, True, r'$2x+3y\leq12$', r'$12\leq12$ : vrai', 'resultat'), (50, True, False, r'$2x+3y<12$', r'$12<12$ : faux', 'limite')]:
    m = mp(ox, 18, 5); region(ax, m, TRI, 'sujet'); axes(ax, m, 7, 5)
    line(ax, [m(6, 0), m(0, 4)], 'varie', lw=1.5, dash=dash)
    disc(ax, *m(3, 2), 1.3, rl)
    text(ax, ox + 16, 56, hd, 'sujet', 'm'); text(ax, ox + 25, 36, r'$(3,\,2)$', rl, 's')
    text(ax, ox + 16, 8, calc, rl, 's')
text(ax, 22, 47, 'trait plein', 'varie', 's'); text(ax, 66, 47, 'pointillés', 'varie', 's')
save(fig, '20-046')
