import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

cx, cy, k = 44, 40, 7.0  # mm par km
fig, ax = canvas(80)
arrow(ax, (6, cy), (84, cy), 'fixe', lw=0.6)
arrow(ax, (cx, 6), (cx, 76), 'fixe', lw=0.6)
bx, by = cx - 4 * k, cy + 4 * k
fx, fy = cx + 4 * k, cy - 4 * k
line(ax, [(cx, cy), (bx, by)], 'sujet', lw=1.5)
line(ax, [(cx, cy), (fx, fy)], 'limite', lw=0.9, dash=True)
ax.add_patch(Arc((cx, cy), 18, 18, theta1=0, theta2=135, ec=COL['varie'], lw=1.2, zorder=3))
ax.add_patch(Arc((cx, cy), 28, 28, theta1=-45, theta2=0, ec=COL['limite'], lw=1.0, ls='--', zorder=3))
disc(ax, bx, by, 1.5, 'sujet')
disc(ax, fx, fy, 1.5, 'limite', fill=False)
disc(ax, cx, cy, 1.3, 'fixe')
text(ax, bx + 3, by + 1.5, r'bateau $(-4,\ 4)$', 'sujet', 's', ha='left')
text(ax, 28, 50, '$r=4\\sqrt{2}$\n≈ 5,66 km', 'sujet', 's', ha='right')
text(ax, cx + 6, cy + 12, '135°', 'varie', 's')
text(ax, cx + 20, cy - 4, '−45°', 'limite', 's')
text(ax, fx - 1, fy - 4, r'$(4,\ -4)$ : mauvais point', 'limite', 's', ha='right')
text(ax, cx - 3, cy - 3.5, 'phare', 'fixe', 's', ha='right')
save(fig, '39-110')
