import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# Échelle 1 mm = 2 km/h : 100 km/h -> 50 mm, à 60° de l'est.
fig, ax = canvas(62)
O = (10, 8)
L = 100 / 2.0
V = (O[0] + L * math.cos(math.radians(60)), O[1] + L * math.sin(math.radians(60)))
line(ax, [O, (O[0] + 50, O[1])], 'fixe', lw=0.9, dash=True)
arrow(ax, O, V, 'varie', lw=1.6)
disc(ax, O[0], O[1], 1.5, 'encre')
ax.add_patch(Arc(O, 20, 20, theta1=0, theta2=60, color=COL['fixe'], lw=0.9, zorder=3))
text(ax, 24, 11.5, '60°', 'fixe', 's')
text(ax, 5.5, 4.5, r'$O$', 'encre', 'm')
text(ax, 61, 4.5, 'est', 'fixe', 's')
text(ax, 17, 36, r'$v$', 'varie', 'xl')
box(ax, 47, 38, 38, 9, 'varie', label='longueur : 100 km/h')
box(ax, 47, 26, 38, 9, 'varie', label='direction : 60° de l’est')
text(ax, 66, 52, r'$v$ dit les deux', 'varie', 's')
save(fig, '41-011')
