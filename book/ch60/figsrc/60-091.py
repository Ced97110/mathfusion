import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 16, 58, 'facteurs invariants', 'sujet', 's')
text(ax, 70, 58, 'diviseurs élémentaires', 'resultat', 's')
box(ax, 3, 44, 26, 10, 'sujet', label=r'$d_1=2$')
box(ax, 3, 22, 26, 10, 'sujet', label=r'$d_2=6=2\times3$')
ys = [44, 28, 12]
for y, v in zip(ys, ['2', '2', '3']):
    box(ax, 62, y, 20, 10, 'resultat', label=v, size='l')
arrow(ax, (29, 49), (61, 49), 'varie')
arrow(ax, (29, 27), (61, 33), 'varie')
arrow(ax, (29, 27), (61, 17), 'varie')
save(fig, '60-091')
