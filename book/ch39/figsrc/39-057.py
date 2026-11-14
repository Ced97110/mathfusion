import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# 1 + i et −1 − i : même distance, directions différentes
fig, ax = canvas(72)
cx, cy, u = 44, 40, 14
r = math.sqrt(2) * u
arrow(ax, (cx - 29, cy), (cx + 29, cy), 'fixe', lw=0.8)
arrow(ax, (cx, cy - 23), (cx, cy + 23), 'fixe', lw=0.8)
disc(ax, cx, cy, r, 'fixe', fill=False, lw=0.7)
P = (cx + u, cy + u)
Q = (cx - u, cy - u)
line(ax, [(cx, cy), P], 'sujet', lw=1.8)
line(ax, [(cx, cy), Q], 'autre', lw=1.8)
disc(ax, P[0], P[1], 1.5, 'sujet')
disc(ax, Q[0], Q[1], 1.5, 'autre')
ax.add_patch(Arc((cx, cy), 16, 16, theta1=0, theta2=45, ec=COL['varie'], lw=1.0, zorder=3))
ax.add_patch(Arc((cx, cy), 10, 10, theta1=0, theta2=225, ec=COL['varie'], lw=1.0, zorder=3))
text(ax, P[0] + 3, P[1] + 3, '1 + i', 'sujet', 'm', ha='left', weight='bold')
text(ax, Q[0] - 3, Q[1] - 3, '−1 − i', 'autre', 'm', ha='right', weight='bold')
text(ax, cx + 14.5, cy + 4.5, '45°', 'varie', 's')
text(ax, cx - 1.5, cy + 9.5, '225°', 'varie', 's', ha='right')
text(ax, 44, 9, 'même distance ≈ 1,41 :\nla direction les sépare', 'fixe', 'm')
save(fig, '39-057')
