import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'corps à 3 éléments, dimension 2', 'encre', 's')
x0, y0, s = 26, 14, 16
vals = [[('0', 'fixe'), ('1', 'limite')], [('1', 'limite'), ('2', 'limite')]]
for j in range(2):
    for i in range(2):
        v, r = vals[j][i]
        box(ax, x0 + i * s, y0 + (1 - j) * s, s, s, r, label=v, size='l')
    text(ax, x0 - 4, y0 + (1 - j) * s + s / 2, str(j), 'encre', 's')
    text(ax, x0 + j * s + s / 2, y0 + 2 * s + 4, str(j), 'encre', 's')
text(ax, x0 + s, y0 + 2 * s + 10, r'carré de $x$', 'encre', 's')
text(ax, 10, y0 + s, r'carré de $y$', 'encre', 's', rot=90)
text(ax, 73, 40, 'seul 0 + 0 = 0', 'fixe', 's')
text(ax, 73, 24, 'aucun vecteur', 'limite', 's')
text(ax, 73, 20, 'isotrope', 'limite', 's')
save(fig, '72-155')
