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
fig, ax = canvas(88)
x0, x1, h = 8, 80, 10
f1 = bar(ax, x0, x1, 66, h, 3, 'sujet', fl('sujet', range(2)))
f3 = bar(ax, x0, x1, 38, h, 6, 'varie', fl('varie', range(4)))
for i in (1, 2): guide(ax, f1(i), 48, 66)
text(ax, x0, 80, r'$a$ = 2 parts prises', 'sujet', ha='left')
text(ax, x0, 52, r'$D$ = 6', 'varie', ha='left')
brace(ax, f3(0), f3(2), 38, 'varie', r'$D$ ÷ $b$ = 2', size='s')
brace(ax, f3(2), f3(4), 38, 'varie', r'$D$ ÷ $b$ = 2', size='s')
text(ax, 44, 21, r'$a$ × ($D$ ÷ $b$) = 2 × 2 = 4', 'varie', 'm')
text(ax, 44, 12, '2/3 = 4/6', 'resultat', 'l')
save(fig, '07-037')
