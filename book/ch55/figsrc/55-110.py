import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 14, 40, r'$\prod_{i<j}$', 'varie', 22)
text(ax, 14, 22, 'produit de', 'varie', 'm')
text(ax, 60, 66, 'six paires : six facteurs', 'sujet', 'm')
pairs = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
for n, (i, j) in enumerate(pairs):
    col, row = n % 2, n // 2
    box(ax, 32 + col * 27, 48 - row * 17, 26, 12, 'sujet', label=rf'$(x_{i}-x_{j})^2$', size='s')
arrow(ax, (27, 40), (31, 40), 'varie')
save(fig, '55-110')
