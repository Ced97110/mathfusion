import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(62)
cx, cy, u = 24, 32, 3.8
arrow(ax, (cx - 22, cy), (cx + 22, cy), 'fixe', lw=0.7)
arrow(ax, (cx, cy - 25), (cx, cy + 25), 'fixe', lw=0.7)
disc(ax, cx, cy, 5 * u, 'autre', fill=False, lw=1.3)
for i in range(24):
    t = 2 * math.pi * i / 24
    disc(ax, cx + 5 * u * math.cos(t), cy + 5 * u * math.sin(t), 0.8, 'autre')
disc(ax, cx, cy, 1.6, 'sujet')
text(ax, 64, cy + 12, r'$O$ : 1 seul point', 'sujet', 'm')
arrow(ax, (50, cy + 9), (cx + 2.2, cy + 1), 'sujet', curve=0.15)
text(ax, 64, cy - 12, 'cercle : une infinité', 'autre', 's')
text(ax, 64, cy - 15.5, 'de points', 'autre', 's')
arrow(ax, (50, cy - 9), (cx + 5 * u * math.cos(-0.5) + 1, cy + 5 * u * math.sin(-0.5) - 0.3), 'autre', curve=-0.15)
text(ax, cx, 3.5, r'$x^2 + y^2 = 0$ : seul $O$', 'sujet', 's')
save(fig, '43-130')
