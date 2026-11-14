import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
box(ax, 4, 40, 30, 11, 'fixe', label=r'$x + y = 5$', size='m')
box(ax, 4, 25, 30, 11, 'fixe', label=r'$x + y = 8$', size='m')
text(ax, 62, 45.5, 'seule : une infinité', 'resultat', 's')
text(ax, 62, 30.5, 'seule : une infinité', 'resultat', 's')
brace(ax, 4, 34, 23, 'limite', label='ensemble : aucune solution', size='s')
box(ax, 14, 2, 60, 9, 'sujet', label='système incompatible', size='m', weight='bold')
save(fig, '24-029')
