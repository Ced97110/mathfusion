import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
box(ax, 3, 28, 16, 10, 'fixe', label='point', size='s'); box(ax, 28, 28, 16, 10, 'autre', label=r'$B$', size='m')
box(ax, 53, 28, 16, 10, 'sujet', label=r'$A$', size='m'); box(ax, 72, 28, 14, 10, 'fixe', label='image', size='s')
arrow(ax, (19, 33), (28, 33), 'varie'); arrow(ax, (44, 33), (53, 33), 'varie'); arrow(ax, (69, 33), (72, 33), 'varie')
brace(ax, 28, 69, 26, 'resultat', label=r'$AB$ : $B$ puis $A$')
save(fig, '43-047')
