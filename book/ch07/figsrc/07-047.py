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
h = 10
bar(ax, 8, 30, 62, h, 3, 'limite', fl('limite', range(2)))
text(ax, 8, 76, 'mal lu : 2 × 1/3', 'limite', ha='left')
text(ax, 34, 67, '= 2/3, moins de 1', 'limite', 'm', ha='left')
ux = [(8, 30), (33, 55), (58, 80)]
for k, (a, b) in enumerate(ux):
    bar(ax, a, b, 30, h, 3, 'resultat', fl('resultat', range(3) if k < 2 else [0]))
text(ax, 8, 44, 'bien lu : 2 + 1/3', 'resultat', ha='left')
brace(ax, 8, 55, 30, 'resultat', '2 entiers', size='s')
brace(ax, 58, 80, 30, 'resultat', '1/3', size='s')
text(ax, 44, 14, '= 7/3, plus de 2', 'resultat', 'l')
save(fig, '07-047')
