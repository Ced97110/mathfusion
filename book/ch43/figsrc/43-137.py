import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
rows = [['0,1', '2', '3'], ['0,5', '6', '7'], ['0,9', '0', '1']]
xs = [30, 46, 62]
ys = [52, 40, 28]
for r in range(3):
    for c in range(3):
        diag = r == c
        box(ax, xs[c] - 6.5, ys[r] - 4.5, 13, 9, 'varie' if diag else 'fixe', label=rows[r][c], size='m')
text(ax, 10, 52, 'liste', 'fixe', 's')
newr = ['0,2', '7', '2']
for c in range(3):
    box(ax, xs[c] - 6.5, 6, 13, 9, 'resultat', label=newr[c], size='m')
text(ax, 10, 10.5, r'$x$', 'resultat', 'l')
text(ax, 46, 60.5, 'chiffres de la diagonale', 'varie', 's')
text(ax, 46, 21, 'chaque chiffre est changé', 'resultat', 's')
save(fig, '43-137')
