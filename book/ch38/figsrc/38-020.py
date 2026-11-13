import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig, ax = canvas(50)
gy = 8
E = (10, 18)
line(ax, [(2, gy), (86, gy)], 'fixe')
line(ax, [(10, gy), E], 'fixe', lw=1.6)
disc(ax, E[0], E[1], 1.8, 'sujet')
line(ax, [E, (84, E[1])], 'fixe', lw=1.0, dash=True)
T = (78, E[1] + 68 * math.tan(math.radians(18)))
line(ax, [E, T], 'sujet', lw=1.6)
disc(ax, T[0], T[1], 1.3, 'autre')
ax.add_patch(Arc(E, 44, 44, theta1=0, theta2=18, ec=COL['varie'], lw=1.4, zorder=3))
text(ax, 38, E[1] + 5.4, '18°', 'varie', 'm')
text(ax, 60, E[1] - 4, 'horizontale', 'fixe', 's')
text(ax, 44, 40, 'angle d’élévation', 'varie', 'm')
text(ax, 74, T[1] + 4.5, 'point plus haut', 'autre', 's')
text(ax, 10, 25, 'œil', 'sujet', 's')
save(fig, '38-020')
