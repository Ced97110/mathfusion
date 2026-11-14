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

fig, ax = canvas(80)
text(ax, 44, 74, r'$A$ : 2 et 5 ; $B$ : 7 et $-1$', 'encre', 'm')
text(ax, 48, 66, r'$\varphi$ : seconde case', 'varie', 's')
rows = [(r'$A+B$', '9', '4', r'$4=5+(-1)$'), (r'$A\times B$', '14', r'$-5$', r'$-5=5\times(-1)$'), (r'$3A$', '6', '15', r'$15=3\times5$')]
for k, (lab, a, b, res) in enumerate(rows):
    yc = 54 - 20 * k
    text(ax, 4, yc, lab, 'encre', 's', ha='left')
    grid(ax, 26, yc - 7, 2, {(0, 0): (a, 'sujet'), (1, 1): (b, 'varie')}, 7)
    arrow(ax, (42, yc), (54, yc), 'varie')
    text(ax, 72, yc, res, 'resultat', 's')
save(fig, '76-048')
