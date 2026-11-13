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
f1 = bar(ax, x0, x1, 66, h, 4, 'autre', fl('autre', range(3)))
f2 = bar(ax, x0, x1, 38, h, 12, 'resultat', fl('resultat', range(9)))
for i in (1, 2, 3): guide(ax, f1(i), 48, 66)
text(ax, x0, 80, r'3/4 : $c$ = 3, $d$ = 4', 'autre', ha='left')
text(ax, x0, 52, r'$D$ = 12', 'resultat', ha='left')
brace(ax, f2(0), f2(3), 38, 'resultat', r'$D$ ÷ $d$ = 3', size='s')
brace(ax, f2(3), f2(6), 38, 'resultat', '3', size='s')
brace(ax, f2(6), f2(9), 38, 'resultat', '3', size='s')
text(ax, 44, 22, r'$c$ × ($D$ ÷ $d$) = 3 × 3 = 9', 'resultat', 'm')
text(ax, 44, 13, '9 douzièmes', 'resultat', 'l')
save(fig, '07-039')
