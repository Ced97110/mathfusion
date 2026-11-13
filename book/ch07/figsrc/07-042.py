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
fig, ax = canvas(84)
x0, x1, h = 8, 80, 10
fl1 = {**fl('sujet', range(3)), **fl('autre', [3, 4])}
fl2 = {**fl('sujet', range(6)), **fl('autre', range(6, 10))}
f1 = bar(ax, x0, x1, 54, h, 6, 'fixe', fl1)
f2 = bar(ax, x0, x1, 22, h, 12, 'fixe', fl2)
guide(ax, f1(5), 32, 54)
text(ax, x0, 68, r'$D$ = 6 : 3/6 + 2/6 = 5/6', 'encre', ha='left')
text(ax, x0, 36.5, r'$D$ = 12 : 6/12 + 4/12', 'encre', ha='left')
text(ax, 38, 43, '= 10/12 = 5/6 : même longueur', 'resultat', 's')
text(ax, 44, 14, 'les deux sont corrects', 'resultat', 'l')
save(fig, '07-042')
