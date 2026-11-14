import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 16, 46, 'candidats', 'sujet', 's')
box(ax, 4, 28, 24, 12, 'limite', True, r'$a=4$')
arrow(ax, (29, 34), (50, 34), 'varie')
text(ax, 39.5, 41, r'$a=4$ interdit', 'varie', 's')
text(ax, 67, 46, 'solutions', 'resultat', 's')
box(ax, 52, 24, 32, 20, 'resultat', False, 'aucune', 'm', dash=True)
save(fig, '21-096')
