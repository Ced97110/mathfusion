import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(62)
CX = 50
xs, p = bitrow(fig, ax, CX, 54, '1234567', 'fixe')
cells(ax, xs, p, 44, 8, ['fixe'] * 3 + ['sujet'] * 4)
bitrow(fig, ax, CX, 44, '0011001', 'encre')
text(ax, 8, 44, 'mot', 'fixe', 's')
text(ax, 8, 54, 'place', 'fixe', 's')
brace(ax, xs[3] - p / 2 + 0.4, xs[6] + p / 2 - 0.4, 39.5, 'sujet', depth=2.2)
text(ax, 44, 26, r'ligne $A$ : $1 + 0 + 0 + 1 = 0$', 'resultat', 'l', weight='bold')
text(ax, 44, 17, 'équation vérifiée', 'resultat', 'm')
text(ax, 44, 8, r'mot 0011011 : $1 + 0 + 1 + 1 = 1$', 'limite', 'm')
crop(fig, ax, 4.3, 58.5)
save(fig, '68-121')
