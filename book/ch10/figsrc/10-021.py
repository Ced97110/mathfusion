import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(38)
box(ax, 3, 22, 30, 11, 'fixe', label=r'$2\,357 + 6\,106$')
arrow(ax, (34.5, 27.5), (43.5, 27.5), 'varie')
box(ax, 45, 22, 12, 11, 'sujet', label=r'$V$', size='l')
text(ax, 61, 27.5, '=', 'encre', 'l')
box(ax, 65, 22, 20, 11, 'resultat', label='8 463')
text(ax, 18, 13, 'vrais nombres', 'fixe', 's'); text(ax, 51, 13, 'nom : valeur exacte', 'sujet', 's'); text(ax, 75, 13, 'sa valeur', 'resultat', 's')
save(fig, '10-021')
