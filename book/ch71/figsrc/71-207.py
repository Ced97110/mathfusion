import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 6, 56, 30, 11, 'sujet', label=r'$x^2$'); box(ax, 52, 56, 30, 11, 'autre', label=r'$2x^2$')
text(ax, 44, 61.5, 'rang 1', 'fixe', 's')
text(ax, 44, 48, r'passage $P^2=2$ ?', 'varie', 's')
box(ax, 4, 28, 20, 12, 'fixe', label=r'$\mathbb{R}$', size='l'); box(ax, 28, 28, 56, 12, 'resultat', label=r'$P=\sqrt{2}$ : congruentes')
box(ax, 4, 8, 20, 12, 'fixe', label=r'$\mathbb{Q}$', size='l'); box(ax, 28, 8, 56, 12, 'limite', label=r'aucun $P$ : pas congruentes')
save(fig, '71-207')
