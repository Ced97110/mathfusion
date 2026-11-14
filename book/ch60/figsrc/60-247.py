import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
for i in range(3):
    box(ax, 6 + 14 * i, 54, 12, 9, 'sujet', label=rf'$b_{i+1}$')
    box(ax, 6 + 14 * i, 12, 12, 9, 'autre', label=rf'$c_{i+1}$')
box(ax, 6, 33, 40, 9, 'fixe', label='même module libre')
arrow(ax, (26, 53.5), (26, 43), 'sujet')
arrow(ax, (26, 22.5), (26, 32), 'autre')
text(ax, 70, 58.5, '3 éléments', 'sujet', 's')
text(ax, 70, 16.5, '3 éléments', 'autre', 's')
arrow(ax, (73, 55), (73, 42), 'fixe')
arrow(ax, (73, 20), (73, 31), 'fixe')
box(ax, 58, 31, 28, 11, 'resultat', label='même nombre', size='s')
save(fig, '60-247')
