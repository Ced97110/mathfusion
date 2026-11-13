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
fig, ax = canvas(84)
bar(ax, 8, 41, 58, 10, 4, 'fixe', fl('fixe', range(3)))
text(ax, 8, 72, '3/4 : propre, moins de 1', 'fixe', ha='left')
bar(ax, 8, 41, 26, 10, 4, 'sujet', fl('sujet', range(4)))
bar(ax, 47, 80, 26, 10, 4, 'sujet', fl('sujet', [0]))
text(ax, 8, 40.5, '5/4 : impropre, plus de 1', 'sujet', ha='left')
brace(ax, 8, 41, 26, 'fixe', '1 unité', size='s')
brace(ax, 47, 80, 26, 'sujet', '1/4 de plus', size='s')
text(ax, 44, 8, 'ou 1 1/4 : nombre mixte', 'sujet', 'm')
save(fig, '07-046')
