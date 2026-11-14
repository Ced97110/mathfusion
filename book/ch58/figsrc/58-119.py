import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 22, 59, r'sous-module, $R=\mathbb{Z}$', 'sujet', 's', weight='bold')
text(ax, 66, 59, r'sous-espace, $F=\mathbb{R}$', 'sujet', 's', weight='bold')
line(ax, [(44, 14), (44, 62)], 'fixe', lw=0.6, dash=True)
# réseau d'entiers : une rangée de points = sous-module
for i in range(5):
    for j in range(4):
        x, y = 6 + i * 8, 22 + j * 8
        disc(ax, x, y, 1.1, 'sujet' if j == 0 else 'fixe', fill=(j == 0))
arrow(ax, (3, 22), (42, 22), 'fixe', lw=0.5)
text(ax, 22, 15, 'riz pur', 'sujet', 's')
# droite continue : multiples d'une flèche
ox, oy = 50, 22
arrow(ax, (ox - 3, oy), (ox + 36, oy), 'fixe', lw=0.5)
line(ax, [(ox, oy), (ox + 25, oy + 31)], 'sujet', lw=1.6)
arrow(ax, (ox, oy), (ox + 8, oy + 10), 'varie', lw=1.6)
text(ax, 66, 15, 'multiples d’une flèche', 'sujet', 's')
box(ax, 8, 2, 72, 8, 'resultat', label='même idée : une partie stable', size='s')
save(fig, '58-119')
