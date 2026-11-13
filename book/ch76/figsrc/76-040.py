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

fig, ax = canvas(78)
g = lambda x, y, cells: grid(ax, x, y, 3, cells, 4.5)
g(6, 46, {(0, 2): ('1', 'varie')}); text(ax, 24.7, 52, r'$\times$', 'encre'); g(30, 46, {(2, 1): ('1', 'varie')})
eq(ax, 48.7, 52); g(54, 46, {(0, 1): ('1', 'resultat')}); text(ax, 76, 52, r'$e_{12}$', 'resultat')
text(ax, 44, 41, 'milieux 3, 3 : égaux', 'varie', 's')
text(ax, 44, 36.5, 'reste : gauche 1, droite 2', 'resultat', 's')
g(6, 18, {(0, 2): ('1', 'varie')}); text(ax, 24.7, 24, r'$\times$', 'encre'); g(30, 18, {(1, 1): ('1', 'varie')})
eq(ax, 48.7, 24); g(54, 18, {(i, j): (None, 'limite') for i in range(3) for j in range(3)}); text(ax, 76, 24, '0', 'limite')
text(ax, 44, 13, 'milieux 3, 2 : différents', 'varie', 's')
save(fig, '76-040')
