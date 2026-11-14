import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(68)
text(ax, 44, 64, 'code de Hamming (7, 4)', 'sujet', 'l', weight='bold')
text(ax, 44, 58, r'colonne $i$ = $i$ en base 2', 'sujet', 'm')
xs, p = bitrow(fig, ax, 46, 50, '1234567', 'fixe')
text(ax, 7, 50, r'$i$', 'fixe', 'l')
cell(ax, xs[5], 34, p - 1, 24, 'varie')
cell(ax, 46, 34, 7 * p + 1, 24, 'sujet', fill=False, lw=1.0)
text(ax, 7, 34, r'$H$', 'sujet', 'xl')
for y, s in ((41, '0001111'), (34, '0110011'), (27, '1010101')):
    bitrow(fig, ax, 46, y, s, 'encre')
arrow(ax, (xs[5], 21.5), (xs[5], 16.5), 'varie')
text(ax, 58, 12.5, 'colonne 6 : 1, 1, 0 = 110', 'varie', 'm')
crop(fig, ax, 8.3, 68.0)
save(fig, '68-119')
