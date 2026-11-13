import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
dy = 14
text(ax, 44, 65 + dy, r'sur les réels $\mathbb{R}$', 'encre', 'm', weight='bold')
box(ax, 2, 40 + dy, 32, 14, 'sujet', label='(2, 0)\n(0, 1)')
arrow(ax, (35, 47 + dy), (51, 47 + dy), 'varie')
text(ax, 43, 52 + dy, r'ligne 1 $\times\frac{1}{2}$', 'varie', 's')
box(ax, 52, 40 + dy, 34, 14, 'resultat', label='(1, 0)\n(0, 1)')
box(ax, 2, 22 + dy, 40, 12, 'resultat', label=r'sur $\mathbb{R}$ : $\frac{1}{2}$ existe', size='s')
box(ax, 46, 22 + dy, 40, 12, 'limite', label=r'sur $\mathbb{Z}$ : $\frac{1}{2}$ interdit', size='s')
text(ax, 44, 16 + dy, 'tout pivot non nul devient 1', 'resultat', 's')
box(ax, 4, 2, 80, 16, 'resultat', label='facteurs invariants : 1 ou 0\nseul invariant : le rang\nmême rang : équivalentes', size='s')
save(fig, '59-158')
