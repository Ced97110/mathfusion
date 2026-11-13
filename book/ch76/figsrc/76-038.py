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

fig, ax = canvas(72)
text(ax, 44, 65, r'$e_{ij}\,e_{kl}=\delta_{jk}\,e_{il}$', 'encre', 'l')
g = lambda x, y, cells: grid(ax, x, y, 2, cells, 6)
g(6, 42, {(0, 1): ('1', 'sujet')}); text(ax, 24, 48, r'$\times$', 'encre'); g(30, 42, {(1, 0): ('1', 'autre')})
eq(ax, 48, 48); g(54, 42, {(0, 0): ('1', 'resultat')}); text(ax, 76, 48, r'$e_{11}$', 'resultat')
text(ax, 36, 37, 'milieux 2, 2 : égaux', 'varie', 's')
g(6, 14, {(0, 1): ('1', 'sujet')}); text(ax, 24, 20, r'$\times$', 'encre'); g(30, 14, {(0, 1): ('1', 'autre')})
eq(ax, 48, 20); g(54, 14, zero()); text(ax, 76, 20, '0', 'limite')
text(ax, 36, 9, 'milieux 2, 1 : différents', 'varie', 's')
save(fig, '76-038')
