import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 14, 57, 60, 9, 'fixe', label='3 objets : combien de sacs ?', size='s')
box(ax, 4, 34, 36, 10, 'sujet', label=r'$2 \times 2 \times 2$'); box(ax, 48, 34, 36, 10, 'autre', label=r'$1 + 3 + 3 + 1$')
arrow(ax, (22, 57), (22, 44), 'varie'); arrow(ax, (66, 57), (66, 44), 'varie')
text(ax, 22, 29.5, 'par les choix', 'sujet', 's'); text(ax, 66, 29.5, 'par la taille', 'autre', 's')
box(ax, 32, 6, 24, 9, 'resultat', label='8 sacs')
arrow(ax, (22, 25), (38, 15), 'resultat'); arrow(ax, (66, 25), (50, 15), 'resultat')
save(fig, '42-271')
