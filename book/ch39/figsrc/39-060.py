import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# r = |z| : une même longueur, deux écritures
fig, ax = canvas(62)
ox, oy, u = 14, 8, 20
arrow(ax, (ox - 6, oy), (ox + 56, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy - 3), (ox, oy + 46), 'fixe', lw=0.8)
ax.add_patch(Arc((ox, oy), 4 * u, 4 * u, theta1=0, theta2=90, ec=COL['fixe'], lw=0.7, ls='--', zorder=1))
P = (ox + 2 * u * math.cos(math.radians(60)), oy + 2 * u * math.sin(math.radians(60)))
line(ax, [(ox, oy), P], 'sujet', lw=2.2)
disc(ax, P[0], P[1], 1.7, 'sujet')
text(ax, 18, oy + 25, 'r = 2', 'sujet', 'm', ha='center', weight='bold')
text(ax, 31.5, oy + 14, '|z| = 2', 'sujet', 'm', ha='left', weight='bold')
text(ax, P[0] + 3, P[1] + 3, '2 cis 60°', 'sujet', 'm', ha='left')
box(ax, 54, 22, 30, 9, 'sujet', label='r = |z|', size='m', weight='bold')
text(ax, ox - 2.5, oy - 3, 'O', 'fixe', 's')
save(fig, '39-060')
