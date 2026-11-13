import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
box(ax, 2, 76, 18, 10, 'sujet', label=r'$x$')
arrow(ax, (20, 81), (60, 81), 'varie'); text(ax, 40, 85.5, r'multiplier par $a=2$', 'varie', 's')
box(ax, 60, 76, 26, 10, 'resultat', label=r'$a\,x$')
text(ax, 44, 68, r'linéaire : somme et multiple respectés', 'encre', 's')
box(ax, 2, 55, 40, 9, 'fixe', label=r'$5\to10,\ 7\to14$', size='s')
box(ax, 46, 55, 40, 9, 'fixe', label=r'$12\to24=10+14$', size='s')
box(ax, 24, 43, 40, 9, 'fixe', label=r'$15\to30=3\times10$', size='s')
arrow(ax, (44, 42), (44, 36), 'varie')
for r, row in enumerate([('2', '0'), ('0', '2')]):
    for c, v in enumerate(row):
        box(ax, 30 + c * 14, 12 + (1 - r) * 11, 14, 11, 'autre', label=v, size='l')
text(ax, 44, 5, r'matrice de $x\mapsto2x$', 'autre', 's')
save(fig, '77-006')
