import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
bx, bw, bh = 4, 40, 10
tx = bx + bw + 5
# deux lignes de départ
box(ax, bx, 84, bw, bh, 'sujet', label='L1 : x + y = 3')
box(ax, bx, 68, bw, bh, 'autre', label='L2 : x − y = 1')
# opération 1 : addition de deux lignes
text(ax, bx + bw / 2, 81, '+', 'varie', 'xl', weight='bold')
arrow(ax, (bx + bw / 2, 66.5), (bx + bw / 2, 56.5), 'varie', lw=1.4)
box(ax, tx, 62, 35, 12, 'varie', label='addition : L1 + L2', size='s', lw=1.2)
box(ax, bx, 46, bw, bh, 'fixe', label='2x = 4')
# opération 2 : multiplication d'une ligne par un nombre
arrow(ax, (bx + bw / 2, 44.5), (bx + bw / 2, 34.5), 'varie', lw=1.4)
box(ax, tx, 40, 35, 12, 'varie', label=r'multiplier par $\frac{1}{2}$', size='s', lw=1.2)
box(ax, bx, 24, bw, bh, 'resultat', label='x = 2')
arrow(ax, (bx + bw / 2, 22.5), (bx + bw / 2, 12.5), 'fixe', lw=1.0)
text(ax, tx, 18, 'dans L1 : 2 + y = 3', 'fixe', 's', ha='left')
box(ax, bx, 2, bw, bh, 'resultat', label='y = 1')
save(fig, '57-004')
