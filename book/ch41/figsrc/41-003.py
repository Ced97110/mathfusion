import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(62)
# Gauche : un nombre suffit
text(ax, 17, 56, 'un seul nombre', 'fixe', 's')
box(ax, 4, 34, 26, 14, 'fixe', label='20 degrés')
box(ax, 4, 14, 26, 14, 'fixe', label='5 kg')
line(ax, [(36, 6), (36, 58)], 'fixe', lw=0.6, dash=True)
# Droite : le vent demande grandeur et direction
text(ax, 62, 56, 'deux informations', 'sujet', 's')
O = (44, 14)
line(ax, [O, (84, 14)], 'fixe', lw=0.9)
text(ax, 80, 10.5, 'est', 'fixe', 's')
L = 34
ex, ey = O[0] + L * math.cos(math.radians(60)), O[1] + L * math.sin(math.radians(60))
arrow(ax, O, (ex, ey), 'sujet', lw=1.3)
ax.add_patch(Arc(O, 22, 22, theta1=0, theta2=60, color=COL['varie'], lw=0.9, zorder=3))
text(ax, 58, 19, '60°', 'varie', 's')
text(ax, 72, 30, 'grandeur : 100 km/h', 'sujet', 's')
text(ax, 72, 24, 'direction : 60°', 'varie', 's')
save(fig, '41-003')
