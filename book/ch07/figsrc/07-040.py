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
box(ax, 4, 4, 80, 44, 'resultat')
box(ax, 12, 8, 64, 29, 'varie')
box(ax, 20, 12, 48, 14, 'sujet')
text(ax, 44, 42.5, r'③ $a$ × ($D$ ÷ $b$) = 1 × 3 = 3', 'resultat', 'm')
text(ax, 44, 31.5, r'② $D$ ÷ $b$ = 6 ÷ 2 = 3', 'varie', 'm')
text(ax, 44, 19, r'① $D$ = 6', 'sujet', 'm')
text(ax, 44, 53, 'pour 1/2 + 1/3', 'encre', 'm')
save(fig, '07-040')
