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

fig, ax = canvas(40)
g = lambda x, cells: grid(ax, x, 16, 2, cells, 8)
g(7, {(0, 0): ('1', 'sujet')}); text(ax, 29, 24, '+', 'encre', 'l'); g(33, {(1, 1): ('1', 'sujet')})
eq(ax, 55, 24); g(59, {(0, 0): ('1', 'resultat'), (1, 1): ('1', 'resultat')})
for x, s, r in [(15, r'$e_{11}$', 'sujet'), (41, r'$e_{22}$', 'sujet'), (67, r'$1$', 'resultat')]: text(ax, x, 11, s, r, 's')
text(ax, 44, 4, r'$n$ lignes : $e_{11}+\cdots+e_{nn}$', 'encre', 's')
save(fig, '76-042')
