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

fig, ax = canvas(70)
text(ax, 28, 63, r'table de $C$ sur $R$', 'sujet', 'm')
x0, w, h = 14, 15, 12
for j, s in enumerate([r'$1$', r'$i$']): text(ax, x0 + w * j + w / 2, 53.5, s, 'fixe', 'm')
vals = [[(r'$1$', 'sujet'), (r'$i$', 'sujet')], [(r'$i$', 'sujet'), (r'$-1$', 'varie')]]
for i, s in enumerate([r'$1$', r'$i$']):
    yb = 38 - 12 * i
    text(ax, 8, yb + h / 2, s, 'fixe', 'm')
    for j in range(2): box(ax, x0 + w * j, yb, w, h, vals[i][j][1], label=vals[i][j][0])
text(ax, 66, 50, r'$(1+2i)(3+i)$', 'encre', 'm')
arrow(ax, (66, 47), (66, 41), 'varie')
text(ax, 66, 38, r'$3+i+6i-2$', 'encre', 'm')
arrow(ax, (66, 35), (66, 29), 'varie')
text(ax, 66, 26, r'$=1+7i$', 'resultat', 'm')
text(ax, 44, 9, '4 cases lues, puis une somme', 'fixe', 's')
save(fig, '76-036')
