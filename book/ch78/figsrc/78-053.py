import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for x0, role, name, prod in [(2, 'fixe', r'$A$', r'produit : $xy$'), (48, 'sujet', r'$A^{-}$', r'crochet : $xy-yx$')]:
    box(ax, x0, 8, 38, 36, role)
    text(ax, x0 + 19, 38, name, role, 'xl')
    disc(ax, x0 + 10, 26, 4.5, 'autre', label=r'$x$'); disc(ax, x0 + 28, 26, 4.5, 'autre', label=r'$y$')
    text(ax, x0 + 19, 14, prod, role, 's')
arrow(ax, (40, 26), (48, 26), 'varie')
text(ax, 44, 3, 'mêmes éléments, produit changé', 'varie', 's')
save(fig, '78-053')
