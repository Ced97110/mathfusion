import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 9, 49, 'élément', 'fixe', 's')
text(ax, 43, 49, 'sa règle', 'fixe', 's')
text(ax, 74, 49, 'appliquée à 1', 'fixe', 's')
rows = [(30, '3', 'tripler', r'$1\mapsto 3$'), (14, '5', r'$\times 5$', r'$1\mapsto 5$')]
for y, a, rule, res in rows:
    box(ax, 2, y, 14, 9, 'sujet', label=a)
    arrow(ax, (17, y + 4.5), (31, y + 4.5), 'varie')
    box(ax, 32, y, 22, 9, 'varie', label=rule)
    arrow(ax, (55, y + 4.5), (63, y + 4.5), 'varie')
    box(ax, 64, y, 22, 9, 'resultat', label=res)
text(ax, 44, 5, 'la règle de a envoie 1 sur a', 'resultat', 'm')
save(fig, '57-061')
