import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, roles):
    pw = w / len(roles)
    for i, r in enumerate(roles):
        ax.add_patch(Rectangle((x + i * pw, y), pw, h, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))

fig, ax = canvas(66)
bar(ax, 10, 46, 68, 8, ['fixe']); text(ax, 44, 57, 'l’unité : un euro, une heure', 'fixe', 's')
bar(ax, 10, 28, 68, 8, ['varie'] * 4); text(ax, 44, 39, '1. le bas : couper en 4', 'varie', 'm')
bar(ax, 10, 10, 68, 8, ['sujet'] * 3 + ['fixe']); text(ax, 44, 21, '2. le haut : prendre 3', 'sujet', 'm')
text(ax, 44, 3.5, '$3/4$ = trois quarts', 'encre', 's')
save(fig, '06-024')
