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
x0, x1, h = 8, 80, 9
fa = {**fl('sujet', range(18)), **fl('autre', range(18, 22))}
fb = {**fl('sujet', range(9)), **fl('autre', [9, 10])}
bar(ax, x0, x1, 58, h, 24, 'fixe', fa, lw=0.5)
bar(ax, x0, x1, 22, h, 12, 'resultat', fb)
guide(ax, 74, 31, 58)
text(ax, x0, 72, '24 = 4 × 6 : 18 + 4 = 22', 'encre', ha='left')
arrow(ax, (14, 56), (14, 33), 'varie')
text(ax, 19, 45, 'on réduit : ÷ 2', 'varie', 'm', ha='left')
text(ax, 80, 52, '22/24 = 11/12', 'resultat', 's', ha='right')
text(ax, x0, 16, '12 = PPCM : 9 + 2 = 11', 'resultat', ha='left')
save(fig, '07-043')
