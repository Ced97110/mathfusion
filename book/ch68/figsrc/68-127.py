import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(56)
CX = 58
xs, p = bitrow(fig, ax, CX, 50, '4567', 'fixe')
for y, s in ((41, '1001'), (32, '0110')):
    cells(ax, xs, p, y, 8, ['resultat', 'sujet', 'sujet', 'sujet'])
    bitrow(fig, ax, CX, y, s, 'encre')
text(ax, 2, 50, 'position', 'fixe', 's', ha='left')
text(ax, 2, 41, 'message 1001', 'fixe', 's', ha='left')
text(ax, 2, 32, 'message 0110', 'fixe', 's', ha='left')
brace(ax, xs[1] - p / 2 + 0.4, xs[3] + p / 2 - 0.4, 27, 'sujet', label='à additionner', depth=2.0)
text(ax, 44, 13, r'$x_4 = x_5 + x_6 + x_7$', 'resultat', 'l', weight='bold')
text(ax, 44, 6, 'somme des 4 bits : 0', 'resultat', 'm')
crop(fig, ax, 2.2, 56.0)
save(fig, '68-127')
