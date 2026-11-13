import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

cx, cy, s = 44, 42, 13  # origine, mm par unité
fig, ax = canvas(84)
arrow(ax, (4, cy), (84, cy), 'fixe', lw=0.7)
arrow(ax, (cx, 6), (cx, 72), 'fixe', lw=0.7)
disc(ax, cx, cy, 2 * s, 'fixe', fill=False, lw=0.8)
pts = [(2.0, 0.0), (-1.0, math.sqrt(3)), (-1.0, -math.sqrt(3))]
for (x, y) in pts:
    line(ax, [(cx, cy), (cx + x * s, cy + y * s)], 'sujet', lw=0.8, dash=True)
    disc(ax, cx + x * s, cy + y * s, 1.3, 'sujet', lw=0.8)
ax.add_patch(Arc((cx, cy), 12, 12, theta1=0, theta2=120, ec=COL['varie'], lw=1.1, zorder=3))
ax.add_patch(Arc((cx, cy), 30, 30, theta1=0, theta2=240, ec=COL['varie'], lw=1.1, zorder=3))
text(ax, cx + 2 * s + 2.5, cy + 3.2, r'$z_0=2$', 'sujet', 's', ha='left')
text(ax, cx - s - 2.5, cy + math.sqrt(3) * s + 2.5, r'$z_1=-1+\sqrt{3}\,i$', 'sujet', 's', ha='right')
text(ax, cx - s - 2.5, cy - math.sqrt(3) * s - 2.5, r'$z_2=-1-\sqrt{3}\,i$', 'sujet', 's', ha='right')
text(ax, cx + 9.5, cy + 6, '120°', 'varie', 's')
text(ax, cx + 6.5, cy - 18, '240°', 'varie', 's')
text(ax, cx + s * 1.4, cy - 2.2 * s + 1, 'module 2', 'fixe', 's')
text(ax, 4, 79, r'$z^3=8$', 'encre', 'l', ha='left')
save(fig, '39-097')
