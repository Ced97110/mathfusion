import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(60)
L = 25.0
c30 = math.cos(math.radians(30)); s30 = math.sin(math.radians(30))
# ligne du haut : poignée à 30°
A1 = (6, 36)
arrow(ax, A1, (A1[0] + L * c30, A1[1] + L * s30), 'sujet', lw=1.5)
arrow(ax, (6, 32), (56, 32), 'fixe', lw=1.2)
text(ax, 22, 56, 'poignée à 30°', 'sujet', 'm')
text(ax, 12, 44.5, '50 N', 'sujet', 's')
text(ax, 31, 28.5, '20 m', 'fixe', 's')
box(ax, 62, 30, 24, 10, 'resultat', label=r'$W\approx 866$ J', size='s')
# ligne du bas : poignée à plat
A2 = (6, 12)
arrow(ax, A2, (A2[0] + L, A2[1]), 'sujet', lw=1.5)
arrow(ax, (6, 8), (56, 8), 'fixe', lw=1.2)
text(ax, 22, 21, 'poignée à plat', 'sujet', 'm')
text(ax, 18, 15.5, '50 N', 'sujet', 's')
text(ax, 31, 4, '20 m', 'fixe', 's')
box(ax, 62, 6, 24, 10, 'resultat', label=r'$W=1\,000$ J', size='s')
save(fig, '41-141')
