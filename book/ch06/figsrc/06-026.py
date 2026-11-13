import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, roles):
    pw = w / len(roles)
    for i, r in enumerate(roles):
        ax.add_patch(Rectangle((x + i * pw, y), pw, h, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))

fig, ax = canvas(66)
text(ax, 44, 60, '« 3 » : quelle longueur ?', 'limite', 'm')
for y, L in [(46, 14), (36, 28), (26, 44)]:
    box(ax, 10, y, L, 6, 'limite')
    text(ax, 10 + L + 7, y + 3, '3 ?', 'limite', 'm')
bar(ax, 10, 6, 60, 8, ['sujet'] * 3 + ['fixe'])
text(ax, 40, 17, '3 quarts : une longueur', 'sujet', 'm')
save(fig, '06-026')
