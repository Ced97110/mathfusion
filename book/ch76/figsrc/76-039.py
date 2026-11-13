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

fig, ax = canvas(62)
text(ax, 44, 57, r'$\delta_{jk}$', 'sujet', 'l')
x0, c = 30, 14
for j in range(2): text(ax, x0 + c * j + c / 2, 50, r'$k=%d$' % (j + 1), 'fixe', 's')
for i in range(2):
    yb = 32 - c * i
    text(ax, 22, yb + c / 2, r'$j=%d$' % (i + 1), 'fixe', 's')
    for j in range(2):
        r = 'resultat' if i == j else 'limite'
        box(ax, x0 + c * j, yb, c, c, r, label='1' if i == j else '0', size='m')
text(ax, 44, 11, r'$j=k$ : le nombre 1', 'resultat', 's')
text(ax, 44, 5, r'$j\neq k$ : le nombre 0', 'limite', 's')
save(fig, '76-039')
