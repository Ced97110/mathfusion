import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 22, 61, 'toujours la même phrase', 'fixe', 's')
text(ax, 73, 61, 'une écriture', 'sujet', 's')
for y, n in zip((44, 28, 12), (16, 256, 9)):
    box(ax, 3, y, 38, 10, 'fixe', label=f'corps à {n} éléments', size='s')
    arrow(ax, (41, y + 5), (60, y + 5), 'varie')
    box(ax, 60, y, 26, 10, 'sujet', label=r'$\mathbb{F}_{%d}$' % n)
text(ax, 44, 4, r'$\mathbb{F}_q$ : $q$ éléments', 'sujet', 'm')
save(fig, '67-049')
