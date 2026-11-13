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
fig, ax = canvas(90)
x0, x1, h = 8, 80, 10
fb = {**fl('sujet', range(6)), **fl('autre', range(6, 10))}
f = bar(ax, x0, x1, 58, h, 12, 'fixe', fb)
brace(ax, f(0), f(6), 70, 'sujet', '1/2 = 6/12', down=False)
brace(ax, f(6), f(10), 70, 'autre', '1/3 = 4/12', down=False)
brace(ax, f(0), f(10), 58, 'fixe', '10/12', down=True, size='m')
g = bar(ax, x0, x1, 18, h, 6, 'resultat', fl('resultat', range(5)))
guide(ax, f(10), 28, 54)
arrow(ax, (14, 50), (14, 30), 'varie')
text(ax, 19, 40, '÷ 2 : haut et bas', 'varie', 'm', ha='left')
text(ax, x0, 12, '5/6 : même nombre', 'resultat', 'l', ha='left')
save(fig, '07-044')
