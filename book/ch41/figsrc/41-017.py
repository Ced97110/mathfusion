import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Deux vents de 100 km/h sur la même droite est-ouest. Échelle 1 mm = 3,4 km/h -> 29,4 mm.
fig, ax = canvas(60)
L = 100 / 3.4
M = 44
y = 50
arrow(ax, (M, y), (M + L, y), 'sujet', lw=1.6)
arrow(ax, (M, y), (M - L, y), 'autre', lw=1.6)
disc(ax, M, y, 1.3, 'encre')
text(ax, M + L / 2, y + 4, 'vent vers l’est', 'sujet', 's')
text(ax, M - L / 2, y + 4, 'vent vers l’ouest', 'autre', 's')
# Autres manuels : une direction (la droite)
brace(ax, M - L, M + L, 41, 'fixe', label='autres manuels : 1 direction')
# Ce livre : deux directions (droite + côté)
brace(ax, M - L, M - 1, 26, 'autre', label='direction 1 : ouest')
brace(ax, M + 1, M + L, 26, 'sujet', label='direction 2 : est')
text(ax, 44, 9, 'direction = droite + côté', 'encre', 'm', weight='bold')
save(fig, '41-017')
