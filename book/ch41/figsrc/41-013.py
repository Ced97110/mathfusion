import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Échelle 1 mm = 4 km. a = 45 mm ; v = (12,5 ; 21,65) mm. Arrivée : (230 ; 86,6) -> (57,5 ; 21,65) mm depuis le départ.
fig, ax = canvas(76)
k = 4.0
dx, dy = 50 / k, 86.6 / k
L = 180 / k
# Chemin 1 : moteur puis vent
O1 = (8, 44)
text(ax, 4, 72, '1. moteur, puis vent', 'sujet', 'm', ha='left')
arrow(ax, O1, (O1[0] + L, O1[1]), 'sujet', lw=1.4)
arrow(ax, (O1[0] + L, O1[1]), (O1[0] + L + dx, O1[1] + dy), 'varie', lw=1.4)
text(ax, O1[0] + L / 2, O1[1] + 3.2, '180', 'sujet', 's')
text(ax, O1[0] + L + dx + 2, O1[1] + dy / 2 - 3, '50 ; 86,6', 'varie', 's', ha='left')
disc(ax, O1[0] + L + dx, O1[1] + dy, 1.5, 'resultat')
disc(ax, O1[0], O1[1], 1.2, 'encre')
# Chemin 2 : vent puis moteur
O2 = (8, 8)
text(ax, 4, 36, '2. vent, puis moteur', 'varie', 'm', ha='left')
arrow(ax, O2, (O2[0] + dx, O2[1] + dy), 'varie', lw=1.4)
arrow(ax, (O2[0] + dx, O2[1] + dy), (O2[0] + dx + L, O2[1] + dy), 'sujet', lw=1.4)
text(ax, O2[0] + dx + L / 2, O2[1] + dy - 4, '180', 'sujet', 's')
text(ax, O2[0] + dx - 2, O2[1] + dy / 2, '50 ; 86,6', 'varie', 's', ha='right')
disc(ax, O2[0] + dx + L, O2[1] + dy, 1.5, 'resultat')
disc(ax, O2[0], O2[1], 1.2, 'encre')
text(ax, 70, 62.5, 'arrivée', 'resultat', 's', ha='left')
text(ax, 70, 26.5, 'arrivée', 'resultat', 's', ha='left')
save(fig, '41-013')
