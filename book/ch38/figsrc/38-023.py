import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig, ax = canvas(60)
gy = 8
E = (12, 14)
X = 52                                   # abscisse de l'arbre
top = E[1] + (X - E[0]) * math.tan(math.radians(40))
line(ax, [(2, gy), (86, gy)], 'fixe')
line(ax, [(12, gy), E], 'fixe', lw=1.6)
disc(ax, E[0], E[1], 1.8, 'sujet')
line(ax, [E, (X, E[1])], 'fixe', lw=0.9, dash=True)
line(ax, [E, (X, top)], 'sujet', lw=1.5)
ax.add_patch(Arc(E, 28, 28, theta1=0, theta2=40, ec=COL['varie'], lw=1.4, zorder=3))
text(ax, 30, E[1] + 4.2, '40°', 'varie', 'm')
line(ax, [(X, gy), (X, top)], 'fixe', lw=2.2)
disc(ax, X, top + 3, 4, 'fixe')
arrow(ax, (X + 9, gy), (X + 9, top), 'resultat', lw=1.0, both=True)
text(ax, X + 10, (gy + top) / 2, '? m', 'resultat', 'm', ha='left')
text(ax, 22, 54, 'l’instrument donne : 40°', 'varie', 's')
save(fig, '38-023')
