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
fig, ax = canvas(104)
x0, x1, h = 8, 80, 9
f1 = bar(ax, x0, x1, 88, h, 3, 'autre', fl('autre', [0]))
f2 = bar(ax, x0, x1, 66, h, 6, 'varie', fl('varie', range(2)))
guide(ax, f1(1), 75, 88); guide(ax, f1(2), 75, 88)
text(ax, x0, 101.5, r'1/3 : $d$ = 3', 'autre', ha='left')
text(ax, x0, 81.5, r'$D$ = 6', 'varie', ha='left')
brace(ax, f2(0), f2(2), 66, 'varie', r'$D$ ÷ $d$ = 6 ÷ 3 = 2', size='m')
g1 = bar(ax, x0, x1, 40, h, 4, 'autre', fl('autre', range(3)))
g2 = bar(ax, x0, x1, 18, h, 12, 'varie', fl('varie', range(3)))
for i in (1, 2, 3): guide(ax, g1(i), 27, 40)
text(ax, x0, 53.5, r'3/4 : $d$ = 4', 'autre', ha='left')
text(ax, x0, 33.5, r'$D$ = 12', 'varie', ha='left')
brace(ax, g2(0), g2(3), 18, 'varie', r'$D$ ÷ $d$ = 12 ÷ 4 = 3', size='m')
save(fig, '07-038')
