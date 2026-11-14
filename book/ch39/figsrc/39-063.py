import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# Judson : 2 cis 60° devient 1 + √3 i
fig, ax = canvas(58)
steps = [(46, 'sujet', 'z = 2 cis 60°'), (34, 'varie', 'a = 2 cos 60° = 1'),
         (22, 'varie', 'b = 2 sin 60° = √3'), (8, 'resultat', 'z = 1 + √3 i')]
for y, role, s in steps:
    box(ax, 2, y, 42, 9, role, label=s, size='s')
for y0, y1 in ((46, 43), (34, 31), (22, 17)):
    arrow(ax, (23, y0), (23, y1), 'fixe', lw=0.9)
ox, oy, u = 54, 8, 14
arrow(ax, (ox - 3, oy), (ox + 31, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy - 2), (ox, oy + 46), 'fixe', lw=0.8)
P = (ox + 2 * u * 0.5, oy + 2 * u * math.sin(math.radians(60)))
line(ax, [(P[0], oy), P], 'fixe', lw=0.8, dash=True)
line(ax, [(ox, oy), (P[0], oy)], 'varie', lw=1.5)
line(ax, [(ox, oy), P], 'sujet', lw=1.8)
disc(ax, P[0], P[1], 1.5, 'sujet')
ax.add_patch(Arc((ox, oy), 14, 14, theta1=0, theta2=60, ec=COL['varie'], lw=0.9, zorder=3))
text(ax, ox + 9.5, oy + 3, '60°', 'varie', 's')
text(ax, ox + 4.5, oy + 20, '2', 'sujet', 'm', ha='right')
text(ax, P[0] + 2.5, P[1] + 2, 'P', 'sujet', 'm', ha='left', weight='bold')
save(fig, '39-063')
