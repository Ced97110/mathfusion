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
text(ax, 44, 56, r'couple $(2,\,6)$', 'sujet', 'l')
text(ax, 22, 46, 'égale', 'varie', 'l'); text(ax, 66, 46, 'plus grand que', 'varie', 'l')
for x, s, r in [(14, '6', 'sujet'), (22, '=', 'varie'), (30, '5', 'fixe'), (58, '6', 'sujet'), (66, '>', 'varie'), (74, '5', 'fixe')]:
    text(ax, x, 34, '$' + s + '$', r, 'xl')
text(ax, 22, 23, 'faux', 'limite', 'l'); text(ax, 66, 23, 'vrai', 'resultat', 'l')
line(ax, [(44, 28), (44, 52)], 'fixe', lw=0.5, dash=True)
text(ax, 44, 12, 'même test, signe changé', 'encre', 's')
text(ax, 44, 4.5, r'$5=2\times2+1$', 'fixe', 's')
save(fig, '20-036')
