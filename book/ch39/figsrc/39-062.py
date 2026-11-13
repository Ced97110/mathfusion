import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# cis 60° : le point du cercle de rayon 1
fig, ax = canvas(64)
cx, cy, u = 28, 30, 24
arrow(ax, (cx - 27, cy), (cx + 27, cy), 'fixe', lw=0.8)
arrow(ax, (cx, cy - 26), (cx, cy + 26), 'fixe', lw=0.8)
disc(ax, cx, cy, u, 'fixe', fill=False, lw=0.7)
P = (cx + u * 0.5, cy + u * math.sin(math.radians(60)))
line(ax, [(cx, cy), (P[0], cy)], 'varie', lw=1.8)
line(ax, [(P[0], cy), P], 'autre', lw=1.8)
line(ax, [(cx, cy), P], 'sujet', lw=1.8)
disc(ax, P[0], P[1], 1.6, 'sujet')
ax.add_patch(Arc((cx, cy), 12, 12, theta1=0, theta2=60, ec=COL['fixe'], lw=0.8, zorder=3))
text(ax, P[0] + 1, P[1] + 5.5, 'cis 60° ≈ 0,5 + 0,866 i', 'sujet', 'm', weight='bold')
text(ax, (cx + P[0]) / 2, cy - 4, 'cos 60° = 0,5', 'varie', 's')
text(ax, 56, cy + 10, 'sin 60°\n≈ 0,866', 'autre', 's', ha='left')
arrow(ax, (55.5, cy + 10), (P[0] + 0.7, cy + 10), 'autre', lw=0.7)
text(ax, 11, 56, 'rayon 1', 'fixe', 's')
save(fig, '39-062')
