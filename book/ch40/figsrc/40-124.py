import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import numpy as np
fig, ax = canvas(68)
cx, cy, R = 29, 36, 26
arrow(ax, (cx - R - 3, cy), (cx + R + 4, cy), 'fixe', lw=0.6)
disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.5)
tips = [(cx + R * math.cos(math.radians(72 * k)), cy + R * math.sin(math.radians(72 * k))) for k in range(5)]
poly(ax, tips, 'autre', fill=False, lw=1.0)
th = np.linspace(0, 2 * math.pi, 900)
line(ax, [(cx + R * math.cos(5 * t) * math.cos(t), cy + R * math.cos(5 * t) * math.sin(t)) for t in th], 'sujet', lw=1.4)
for p in tips:
    disc(ax, p[0], p[1], 1.0, 'autre')
t1 = tips[1]
line(ax, [t1, (t1[0], cy)], 'varie', lw=0.8, dash=True)
disc(ax, t1[0], cy, 1.1, 'varie')
ax.add_patch(Arc((cx, cy), 18, 18, theta1=0, theta2=72, color=COL['varie'], lw=1.0, zorder=3))
text(ax, cx + 12, cy + 4.5, '72°', 'varie', 's')
text(ax, cx + 8, cy - 5, '0,309', 'varie', 's')
text(ax, 74, 60, r'$r=\cos 5\theta$', 'sujet', 'm')
text(ax, 74, 53, '5 pointes\naux 72°, 144°…', 'sujet', 's')
text(ax, 74, 42, 'pentagone\nrégulier', 'autre', 's')
text(ax, 74, 30, r'$\cos 72^\circ\approx 0{,}309$', 'varie', 's')
text(ax, 74, 24, 'à construire\nà la règle, au compas', 'encre', 's')
save(fig, '40-124')
