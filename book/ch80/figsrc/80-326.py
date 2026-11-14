import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
box(ax, 8, 62, 72, 12, 'sujet', label=r'$1 \vee 1 = 1 + 1 + 1$')
box(ax, 4, 36, 36, 12, 'varie', label=r'$1 + 1 = 0$'); box(ax, 48, 36, 36, 12, 'resultat', label=r'$0 + 1 = 1$')
arrow(ax, (40, 42), (48, 42), 'varie'); arrow(ax, (30, 62), (22, 48), 'varie')
text(ax, 22, 31, '1re étape', 'varie', 's'); text(ax, 66, 31, '2e étape', 'resultat', 's')
box(ax, 8, 8, 72, 12, 'limite', label=r'avec les entiers : $1+1+1=3$', size='s', dash=True)
save(fig, '80-326')
