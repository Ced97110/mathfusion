import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 2, 46, 52, 14, 'sujet', label=r'$n_3$ divise 2 : 1 ou 2', size='s')
box(ax, 2, 26, 52, 14, 'sujet', label=r'$n_3 \equiv 1\ (\mathrm{mod}\ 3)$ : 1', size='s')
box(ax, 2, 6, 52, 14, 'resultat', label='unique, donc normal', size='s', weight='bold')
arrow(ax, (28, 45.5), (28, 40.5), 'fixe'); arrow(ax, (28, 25.5), (28, 20.5), 'fixe')
box(ax, 58, 6, 28, 54, 'fixe', fill=False, dash=True)
text(ax, 72, 54, 'avant (chap. 48)', 'fixe', 's')
for i in range(3):
    for j in range(2): disc(ax, 65 + 14 * j, 44 - 9 * i, 2.8, 'fixe')
text(ax, 72, 15, 'un test par élément', 'fixe', 's')
save(fig, '50-091')
