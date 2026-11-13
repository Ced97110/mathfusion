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
fig, ax = canvas(58)
y, h = 28, 12
bar(ax, 8, 38, y, h, 1, 'sujet', fl('sujet', [0]))
bar(ax, 46, 76, y, h, 2, 'sujet', fl('sujet', [0]))
text(ax, 42, y + h / 2, '+', 'encre', 'l')
brace(ax, 8, 38, y, 'sujet', 'entier : 1', size='m')
brace(ax, 46, 76, y, 'sujet', 'fraction : 1/2 < 1', size='m')
text(ax, 44, 50, '1 1/2 = 1 + 1/2', 'sujet', 'l')
save(fig, '07-045')
