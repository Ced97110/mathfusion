import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
from matplotlib.patches import Arc
fig, ax = canvas(56)
ox, oy, s = 52, 12, 8
P = lambda x, y: (ox + s * x, oy + s * y)
box(ax, 2, 20, 34, 14, 'sujet', label=r'$1\times4+3\times2=10$')
text(ax, 19, 39, 'ne lit que les composantes', 'fixe', 's')
text(ax, 19, 14, '« d’où sort ce nombre ? »', 'fixe', 's')
arrow(ax, (37, 27), (50, 27), 'varie', lw=1.2)
text(ax, 43.5, 31, 'mesure', 'varie', 's')
arrow(ax, P(0, 0), P(1, 3), 'sujet', lw=1.4)
arrow(ax, P(0, 0), P(4, 2), 'autre', lw=1.4)
ax.add_patch(Arc((ox, oy), 18, 18, theta1=math.degrees(math.atan2(2, 4)), theta2=math.degrees(math.atan2(3, 1)), color=COL['resultat'], lw=1.5, zorder=4))
text(ax, 58, 22, r'$45^\circ$', 'resultat', 'm')
text(ax, 58.5, 40, r'$u$', 'sujet', 'm')
text(ax, 85, 30, r'$v$', 'autre', 'm')
text(ax, 68, 6, 'angle entre les flèches', 'resultat', 's')
save(fig, '41-074')
