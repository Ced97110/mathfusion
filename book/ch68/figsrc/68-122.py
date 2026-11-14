import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(66)
CX = 50
xs, p = bitrow(fig, ax, CX, 58, '1234567', 'fixe')
for i in (1, 2, 5, 6):
    cell(ax, xs[i], 46, p - 0.8, 20, 'varie')
bitrow(fig, ax, CX, 51, '0011001', 'encre')
bitrow(fig, ax, CX, 41, '0011011', 'encre')
text(ax, 8, 58, 'place', 'fixe', 's')
text(ax, 8, 51, 'mot 1', 'fixe', 's')
text(ax, 8, 41, 'mot 2', 'fixe', 's')
text(ax, 44, 28, r'ligne $B$ : positions 2, 3, 6, 7', 'varie', 'm', weight='bold')
text(ax, 44, 19, r'$0 + 1 + 0 + 1 = 0$ : vérifiée', 'resultat', 'm')
text(ax, 44, 11, r'$0 + 1 + 1 + 1 = 1$ : fausse', 'limite', 'm')
crop(fig, ax, 7.2, 62.5)
save(fig, '68-122')
