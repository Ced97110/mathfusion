import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
bw, bh = 28, 11
box(ax, 4, 46, bw, bh, 'sujet', label='1'); box(ax, 56, 46, bw, bh, 'sujet', label='3')
box(ax, 4, 8, bw, bh, 'resultat', label='quart'); box(ax, 56, 8, bw, bh, 'resultat', label='3 quarts', size='s')
arrow(ax, (4 + bw + 1, 51.5), (55, 51.5), 'fixe'); text(ax, 44, 56, '1+1+1', 'fixe', 's')
arrow(ax, (4 + bw + 1, 13.5), (55, 13.5), 'fixe'); text(ax, 44, 18, 'quart ×3', 'fixe', 's')
arrow(ax, (18, 45), (18, 20), 'varie'); arrow(ax, (70, 45), (70, 20), 'varie')
text(ax, 13, 32.5, r'$\eta$', 'varie', 'l', ha='right'); text(ax, 75, 32.5, r'$\eta$', 'varie', 'l', ha='left')
text(ax, 44, 33, 'même résultat', 'resultat', 's')
text(ax, 44, 66, r'$\eta(a^k)=\eta(a)^k$, $k=3$', 'encre', 'm')
save(fig, '45-070')
