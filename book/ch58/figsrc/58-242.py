import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 44.5, 83, 'la liste', 'sujet', 'm', weight='bold')
box(ax, 27, 66, 12, 11, 'sujet', label='3', weight='bold')
box(ax, 40, 66, 22, 11, 'autre', label='(1, 2)', weight='bold')
# un homomorphisme par case
box(ax, 4, 38, 34, 11, 'varie', label=r'$\eta_1$ : double', size='s')
box(ax, 50, 38, 34, 11, 'varie', label=r'$\eta_2$ : additionne', size='s')
arrow(ax, (31, 65), (21, 50.5), 'sujet')
arrow(ax, (58, 65), (67, 50.5), 'autre')
# résultats dans le même module
box(ax, 10, 17, 22, 10, 'sujet', label='6', weight='bold')
box(ax, 56, 17, 22, 10, 'autre', label='3', weight='bold')
arrow(ax, (21, 37), (21, 28.5), 'sujet')
arrow(ax, (67, 37), (67, 28.5), 'autre')
text(ax, 44.5, 22, '+', 'encre', 'l', weight='bold')
text(ax, 44.5, 9, r'$\eta$ = 6 + 3 = 9, dans $\mathbb{Z}$', 'resultat', 'm', weight='bold')
save(fig, '58-242')
