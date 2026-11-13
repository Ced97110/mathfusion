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
fig, ax = canvas(66)
def row(y, nb, nd, ka, kd, fa, fd):
    bar(ax, 8, 38, y, 10, nb, 'sujet', fl('sujet', range(ka)))
    bar(ax, 50, 80, y, 10, nd, 'autre', fl('autre', range(kd)))
    text(ax, 44, y + 5, '+', 'encre', 'l')
    text(ax, 23, y + 13.5, fa, 'sujet', 'm'); text(ax, 65, y + 13.5, fd, 'autre', 'm')
    text(ax, 23, y - 4, r'$b$ = %d' % nb, 'sujet', 'm'); text(ax, 65, y - 4, r'$d$ = %d' % nd, 'autre', 'm')
row(42, 2, 3, 1, 1, '1/2', '1/3')
row(14, 3, 5, 1, 2, '1/3', '2/5')
save(fig, '07-035')
