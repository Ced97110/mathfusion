import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
box(ax, 3, 18, 22, 12, 'fixe', label='(3, 4)', size='m'); box(ax, 33, 18, 22, 12, 'sujet', label=r'$I$', size='l'); box(ax, 63, 18, 22, 12, 'fixe', label='(3, 4)', size='m')
arrow(ax, (26, 24), (32, 24), 'varie'); arrow(ax, (56, 24), (62, 24), 'varie')
text(ax, 44, 36, 'matrice identité', 'sujet', 's')
brace(ax, 14, 74, 16, 'resultat', label='même point : rien ne change')
save(fig, '43-048')
