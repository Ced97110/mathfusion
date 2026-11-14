import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(76)
CX = 53
xs, p = bitrow(fig, ax, CX, 68, '1234567', 'fixe')
cells(ax, xs, p, 55, 8, ['', '', 'sujet', '', 'sujet', 'sujet', 'sujet'])
bitrow(fig, ax, CX, 55, BL * 2 + '1' + BL + '001', 'encre')
cells(ax, xs, p, 40, 8, ['resultat', 'resultat', '', 'resultat', '', '', ''])
bitrow(fig, ax, CX, 40, '00' + BL + '1' + BL * 3, 'encre')
cells(ax, xs, p, 25, 8, ['resultat', 'resultat', 'sujet', 'resultat', 'sujet', 'sujet', 'sujet'])
bitrow(fig, ax, CX, 25, '0011001', 'encre')
text(ax, 2, 55, '1. placer\nle message', 'sujet', 's', ha='left')
text(ax, 2, 40, '2. calculer\nles contrôles', 'resultat', 's', ha='left')
text(ax, 2, 25, '3. lire\nle mot c', 'encre', 's', ha='left')
for y0, y1 in ((50, 45), (35, 30)):
    arrow(ax, (CX, y0), (CX, y1), 'varie')
crop(fig, ax, 17.8, 72.5)
save(fig, '68-128')
