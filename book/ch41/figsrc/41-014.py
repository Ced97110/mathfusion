import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# Échelle 1 mm = 3,4 km/h : r = 245,8 -> 72,3 mm à 20,6° au-dessus de l'est.
fig, ax = canvas(62)
ang = 20.6
L = 245.8 / 3.4
O = (6, 22)
R = (O[0] + L * math.cos(math.radians(ang)), O[1] + L * math.sin(math.radians(ang)))
line(ax, [O, (84, O[1])], 'fixe', lw=0.9, dash=True)
arrow(ax, O, R, 'resultat', lw=1.8)
disc(ax, O[0], O[1], 1.4, 'encre')
ax.add_patch(Arc(O, 40, 40, theta1=0, theta2=ang, color=COL['varie'], lw=1.0, zorder=3))
text(ax, 33, 18.8, '20,6°', 'varie', 's')
text(ax, 3, 18, r'$O$', 'encre', 'm', ha='left')
text(ax, 80, 18.5, 'est', 'fixe', 's')
text(ax, 38, 36, 'longueur : 245,8 km/h', 'resultat', 's', rot=ang)
text(ax, 18, 46, r'$r$', 'resultat', 'xl')
box(ax, 2, 2, 42, 9, 'resultat', label='longueur = vitesse')
box(ax, 46, 2, 40, 9, 'varie', label='inclinaison = direction')
save(fig, '41-014')
