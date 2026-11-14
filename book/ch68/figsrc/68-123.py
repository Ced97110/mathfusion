import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(66)
CX = 50
xs, p = bitrow(fig, ax, CX, 58, '1234567', 'fixe')
for i in (0, 2, 4, 6):
    cell(ax, xs[i], 46, p - 0.8, 20, 'resultat')
cell(ax, xs[0], 41, p - 0.8, 8, 'limite')
bitrow(fig, ax, CX, 51, '0011001', 'encre')
bitrow(fig, ax, CX, 41, '1011001', 'encre')
text(ax, 8, 58, 'place', 'fixe', 's')
text(ax, 8, 51, 'mot', 'fixe', 's')
text(ax, 8, 41, '1er bit', 'limite', 's')
text(ax, 8, 37.5, 'inversé', 'limite', 's')
text(ax, 44, 28, r'ligne $C$ : positions 1, 3, 5, 7', 'resultat', 'm', weight='bold')
text(ax, 44, 19, r'$0 + 1 + 0 + 1 = 0$ : vérifiée', 'resultat', 'm')
text(ax, 44, 11, r'$1 + 1 + 0 + 1 = 1$ : fausse', 'limite', 'm')
crop(fig, ax, 7.2, 62.5)
save(fig, '68-123')
