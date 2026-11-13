import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, roles):
    pw = w / len(roles)
    for i, r in enumerate(roles):
        ax.add_patch(Rectangle((x + i * pw, y), pw, h, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))

fig, ax = canvas(54)
for y, n in [(36, 8), (22, 12)]:
    bar(ax, 22, y, 48, 8, ['sujet'] * n)
    text(ax, 11, y + 4, f'${n}/{n}$', 'sujet', 'l')
    text(ax, 79, y + 4, '$= 1$', 'resultat', 'l')
bar(ax, 22, 6, 48, 8, ['resultat'])
text(ax, 11, 10, '$1$', 'resultat', 'l'); text(ax, 46, 10, 'l’unité entière', 'resultat', 's')
save(fig, '06-031')
