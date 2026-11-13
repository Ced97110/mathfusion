import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle
def bar(ax, x0, x1, y, h, n, role, fills=None, lw=0.8):
    w = (x1 - x0) / n; fills = fills or {}
    for i in range(n):
        fc = FILL[fills[i]] if i in fills else 'white'
        ax.add_patch(Rectangle((x0 + i * w, y), w, h, ec=COL[role], fc=fc, lw=lw, zorder=2))
    return lambda i: x0 + i * w
def guide(ax, x, y0, y1):
    ax.plot([x, x], [y0, y1], color=COL['fixe'], lw=0.7, ls='--', zorder=1.5)
def fl(role, ids): return {i: role for i in ids}
fig, ax = canvas(72)
x0, x1, h = 8, 80, 10
f1 = bar(ax, x0, x1, 48, h, 2, 'sujet', fl('sujet', [0]))
f2 = bar(ax, x0, x1, 18, h, 6, 'sujet', fl('sujet', range(3)))
guide(ax, f1(1), 28, 48)
arrow(ax, (16, 46), (16, 30), 'varie')
text(ax, 21, 38, '× 3/3 = × 1', 'varie', 'm', ha='left')
text(ax, 66, 38, 'même longueur', 'sujet', 'm')
text(ax, x0, 62, '1/2', 'sujet', 'l', ha='left')
text(ax, x0, 12, '3/6', 'sujet', 'l', ha='left')
text(ax, 62, 12, 'haut et bas × 3', 'varie', 's')
save(fig, '07-041')
