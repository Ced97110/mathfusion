import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, 'une case = une direction', 'encre', 'm')
cw, g, x0 = 15, 1.5, 34
def row(y, n, k, lab, klab):
    for i in range(n):
        box(ax, x0 + i * (cw + g), y, cw, 12, 'varie' if i < k else 'resultat', label='réflexion' if i < k else 'fixe', size='s')
    text(ax, 16, y + 6, lab, 'encre', 's')
    brace(ax, x0 + 1, x0 + k * (cw + g) - g - 1, y, 'varie', klab)
    xs = x0 + k * (cw + g)
    brace(ax, xs + 1, x0 + n * (cw + g) - g - 1, y, 'resultat', r'$n-k\geq 1$')
row(40, 3, 2, 'rotation, n = 3', r'$k=2$ : changent')
row(14, 2, 1, 'impropre, n = 2', r'$k=1$')
text(ax, 44, 3, 'au moins 1 direction reste fixe', 'resultat', 's')
save(fig, '72-148')
