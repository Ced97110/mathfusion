import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# 41-027 : theta = angle entre l'axe x (est) et la flèche du vent ; 0° = est, 90° = nord
fig, ax = canvas(76)
s = 0.5
O = (14, 10)
V = (O[0] + 100 * s * math.cos(math.radians(60)), O[1] + 100 * s * math.sin(math.radians(60)))
arrow(ax, O, (80, O[1]), 'fixe', lw=0.8)
line(ax, [O, (O[0], O[1] + 56)], 'fixe', dash=True)
arrow(ax, O, V, 'varie', lw=1.6)
r = 14
ax.add_patch(Arc(O, 2 * r, 2 * r, theta1=0, theta2=60, ec=COL['fixe'], lw=1.2, zorder=3))
a = math.radians(30)
text(ax, O[0] + (r + 7) * math.cos(a), O[1] + (r + 7) * math.sin(a), r'$\theta$ = 60°', 'fixe', 'l')
text(ax, 80, O[1] + 3.5, 'axe $x$ (est) : 0°', 'fixe', 's', ha='right')
text(ax, O[0] + 1.5, O[1] + 59, 'nord : 90°', 'fixe', 's', ha='left')
text(ax, V[0] + 2.5, V[1] + 1, '100 km/h', 'varie', 'm', ha='left')
text(ax, O[0] - 3, O[1] - 3.5, '$O$', 'encre')
save(fig, '41-027')
