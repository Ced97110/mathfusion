import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, radians
fig, ax = canvas(82)
degs = [0, 30, 60, 90, 120, 150, 180]
cosv = ['1', '0,866', '0,5', '0', '−0,5', '−0,866', '−1']
rv = ['2', '1,87', '1,5', '1', '0,5', '0,13', '0']
x0 = 22.0; dx = 9.4; base = 28.0
text(ax, 3, 73, 'angle\ncos $\\theta$\n$r$', 'encre', 's', ha='left')
box(ax, 1, 65, 85, 16, 'fixe', fill=False, dash=True)
for i in range(7):
    x = x0 + i * dx
    text(ax, x, 73, f'{degs[i]}°\n{cosv[i]}\n{rv[i]}', 'sujet', 's')
# bars: height proportional to the exact r = 1 + cos, 10 mm per unit; r = 0 gives a flat line
for i, d in enumerate(degs):
    h = 10.0 * (1 + cos(radians(d)))
    x = x0 + i * dx
    if h > 0.05:
        ax.add_patch(Rectangle((x - 3, base), 6, h, ec=COL['resultat'], fc=FILL['resultat'], lw=0.8, zorder=2))
    else:
        disc(ax, x, base, 1.0, 'resultat')
line(ax, [(x0 - 5, base), (x0 + 6 * dx + 5, base)], 'fixe')
text(ax, 3, 40, 'hauteur\n$=r$', 'resultat', 's', ha='left')
box(ax, 1, 4, 85, 15, 'fixe', fill=False, dash=True,
    label='absent : de 180° à 360°\net les angles entre colonnes', size='s')
text(ax, 44, 23.5, 'sept points seulement ; 1,87 est arrondi', 'encre', 's')
save(fig, '40-018')
