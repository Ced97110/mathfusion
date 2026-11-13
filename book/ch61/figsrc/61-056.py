import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 4, 38, 34, 12, 'sujet', label=r'$x^2-2$', size='l'); box(ax, 50, 38, 34, 12, 'autre', label=r'$x^2-2$', size='l')
text(ax, 21, 55, 'élève 1', 'sujet', 's'); text(ax, 67, 55, 'élève 2', 'autre', 's')
text(ax, 44, 44, '=', 'resultat', 'xl', weight='bold')
arrow(ax, (21, 37.5), (38, 24), 'varie'); arrow(ax, (67, 37.5), (50, 24), 'varie')
box(ax, 28, 10, 32, 13, 'resultat', label=r'$m=x^2-2$', size='m')
text(ax, 44, 4, 'une seule réponse', 'resultat', 's')
save(fig, '61-056')
