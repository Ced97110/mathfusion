import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
box(ax, 3, 4, 82, 54, 'fixe', fill=True)
text(ax, 44, 53, 'transformations réversibles', 'fixe', 's')
box(ax, 6, 8, 50, 38, 'resultat')
text(ax, 31, 40, 'dét. 1 = fabricables', 'resultat', 's')
disc(ax, 31, 29, 1.6, 'resultat'); text(ax, 31, 23, 'quart de tour', 'resultat', 's'); text(ax, 31, 17, 'dét. 1', 'resultat', 's')
disc(ax, 71, 29, 1.6, 'limite'); text(ax, 71, 23, 'dilatation', 'limite', 's'); text(ax, 71, 17, 'dét. 2', 'limite', 's')
save(fig, '73-156')
