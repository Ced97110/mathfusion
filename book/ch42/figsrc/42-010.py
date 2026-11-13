import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
text(ax, 20, 50, '∅', 'sujet', 40, weight='bold')
arrow(ax, (36, 50), (46, 50), 'sujet')
text(ax, 64, 53, 'se lit', 'fixe', 's'); text(ax, 64, 47, 'ensemble vide', 'resultat', 'm', weight='bold')
text(ax, 64, 38, 'et non « zéro »', 'limite', 's')
box(ax, 14, 6, 20, 10, 'sujet', label='∅', size='l')
arrow(ax, (24, 38), (24, 17), 'varie')
text(ax, 62, 11, 'case du bas : sac sans objet', 'fixe', 's')
save(fig, '42-010')
