import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, 'produit de transvections', 'resultat', 's')
poly(ax, [(4,50),(14,50),(14,60),(4,60)], 'fixe'); text(ax, 9, 45, 'aire 1', 'fixe', 's')
for i in range(3):
    x = 21 + i * 12
    arrow(ax, (x - 4, 55), (x + 1, 55), 'resultat'); box(ax, x + 1.5, 51, 8, 8, 'resultat', label=r'$\tau$', size='s')
arrow(ax, (57, 55), (62, 55), 'resultat')
poly(ax, [(64,50),(74,50),(80,60),(70,60)], 'resultat'); text(ax, 72, 45, 'aire 1', 'resultat', 's')
line(ax, [(4, 38), (84, 38)], 'fixe', dash=True)
text(ax, 44, 32, 'double les positions', 'limite', 's')
poly(ax, [(4,8),(14,8),(14,18),(4,18)], 'fixe'); text(ax, 9, 3.5, 'aire 1', 'fixe', 's')
arrow(ax, (19, 13), (44, 13), 'limite')
poly(ax, [(49,8),(69,8),(69,18),(49,18)], 'limite'); text(ax, 59, 3.5, 'aire 2', 'limite', 's')
text(ax, 86, 13, 'pas un produit', 'limite', 's', ha='right')
save(fig, '75-079')
