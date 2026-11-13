import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(92)
cx, cy, R = 44, 52, 24
pos = []
for k in range(10):
    a = math.radians(90 - 36 * k)
    pos.append((cx + R * math.cos(a), cy + R * math.sin(a)))
for k, (x, y) in enumerate(pos):
    disc(ax, x, y, 3.6, 'fixe' if k == 0 else 'sujet', label=str(k), size='s')
# flèche +y2 entre 0 et 1 puis retour 9 -> 0
arrow(ax, (pos[0][0] + 4.5, pos[0][1] + 0.5), (pos[1][0] - 1.5, pos[1][1] + 4.2), 'varie', curve=-0.2)
text(ax, 60, 80, '+ y₂', 'varie', 's')
text(ax, cx, cy, 'k·y₂, k = 0 à 9', 'sujet', 's')
text(ax, cx, 14, '10·y₂ = 0 : retour au départ', 'resultat', 's')
text(ax, 22, 6, 'ann y₂ = (10)', 'resultat', 's')
text(ax, 66, 6, 'Dy₂ ≅ ℤ/(10)', 'sujet', 's')
save(fig, '59-098')
