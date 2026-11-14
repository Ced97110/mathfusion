import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
text(ax, 18, 76, 'élément', 'sujet', 's'); text(ax, 70, 76, 'ses atomes', 'autre', 's')
for k, (n, S) in enumerate(((6, r'$\{2,3\}$'), (10, r'$\{2,5\}$'))):
    y = 58 - k * 18
    box(ax, 6, y - 6, 24, 12, 'sujet', label=str(n), size='m')
    arrow(ax, (31, y), (53, y), 'varie', both=True)
    box(ax, 54, y - 6, 28, 12, 'autre', label=S, size='m')
text(ax, 42, 61, 'sous 6', 'varie', 's'); text(ax, 42, 43, 'sous 10', 'varie', 's')
box(ax, 6, 8, 12, 10, 'autre', label='2', size='m'); box(ax, 24, 8, 12, 10, 'autre', label='5', size='m')
arrow(ax, (36, 13), (52, 13), 'resultat')
box(ax, 54, 8, 14, 10, 'sujet', label='10', size='m')
text(ax, 44, 25, 'plus petit multiple commun', 'resultat', 's')
save(fig, '80-216')
