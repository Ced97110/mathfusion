import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 24, 46, 40, 10, 'fixe', label=r'$2\,357 + 6\,106$')
arrow(ax, (34, 46), (22, 33), 'sujet'); arrow(ax, (54, 46), (66, 33), 'varie')
box(ax, 3, 22, 38, 11, 'sujet', label=r'$V$ = 8 463', size='l'); box(ax, 47, 22, 38, 11, 'varie', label=r'$\tilde{V}$ = 8 500', size='l')
text(ax, 22, 14, 'exacte : vrais nombres', 'sujet', 's'); text(ax, 66, 14, 'approchée : remplacés', 'varie', 's')
text(ax, 44, 5, r'le trait $\sim$ : version approchée', 'varie', 's')
save(fig, '10-022')
