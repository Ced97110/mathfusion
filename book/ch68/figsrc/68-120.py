import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(62)
CX = 42
xs, p = bitrow(fig, ax, CX, 54, '1234567', 'fixe')
rows = [('A', '0001111', 'sujet', 44, 4), ('B', '0110011', 'varie', 36, 2), ('C', '1010101', 'resultat', 28, 1)]
cell(ax, xs[5], 36, p - 1, 28, 'fixe', fill=False, dash=True, lw=1.0)
for name, s, role, y, w in rows:
    for x, ch in zip(xs, s):
        if ch == '1': disc(ax, x, y, 3.3, role)
    bitrow(fig, ax, CX, y, s, 'encre')
    text(ax, 7, y, name, role, 'xl', weight='bold')
    text(ax, 80, y, f'vaut {w}', role, 's')
arrow(ax, (xs[5], 21), (xs[5], 16.5), 'fixe')
text(ax, 58, 12, 'colonne 6 : 4 + 2 + 0 = 6', 'resultat', 'm')
crop(fig, ax, 8.2, 58.5)
save(fig, '68-120')
