import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, roles):
    pw = w / len(roles)
    for i, r in enumerate(roles):
        ax.add_patch(Rectangle((x + i * pw, y), pw, h, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))

fig, ax = canvas(56)
text(ax, 44, 50, '$0/3 = 0$', 'resultat', 'l')
brace(ax, 10, 70, 34, 'fixe', 'unité coupée en 3 parts', down=False)
bar(ax, 10, 24, 60, 8, ['fixe'] * 3)
f = numberline(ax, 10, 70, 16, 0, 1, step=1 / 3, labels=False, arrow_right=False)
for v, s in [(0, '0'), (1 / 3, '$1/3$'), (2 / 3, '$2/3$'), (1, '1')]:
    text(ax, f(v), 11, s, 'fixe', 's')
disc(ax, f(0), 16, 1.8, 'resultat')
arrow(ax, (10, 23.5), (10, 18.3), 'varie')
text(ax, 44, 4, '0 part prise : on reste en 0', 'resultat', 's')
save(fig, '06-029')
