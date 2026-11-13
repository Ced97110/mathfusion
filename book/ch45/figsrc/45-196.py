import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
bw, bh, y = 25.0, 13.0, 56.0
box(ax, 1, y, 24, bh, 'sujet', label='PGCD(3, 4) = 1', size='s')
box(ax, 29, y, 32, bh, 'varie', label='PGCD × PPCM = mn', size='s', weight='bold')
box(ax, 65, y, 22, bh, 'resultat', label='PPCM = 12', size='s')
arrow(ax, (25, y + bh / 2), (29, y + bh / 2), 'fixe'); arrow(ax, (61, y + bh / 2), (65, y + bh / 2), 'fixe')
text(ax, 13, y + bh + 3, 'départ', 'sujet', 's'); text(ax, 45, y + bh + 3, 'étape clé', 'varie', 's'); text(ax, 76, y + bh + 3, 'arrivée', 'resultat', 's')
s, x0, y0 = 8.5, 27.0, 8.0
for i in range(3):
    for j in range(4):
        box(ax, x0 + j * s, y0 + i * s, s, s, 'resultat', r=0.6)
text(ax, 14, y0 + 13, '3 × 4 = 12', 'resultat', 'm')
text(ax, 14, y0 + 8, 'états', 'resultat', 's')
text(ax, 44, 44, '(1, 1) les atteint tous', 'encre', 's')
save(fig, '45-196')
