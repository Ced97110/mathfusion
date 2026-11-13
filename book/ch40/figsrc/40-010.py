import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin
fig, ax = canvas(52)
s = 40.0; R = 0.35 * s  # 40 mm par mètre : rayon 14 mm
gy = 8.0; x1 = 16.0; d = pi * R  # demi-tour : le centre avance de pi*R = 1,10 m
x2 = x1 + d
line(ax, [(2, gy), (86, gy)], 'fixe', lw=1.2)
for x in (x1, x2):
    ax.add_patch(Circle((x, gy + R), R, ec=COL['sujet'], fc='none', lw=1.0, zorder=2))
    disc(ax, x, gy + R, 0.8, 'fixe')
T = [pi * i / 100 for i in range(101)]
line(ax, [(x1 + R * (t - sin(t)), gy + R * (1 - cos(t))) for t in T], 'varie', lw=1.0, dash=True)
disc(ax, x1, gy, 1.3, 'varie')
disc(ax, x2, gy + 2 * R, 1.3, 'varie')
arrow(ax, (x1 + 1.5, gy + R), (x2 - 1.5, gy + R), 'fixe', lw=0.8)
text(ax, (x1 + x2) / 2, gy + R - 4.5, 'centre :\n+1,10 m', 'fixe', 's')
text(ax, (x1 + x2) / 2, gy - 5, 'pas de point fixe', 'fixe', 's')
line(ax, [(x2 + R + 3, gy), (x2 + R + 3, gy + 2 * R)], 'varie', lw=0.8)
text(ax, x2 + R + 3, gy + R, '0,70 m', 'varie', 's', ha='left', rot=0)
text(ax, x1, gy - 5.5 + 0.5, 'départ', 'varie', 's')
text(ax, x2, gy + 2 * R + 4, 'demi-tour', 'varie', 's')
save(fig, '40-010')
