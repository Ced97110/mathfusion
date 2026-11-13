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
x0, x1, h = 8, 80, 9
f1 = bar(ax, x0, x1, 62, h, 2, 'sujet', fl('sujet', range(2)))
f2 = bar(ax, x0, x1, 42, h, 3, 'autre', fl('autre', range(3)))
f3 = bar(ax, x0, x1, 20, h, 6, 'resultat', fl('resultat', range(6)))
for f, ids in ((f1, [1]), (f2, [1, 2])):
    for i in ids: guide(ax, f(i), 29, 62)
text(ax, x0, 74.5, r'$b$ = 2 parts', 'sujet', ha='left')
text(ax, x0, 54.5, r'$d$ = 3 parts', 'autre', ha='left')
text(ax, x0, 32.5, r'$D$ = 6 parts', 'resultat', ha='left')
text(ax, 44, 13, r'$D$ = PPCM de 2 et 3 = 6', 'resultat', 'm')
save(fig, '07-033')
