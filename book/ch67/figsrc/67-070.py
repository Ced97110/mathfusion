import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# q = 4, characteristic 2 : derivative of x^4 - x is 4 x^3 - 1 and 4 = 0, so it is -1
text(ax, 44, 79, 'caractéristique 2, $q = 4$', 'encre', 's')
box(ax, 22, 62, 44, 12, 'sujet', label=r'$x^4 - x$')
arrow(ax, (44, 61), (44, 53), 'varie')
text(ax, 62, 57, 'dérivée', 'varie', 's')
box(ax, 22, 40, 44, 12, 'sujet', label=r'$4\,x^3 - 1$')
arrow(ax, (44, 39), (44, 31), 'varie')
text(ax, 62, 35, r'$4 = 0$', 'varie', 'm', weight='bold')
box(ax, 22, 18, 44, 12, 'resultat', label=r'$-1$')
text(ax, 44, 8, 'jamais nul : pas de racine double', 'resultat', 's')
save(fig, '67-070')
