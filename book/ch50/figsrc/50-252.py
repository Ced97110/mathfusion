import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 3, 24, 22, 14, 'sujet', label='ordre 60', size='m')
box(ax, 35, 36, 26, 12, 'fixe', label=r'$n_5 = 1$'); box(ax, 35, 14, 26, 12, 'fixe', label=r'$n_5 = 6$')
arrow(ax, (25, 33), (35, 41), 'varie'); arrow(ax, (25, 29), (35, 20), 'varie')
text(ax, 48, 7, 'le comptage ne choisit pas', 'varie', 's')
box(ax, 68, 22, 18, 18, 'resultat'); text(ax, 77, 34, r'$A_5$', 'resultat', 'l', weight='bold'); text(ax, 77, 27, 'existe', 'resultat', 's')
arrow(ax, (61, 42), (68, 36), 'resultat'); arrow(ax, (61, 20), (68, 26), 'resultat')
save(fig, '50-252')
