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
text(ax, 44, 66, r'$u_iu_j=\sum_k\gamma_{ijk}\,u_k$', 'encre', 'l')
rows = [('choisir', r'$u_2=i$ et $u_2=i$', 'sujet'), ('multiplier', r'$i\times i=-1$', 'varie'),
        ('écrire dans la base', r'$-1\,u_1+0\,u_2$', 'sujet'), ('lire les nombres', r'$\gamma_{221}=-1$ ; $\gamma_{222}=0$', 'resultat')]
for k, (a, b, r) in enumerate(rows):
    y = 50 - 14 * k
    box(ax, 2, y, 30, 10, 'fixe', label=a, size='s')
    box(ax, 36, y, 50, 10, r, label=b)
    if k < 3: arrow(ax, (17, y), (17, y - 4), 'varie')
save(fig, '76-033')
