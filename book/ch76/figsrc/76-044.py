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

fig, ax = canvas(73)
text(ax, 44, 68, 'deux matrices diagonales', 'encre', 'm')
def dg(x, y, a, b, r):
    grid(ax, x, y, 2, {(0, 0): (a, r), (1, 1): (b, r)}, 7)
dg(22, 50, '2', '3', 'sujet'); dg(52, 50, '5', r'$-1$', 'autre')
for x, a, b, cap in [(4, '7', '2', 'somme'), (34, '10', r'$-3$', 'produit'), (64, '8', '12', '4 fois la 1re')]:
    dg(x, 18, a, b, 'resultat'); text(ax, x + 7, 13, cap, 'resultat', 's')
    arrow(ax, (x + 7, 47), (x + 7, 35), 'varie')
save(fig, '76-044')
