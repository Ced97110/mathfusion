import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(64)
text(ax, 20, 56, r'$G$ : 15 éléments', 'sujet', 'm')
for i in range(3):
    for j in range(5):
        disc(ax, 6 + 6 * j, 46 - 7 * i, 2.2, 'varie' if (i, j) == (0, 0) else 'sujet')
text(ax, 20, 22, r'$xy$ : ordre 15', 'varie', 's')
arrow(ax, (38, 38), (49, 38), 'resultat'); text(ax, 43.5, 43, '≅', 'resultat', 'xl')
cx, cy, R = 68, 38, 14
for k in range(15):
    a = math.radians(24 * k)
    disc(ax, cx + R * math.sin(a), cy + R * math.cos(a), 2.0, 'resultat')
text(ax, cx, cy, 'ℤ/15ℤ', 'resultat', 'm')
text(ax, cx, 56, 'horloge à 15 heures', 'resultat', 's')
text(ax, 44, 8, r'tous = puissances de $xy$', 'encre', 'm')
save(fig, '50-172')
