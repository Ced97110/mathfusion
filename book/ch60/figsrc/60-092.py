import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
xs = [6, 22, 38]
for x, v, r in zip(xs, ['2', '2', '3'], ['varie', 'fixe', 'varie']):
    box(ax, x, 44, 14, 10, r, label=v, size='l')
text(ax, 22, 58, 'diviseurs élémentaires', 'sujet', 's')
arrow(ax, (52, 49), (60, 49), 'varie')
box(ax, 60, 44, 24, 10, 'resultat', label=r'$d_2=2\times3=6$')
text(ax, 72, 57, 'tour 1', 'varie', 's')
arrow(ax, (29, 43), (29, 31), 'fixe')
text(ax, 44, 37, 'reste', 'fixe', 's', ha='left')
box(ax, 22, 20, 14, 10, 'fixe', label='2', size='l')
arrow(ax, (36, 25), (60, 25), 'varie')
box(ax, 60, 20, 24, 10, 'resultat', label=r'$d_1=2$')
text(ax, 72, 33, 'tour 2', 'varie', 's')
text(ax, 44, 10, 'deux tours : 2 facteurs', 'resultat', 's')
save(fig, '60-092')
