import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grid(ax, x, y, n, cells, c=6.0):
    """n x n cases de coin bas-gauche (x, y) ; cells : {(ligne, colonne): (texte ou None, role)}."""
    for i in range(n):
        for j in range(n):
            lab, r = cells.get((i, j), (None, 'fixe'))
            box(ax, x + j * c, y + (n - 1 - i) * c, c, c, r, label=lab, size='s', r=0.3, lw=0.6)

def eq(ax, x, y, w=3.6):
    line(ax, [(x - w / 2, y + 0.9), (x + w / 2, y + 0.9)], 'encre', lw=0.9)
    line(ax, [(x - w / 2, y - 0.9), (x + w / 2, y - 0.9)], 'encre', lw=0.9)

def zero(n=2):
    return {(i, j): (None, 'limite') for i in range(n) for j in range(n)}

fig, ax = canvas(64)
c = 7
for x, a, b in [(4, '2', '5'), (32, '7', '5'), (60, '2', '3')]:
    grid(ax, x, 38, 2, {(0, 0): (a, 'fixe'), (1, 1): (b, 'varie')}, c)
brace(ax, 4, 46, 54, 'resultat', label='même classe', down=False)
disc(ax, 25, 22, 5.5, 'resultat', label='5', size='m'); disc(ax, 67, 22, 5.5, 'resultat', label='3', size='m')
arrow(ax, (11, 37), (22, 27), 'varie'); arrow(ax, (39, 37), (28, 27), 'varie'); arrow(ax, (67, 37), (67, 28), 'varie')
text(ax, 44, 8, 'classe = seconde case', 'varie', 's')
save(fig, '76-047')
