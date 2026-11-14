import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# forme polaire : r = 2 et θ = 60° donnent a = 1 et b = √3
fig, ax = canvas(64)
ox, oy, u = 14, 10, 20
arrow(ax, (ox - 6, oy), (ox + 60, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy - 3), (ox, oy + 42), 'fixe', lw=0.8)
P = (ox + 2 * u * math.cos(math.radians(60)), oy + 2 * u * math.sin(math.radians(60)))
line(ax, [(P[0], oy), P], 'fixe', lw=1.2, dash=True)
line(ax, [(ox, oy), (P[0], oy)], 'varie', lw=1.6)
line(ax, [(ox, oy), P], 'sujet', lw=2.0)
disc(ax, P[0], P[1], 1.6, 'sujet')
ax.add_patch(Arc((ox, oy), 18, 18, theta1=0, theta2=60, ec=COL['varie'], lw=1.0, zorder=3))
text(ax, ox + 14.5, oy + 5.5, '60°', 'varie', 's')
text(ax, 18.5, oy + 22, 'r = 2', 'sujet', 'm', ha='center')
text(ax, (ox + P[0]) / 2, oy - 3.7, 'a = 2 cos 60° = 1', 'varie', 's', ha='center')
text(ax, P[0] + 3, oy + 17, 'b = 2 sin 60°\n= √3 ≈ 1,73', 'fixe', 's', ha='left')
text(ax, P[0] + 3, P[1] + 2, 'z = 1 + √3 i', 'sujet', 'm', ha='left', weight='bold')
box(ax, 14, 54, 60, 8, 'sujet', label='z = r (cos θ + i sin θ)', size='m')
save(fig, '39-058')
