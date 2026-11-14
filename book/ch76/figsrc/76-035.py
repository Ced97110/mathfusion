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

fig, ax = canvas(92)
text(ax, 44, 85, r'$x=2+3i$ ; $y=1+4i$', 'encre', 'm')
x0, w, h = 28, 26, 12
for j, s in enumerate([r'$1\cdot u_1$', r'$4\cdot u_2$']): text(ax, x0 + w * j + w / 2, 73, s, 'varie', 'm')
for i, s in enumerate([r'$2\cdot u_1$', r'$3\cdot u_2$']):
    yb = 54 - 13 * i
    text(ax, 14, yb + h / 2, s, 'varie', 'm')
    for j in range(2): box(ax, x0 + w * j, yb, w, h, 'fixe', label=r'$u_%du_%d$' % (i + 1, j + 1))
arrow(ax, (54, 40), (54, 34), 'varie')
box(ax, 29, 22, 50, 12, 'resultat', label=r'$xy=-10+11\,i$')
text(ax, 44, 16, 'orange : nombres sortis du produit', 'varie', 's')
text(ax, 44, 11, 'gris : produits lus dans la table', 'fixe', 's')
save(fig, '76-035')
