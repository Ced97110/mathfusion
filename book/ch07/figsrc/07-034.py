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
x0, x1 = 8, 80
f = bar(ax, x0, x1, 40, 12, 4, 'sujet', fl('sujet', range(3)))
brace(ax, x0, x1, 54, 'sujet', r'$b$ = 4 parts font l’unité', down=False, size='m')
text(ax, 44, 35, r'$a$ = 3 parts prises', 'sujet', 's')
bar(ax, x0, x1, 8, 12, 8, 'fixe')
text(ax, 44, 3.5, r'$b$ = 8 : parts plus petites', 'fixe', 's')
save(fig, '07-034')
