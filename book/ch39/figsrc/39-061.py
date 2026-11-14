import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# θ : l'angle de la direction de 1 + i, depuis l'axe horizontal
fig, ax = canvas(52)
ox, oy, u = 12, 10, 24
arrow(ax, (ox - 6, oy), (ox + 46, oy), 'fixe', lw=0.9)
arrow(ax, (ox, oy - 3), (ox, oy + 36), 'fixe', lw=0.9)
P = (ox + u, oy + u)
line(ax, [(ox, oy), P], 'sujet', lw=2.0)
disc(ax, P[0], P[1], 1.6, 'sujet')
ax.add_patch(Arc((ox, oy), 24, 24, theta1=0, theta2=45, ec=COL['varie'], lw=1.4, zorder=3))
text(ax, P[0] + 3, P[1] + 2, '1 + i', 'sujet', 'm', ha='left', weight='bold')
text(ax, 34, 13.5, 'θ = 45°', 'varie', 's')
box(ax, 52, 36, 34, 12, 'varie', label='θ : la direction\ndu point', size='s')
arrow(ax, (52, 38), (21.8, 16.9), 'varie', lw=0.8)
text(ax, 38, 5, 'axe horizontal', 'fixe', 's')
save(fig, '39-061')
