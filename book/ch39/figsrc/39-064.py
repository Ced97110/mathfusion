import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# 3√2 − 3√2 i : module 6, argument 315°
fig, ax = canvas(74)
ox, oy, u = 24, 54, 8
a = 3 * math.sqrt(2)
P = (ox + a * u, oy - a * u)
arrow(ax, (ox - 8, oy), (ox + 50, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy + 16), (ox, oy - 40), 'fixe', lw=0.8)
line(ax, [(P[0], oy), P], 'fixe', lw=0.8, dash=True)
line(ax, [(ox, oy), P], 'sujet', lw=2.0)
disc(ax, P[0], P[1], 1.6, 'sujet')
ax.add_patch(Arc((ox, oy), 20, 20, theta1=0, theta2=315, ec=COL['varie'], lw=1.3, zorder=3))
text(ax, 37, oy - 3.5, '315°', 'varie', 's')
text(ax, P[0] - 3, P[1] - 4.5, 'z = 3√2 − 3√2 i', 'sujet', 'm', ha='right', weight='bold')
text(ax, 32, 70, 'module √(18 + 18) = 6', 'sujet', 's', ha='left')
text(ax, 32, 65, 'arctan(−1) = −45°', 'fixe', 's', ha='left')
text(ax, 32, 60, '−45° + 360° = 315°', 'varie', 's', ha='left')
text(ax, 72, oy - 24, '6 cis 315°', 'resultat', 'm', weight='bold')
save(fig, '39-064')
