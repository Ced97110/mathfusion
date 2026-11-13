import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
ideals = [48, 24, 12, 6, 3]
xs = [2 + 13 * i for i in range(5)]
arrow(ax, (2, 52), (85, 52), 'varie')
text(ax, 44, 57, 'indice = numéro de place', 'varie', 's')
for i, (x, d) in enumerate(zip(xs, ideals)):
    box(ax, x, 30, 10, 11, 'sujet', label=rf'$I_{i + 1}$', size='m')
    text(ax, x + 5, 25.5, f'({d})', 'sujet', 's')
text(ax, 69, 35.5, '…', 'fixe', 'l')
box(ax, 74, 30, 11, 11, 'autre', label=r'$I_n$', size='m', dash=True)
text(ax, 79.5, 25.5, 'rang n', 'autre', 's')
save(fig, '56-104')
