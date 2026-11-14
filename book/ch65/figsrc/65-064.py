import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

assert 0 ** 2 - 4 * (-2) == 8 and (2 * 2 ** 0.5) ** 2 - 8 < 1e-9
fig, ax = canvas(74)
text(ax, 44, 70, r'$x^2-2$ : $d=0^2-4\times(-2)=8$', 'sujet', 'm', weight='bold')
# row Q
box(ax, 2, 40, 38, 20, 'sujet', label=r'sur $\mathbb{Q}$' + '\n8 n’est pas un carré', size='s')
arrow(ax, (40.6, 50), (47.4, 50), 'fixe', lw=0.9)
box(ax, 48, 40, 38, 20, 'resultat', label=r'$G=S_2$' + '\n2 permutations', size='s', weight='bold')
# row R
box(ax, 2, 12, 38, 20, 'autre', label=r'sur $\mathbb{R}$' + '\n' + r'$8=(2\sqrt{2})^2$', size='s')
arrow(ax, (40.6, 22), (47.4, 22), 'fixe', lw=0.9)
box(ax, 48, 12, 38, 20, 'autre', label=r'$G=\{1\}$' + '\n1 permutation', size='s', weight='bold')
text(ax, 44, 4.5, 'le groupe dépend du corps de base', 'varie', 's')
save(fig, '65-064')
