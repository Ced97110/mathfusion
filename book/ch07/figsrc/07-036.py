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
fig, ax = canvas(80)
x0, x1, h = 8, 80, 10
f1 = bar(ax, x0, x1, 56, h, 2, 'sujet', fl('sujet', [0]))
f3 = bar(ax, x0, x1, 28, h, 6, 'varie', fl('varie', range(3)))
guide(ax, f1(1), 38, 56)
text(ax, x0, 70, r'$b$ = 2 parts', 'sujet', ha='left')
text(ax, x0, 43, r'$D$ = 6 parts', 'varie', ha='left')
brace(ax, f3(0), f3(3), 28, 'varie', r'$D$ ÷ $b$ = 6 ÷ 2 = 3', size='m')
save(fig, '07-036')
