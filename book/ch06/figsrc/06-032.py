import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, roles):
    pw = w / len(roles)
    for i, r in enumerate(roles):
        ax.add_patch(Rectangle((x + i * pw, y), pw, h, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))

fig, ax = canvas(62)
bar(ax, 10, 46, 30, 8, ['sujet'] * 3); text(ax, 25, 57, 'barre 1', 'fixe', 's')
bar(ax, 46, 46, 30, 8, ['sujet'] * 2 + ['fixe']); text(ax, 61, 57, 'barre 2', 'fixe', 's')
brace(ax, 10, 76, 44, 'sujet', '5 parts prises sur 3')
box(ax, 10, 14, 28, 10, 'sujet', label='$5/3$'); box(ax, 50, 14, 28, 10, 'autre', label='$1+2/3$')
text(ax, 44, 19, '=', 'encre', 'l'); text(ax, 44, 7, 'même nombre', 'encre', 's')
save(fig, '06-032')
