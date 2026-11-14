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

fig, ax = canvas(60)
g = lambda x, y, cells: grid(ax, x, y, 2, cells, 6)
text(ax, 44, 54, r'$e_{12}\,e_{21}=e_{11}$', 'encre', 'm')
g(6, 38, {(0, 1): ('1', 'sujet')}); text(ax, 24, 44, r'$\times$', 'encre'); g(30, 38, {(1, 0): ('1', 'autre')})
eq(ax, 48, 44); g(54, 38, {(0, 0): ('1', 'resultat')})
text(ax, 60, 34, r'$\neq$', 'limite', 'l')
text(ax, 44, 29, r'$e_{21}\,e_{12}=e_{22}$', 'encre', 'm')
g(6, 13, {(1, 0): ('1', 'autre')}); text(ax, 24, 19, r'$\times$', 'encre'); g(30, 13, {(0, 1): ('1', 'sujet')})
eq(ax, 48, 19); g(54, 13, {(1, 1): ('1', 'resultat')})
text(ax, 44, 5, 'l’ordre change le résultat', 'limite', 's')
save(fig, '76-041')
