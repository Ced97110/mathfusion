import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
pairs = [(0, 1), (1, 3), (2, 5), (3, 7)]
for i, (a, b) in enumerate(pairs):
    box(ax, 12, 72 - i * 11, 24, 9, 'sujet', label=f'({a}, {b})', size='m')
box(ax, 12, 28, 24, 9, 'fixe', dash=True, label='(4, 9)', size='m')
text(ax, 24, 19, '…', 'fixe', 'xl')
line(ax, [(8, 81), (6, 81), (6, 39), (8, 39)], 'sujet'); text(ax, 3, 60, '4 couples', 'sujet', 's', rot=90)
arrow(ax, (50, 62), (50, 8), 'varie'); text(ax, 62, 35, 'ne finit jamais', 'varie', 's')
text(ax, 62, 62, 'et ainsi de suite', 'fixe', 's')
save(fig, '19-010')
