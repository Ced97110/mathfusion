import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 4, 38, 26, 14, 'sujet', label=r'$1+\sqrt{2}$', size='l')
box(ax, 58, 38, 26, 14, 'resultat', label=r'$\sqrt{2}-1$', size='l')
arrow(ax, (30.5, 45), (57.5, 45), 'varie')
text(ax, 44, 49.5, 'inverser', 'varie', 's')
for x0 in (4, 58):
    box(ax, x0, 14, 12, 10, 'fixe', label='1', size='s')
    box(ax, x0 + 14, 14, 12, 10, 'fixe', label=r'$\sqrt{2}$', size='s')
    line(ax, [(x0 + 13, 37.5), (x0 + 13, 25)], 'fixe', dash=True)
    text(ax, x0 + 13, 8, '2 briques', 'fixe', 's')
text(ax, 44, 19, 'mêmes', 'fixe', 's')
save(fig, '61-084')
