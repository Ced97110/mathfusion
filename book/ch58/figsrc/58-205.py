import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
# stock (3, 1) : séparer, remplacer chaque sac par son image, additionner
text(ax, 55, 73, r'$\eta(x)$ pour le stock $(3, 1)$', 'encre', 'm', weight='bold')
ys = [54, 33, 12]
for y, w in zip(ys, ['séparer', 'remplacer', 'additionner']):
    text(ax, 2, y + 5.5, w, 'varie', 's', ha='left', weight='bold')
box(ax, 24, ys[0], 28, 11, 'sujet', label='3 sacs type 1', size='s')
text(ax, 55, ys[0] + 5.5, '+', 'encre', 'm')
box(ax, 58, ys[0], 28, 11, 'varie', label='1 sac type 2', size='s')
box(ax, 24, ys[1], 28, 11, 'sujet', label=r'$3 \times (2, 1) = (6, 3)$', size='s')
box(ax, 58, ys[1], 28, 11, 'varie', label=r'$1 \times (1, 3) = (1, 3)$', size='s')
for x in (38, 72):
    arrow(ax, (x, ys[0] - 0.5), (x, ys[1] + 11.5), 'fixe', lw=1.0)
    arrow(ax, (x, ys[1] - 0.5), (55, ys[2] + 11.5), 'fixe', lw=1.0)
box(ax, 24, ys[2], 62, 11, 'resultat', label=r'$(6, 3) + (1, 3) = (7, 6)$', size='m', weight='bold')
save(fig, '58-205')
