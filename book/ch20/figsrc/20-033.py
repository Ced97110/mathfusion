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
fig, ax = canvas(46)
for x, s, r in [(13, '2', 'sujet'), (20, 'x', 'fixe'), (27, '+', 'fixe'), (34, '3', 'sujet'), (41, 'y', 'fixe'), (52, r'\leq', 'varie'), (65, '12', 'sujet')]:
    text(ax, x, 34, '$' + s + '$', r, 'xl')
for x, s, r, xt in [(13, r'$a=2$', 'sujet', 13), (34, r'$b=3$', 'sujet', 34), (52, 'signe $\\leq$', 'varie', 52), (65, r'$c=12$', 'sujet', 68)]:
    text(ax, xt, 12, s, r, 'm'); arrow(ax, (xt if x != 65 else 66, 17), (x, 29), 'fixe', lw=0.8)
save(fig, '20-033')
