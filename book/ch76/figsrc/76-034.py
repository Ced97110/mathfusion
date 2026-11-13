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
text(ax, 44, 60, 'constantes de structure', 'sujet', 'm')
x0, w, h = 26, 28, 12
cols = [r'$1$', r'$i$']; vals = [[r'$(1\,;\,0)$', r'$(0\,;\,1)$'], [r'$(0\,;\,1)$', r'$(-1\,;\,0)$']]
text(ax, 20, 51, r'$\times$', 'fixe')
for j in range(2): text(ax, x0 + w * j + w / 2, 51, cols[j], 'fixe', 'm')
for i in range(2):
    yb = 34 - 12 * i
    text(ax, 20, yb + h / 2, cols[i], 'fixe', 'm')
    for j in range(2): box(ax, x0 + w * j, yb, w, h, 'sujet', label=vals[i][j])
brace(ax, x0, x0 + 2 * w, 22, 'sujet', label=r'8 nombres = $\gamma_{ijk}$')
text(ax, 54, 11, r'devant 1 ; devant $i$', 'fixe', 's')
save(fig, '76-034')
