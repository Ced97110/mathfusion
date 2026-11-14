import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 23, 74, 'y a le coefficient 1', 'sujet', 's'); text(ax, 65, 74, 'y a le coefficient 2', 'autre', 's')
box(ax, 3, 52, 40, 10, 'sujet', label=r'$x+y=5$'); box(ax, 45, 52, 40, 10, 'autre', label=r'$3x+2y=12$')
arrow(ax, (23, 52), (23, 24), 'varie'); text(ax, 25, 41, 'retrancher x', 'varie', 's', ha='left')
arrow(ax, (65, 52), (65, 24), 'varie'); text(ax, 67, 41, 'retrancher 3x', 'varie', 's', ha='left'); text(ax, 67, 36, 'diviser par 2', 'varie', 's', ha='left')
box(ax, 3, 12, 40, 12, 'sujet', label=r'$y=5-x$'); box(ax, 45, 12, 40, 12, 'autre', label=r'$y=6-\frac{3x}{2}$')
text(ax, 23, 6, 'sans fraction', 'resultat', 's'); text(ax, 65, 6, 'avec une fraction', 'autre', 's')
save(fig, '24-044')
