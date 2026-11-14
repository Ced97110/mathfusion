import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(52)
for cx, deg, lab, note, role in [(16, 0, r'$\theta = 0°$', 'identité', 'resultat'), (44, 90, r'$\theta = 90°$', 'quart de tour', 'sujet'), (72, 360, r'$\theta = 360°$', 'identité', 'resultat')]:
    cy, r = 26, 10
    disc(ax, cx, cy, r, 'fixe')
    line(ax, [(cx, cy), (cx + r, cy)], 'fixe', 0.8, dash=True)
    a = math.radians(deg if deg < 360 else 0)
    arrow(ax, (cx, cy), (cx + r * math.cos(a), cy + r * math.sin(a)), 'varie', 1.3)
    if deg:
        ts = [math.radians(t) for t in range(0, deg + 1, 5)]
        ax.plot([cx + (r + 2) * math.cos(t) for t in ts], [cy + (r + 2) * math.sin(t) for t in ts], color=COL['varie'], lw=0.9, zorder=3)
    text(ax, cx, 8, lab, 'varie', 's'); text(ax, cx, 47, note, role, 's')
text(ax, 44, 2.5, 'même rotation : 0° et 360°', 'resultat', 's')
save(fig, '73-133')
