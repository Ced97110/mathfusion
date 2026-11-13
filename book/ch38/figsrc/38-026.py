import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

fig, ax = canvas(62)
g = 8.0
E = (10, g)                       # l'endroit où l'on se tient
d = 45.0
top = (E[0] + d, g + d * math.tan(math.radians(40)))   # sommet, visé à 40°
line(ax, [(4, g), (84, g)], 'fixe')
box(ax, E[0] + d, g, 8, top[1] - g, 'fixe', fill=True)   # la tour
disc(ax, E[0], g, 1.2, 'encre')
# horizontale et visée
line(ax, [E, (E[0] + d, g)], 'fixe', dash=True)
line(ax, [E, top], 'sujet', lw=1.3)
ax.add_patch(Arc(E, 2 * 16, 2 * 16, theta1=0, theta2=40, color=COL['varie'], lw=1.2, zorder=3))
text(ax, E[0] + 22, g + 4.2, r'$\theta$ = 40°', 'varie', 'm', weight='bold')
text(ax, 12, g - 3.5, 'vous', 'encre', 's', ha='left')
text(ax, E[0] + d + 4, g - 3.5, 'tour', 'fixe', 's')
text(ax, E[0] + d - 2, top[1] + 3.5, 'sommet', 'sujet', 's', ha='right')
text(ax, 30, g - 3.5, 'horizontale', 'fixe', 's')
text(ax, 22, 30, 'visée', 'sujet', 's', ha='right')
save(fig, '38-026')
