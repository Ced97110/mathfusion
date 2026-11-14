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

fig, ax = canvas(48)
c = 6
grid(ax, 4, 22, 2, {(0, 1): ('1', 'sujet')}, c); grid(ax, 26, 22, 2, {(0, 0): ('1', 'sujet')}, c)
grid(ax, 48, 22, 2, {(0, 0): ('1', 'autre'), (1, 1): ('1', 'autre')}, c)
grid(ax, 70, 22, 2, {(0, 0): ('a', 'fixe'), (0, 1): ('b', 'fixe'), (1, 0): ('c', 'fixe'), (1, 1): ('d', 'fixe')}, c)
for x, s, r in [(10, r'$e_{12}$', 'sujet'), (32, r'$e_{11}$', 'sujet'), (54, 'unité : deux 1', 'autre'), (76, 'quelconque', 'fixe')]:
    text(ax, x, 17, s, r, 's')
brace(ax, 4, 38, 36.5, 'sujet', label='un seul 1, le reste nul', down=False)
save(fig, '76-037')
