import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
s = 16
ox, oy = 52, 14
arrow(ax, (4, oy), (86, oy), 'fixe', lw=0.7)
arrow(ax, (ox, 5), (ox, 50), 'fixe', lw=0.5)
# droite 8x − 3y + 10 = 0 : x = (3y − 10)/8
line(ax, [(ox + s * (3 * y - 10) / 8, oy + s * y) for y in (-0.8, 2.6)], 'sujet', lw=1.4)
Px = ox - 1.25 * s
arrow(ax, (ox, oy), (Px + 1, oy), 'varie', lw=1.6)
disc(ax, Px, oy, 1.4, 'resultat')
disc(ax, ox, oy, 1.1, 'fixe')
text(ax, ox + 3, oy - 3, 'O', 'fixe', 's')
text(ax, Px, oy - 4.3, '(−1,25 ; 0)', 'resultat', 's')
text(ax, 66, 21, 'r = −1,25 : on recule', 'varie', 's')
text(ax, 80, 9, 'θ = 0', 'fixe', 's')
text(ax, 60, 4, '8 × (−1,25) + 10 = 0', 'resultat', 's')
text(ax, 62, 55, 'droite 8x − 3y + 10 = 0', 'sujet', 's')
save(fig, '40-108')
