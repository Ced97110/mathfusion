import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, roles):
    pw = w / len(roles)
    for i, r in enumerate(roles):
        ax.add_patch(Rectangle((x + i * pw, y), pw, h, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))

fig, ax = canvas(62)
text(ax, 44, 56, r'$12/4$', 'sujet', 'l')
text(ax, 44, 49, 'la barre veut dire « divisé par »', 'varie', 's')
text(ax, 44, 43, r'$12 \div 4 = 3$', 'resultat', 'l')
for g in range(3):
    x = 11 + g * 24
    bar(ax, x, 22, 20, 5, ['sujet'] * 4)
    box(ax, x - 1.5, 19.5, 23, 10, 'resultat', fill=False)
    text(ax, x + 10, 33, '1 unité', 'resultat', 's')
brace(ax, 11, 79, 19, 'sujet', '12 quarts')
text(ax, 44, 5, '4 quarts font 1 unité', 'fixe', 's')
save(fig, '06-023')
