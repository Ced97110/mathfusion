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
fig, ax = canvas(70)
y, h = 38, 10
for k in range(9):
    a = 8 + 8 * k
    bar(ax, a, a + 8, y, h, 5, 'sujet', fl('sujet', range(5) if k < 8 else range(3)), lw=0.4)
    ax.add_patch(Rectangle((a, y), 8, h, ec=COL['sujet'], fc='none', lw=1.4, zorder=2.5))
text(ax, 8, 53, 'chaque unité : 5 cinquièmes', 'sujet', ha='left')
brace(ax, 8, 72, y, 'sujet', '8 × 5 = 40', size='m')
brace(ax, 72, 80, y, 'varie', '3', size='m')
text(ax, 44, 20, '(8 × 5 + 3)/5 = 43/5', 'resultat', 'l')
text(ax, 44, 11, 'le dénominateur 5 ne change pas', 'resultat', 's')
save(fig, '07-048')
