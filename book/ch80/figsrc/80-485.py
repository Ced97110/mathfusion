import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 4, 46, 38, 10, 'fixe', label=r'$3 + 5 = 5 + 3$')
box(ax, 46, 46, 38, 10, 'fixe', label=r'$4 + 6 = 6 + 4$')
arrow(ax, (23, 45), (32, 35), 'varie'); arrow(ax, (65, 45), (56, 35), 'varie')
box(ax, 14, 22, 60, 12, 'sujet', label=r'$a + b = b + a$', size='xl', weight='bold')
text(ax, 44, 15, r'$a$ et $b$ : tous les nombres', 'varie', 'm')
text(ax, 44, 8, 'vrai pour chaque couple', 'resultat', 'm')
save(fig, '80-485')
