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
fig, ax = canvas(90)
w = 5.4; x0 = (88 - 12 * w) / 2
for i in range(12):
    r = 'sujet' if i < 6 else 'varie'
    ax.add_patch(Rectangle((x0 + i * w, 70), w, 6, ec=COL[r], fc=FILL[r], lw=0.6, zorder=2))
    ax.add_patch(Rectangle((x0 + i * w, 48), w, 6, ec=COL['autre'], fc=FILL['autre'], lw=0.6, zorder=2))
text(ax, 44, 81, r'gauche : $2\times3+3\times2$', 'sujet', 's')
text(ax, 44, 62, '$=$', 'resultat', 'xl'); text(ax, 44, 42, 'droite : 12', 'autre', 's')
box(ax, 4, 14, 38, 16, 'resultat', label='≤ accepte l’égalité\n$12\\leq12$ : vrai', size='s')
box(ax, 46, 14, 38, 16, 'limite', label='< la refuse\n$12<12$ : faux', size='s')
arrow(ax, (24, 38), (24, 31), 'fixe', lw=0.8); arrow(ax, (64, 38), (64, 31), 'fixe', lw=0.8)
save(fig, '20-047')
