import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
text(ax, 44, 70, r'$\nu : R\rightarrow R/I,\ a\mapsto a+I$', 'encre', 's')
text(ax, 18, 62, r'$R=\mathbb{Z}$', 'sujet', 'm'); text(ax, 70, 62, r'$R/I$, $I=(4)$', 'autre', 'm')
for i, (a, c) in enumerate([(5, 1), (6, 2), (11, 3)]):
    y = 50 - i * 14
    box(ax, 6, y - 5, 24, 10, 'sujet', label=str(a), size='m')
    box(ax, 56, y - 5, 28, 10, 'autre', label=r'$%d+I$' % c, size='m')
    arrow(ax, (31, y), (55, y), 'varie')
    text(ax, 43, y + 3, r'$\nu$', 'varie', 'm')
text(ax, 44, 9, 'chaque élément va sur sa classe', 'resultat', 's')
save(fig, '52-141')
