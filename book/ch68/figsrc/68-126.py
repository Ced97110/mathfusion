import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(72)
CX = 50
xs, p = bitrow(fig, ax, CX, 66, '1234567', 'fixe')
roles = ['', 'resultat', 'sujet', '', 'fixe', 'sujet', 'sujet']
cells(ax, xs, p, 55, 8, roles)
for i in (0, 3):
    cell(ax, xs[i], 55, p - 0.8, 8, 'fixe', fill=False, dash=True)
bitrow(fig, ax, CX, 55, BL + '01' + BL + '001', 'encre')
box(ax, 29, 25, 34, 9, 'resultat', label=r'$1 + 0 + 1 = 0$')
arrow(ax, (xs[2], 50.5), (xs[2], 34.8), 'varie')
arrow(ax, (xs[5], 50.5), (58, 34.8), 'varie')
arrow(ax, (xs[6], 50.5), (62, 34.8), 'varie')
arrow(ax, (31, 34.8), (xs[1], 50.5), 'varie')
text(ax, 6, 17, '1. lire les bits 3, 6 et 7', 'varie', 'm', ha='left')
text(ax, 6, 11, '2. les additionner', 'varie', 'm', ha='left')
text(ax, 6, 5, '3. écrire le résultat en 2', 'varie', 'm', ha='left')
save(fig, '68-126')
