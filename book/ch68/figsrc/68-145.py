import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(66)
CX = 36
xs, p = bitrow(fig, ax, CX, 59, '1234567', 'fixe', size='m', k=5)
text(ax, 66, 59, 'nombre de 1', 'fixe', 's')
cell(ax, xs[5], 40, p - 0.4, 27, 'limite', fill=False, dash=True, lw=1.2)
rows = [('A', 'sujet', 47, {3, 4, 5, 6}, '3 : impair'), ('B', 'varie', 38, {1, 2, 5, 6}, '3 : impair'),
        ('C', 'resultat', 29, {0, 2, 4, 6}, '2 : pair')]
for name, role, y, idx, res in rows:
    cells(ax, xs, p, y, 7, [role if i in idx else '' for i in range(7)])
    bitrow(fig, ax, CX, y, '0011011', 'encre', size='m', k=5)
    text(ax, 7, y, name, role, 'xl', weight='bold')
    text(ax, 62, y, res, role, 'm', ha='left')
arrow(ax, (xs[5], 24.5), (xs[5], 17.5), 'limite', lw=1.2)
box(ax, 20, 3, 62, 14, 'limite', label='$x_6$ est faux\ndans $A$ et $B$, hors de $C$')
crop(fig, ax, 0.0, 63.2)
save(fig, '68-145')
