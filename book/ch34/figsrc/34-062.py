import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(72)
cx, cy, r = 28, 36, 26
disc(ax, cx, cy, r, 'fixe', fill=False)
line(ax, [(cx - r - 2, cy), (cx + r + 3, cy)], 'fixe', lw=0.7)
c, s = r * math.cos(math.radians(30)), r * math.sin(math.radians(30))
P1 = (cx + c, cy + s); P2 = (cx + c, cy - s)
line(ax, [(cx, cy), P1], 'sujet', lw=1.2); line(ax, [(cx, cy), P2], 'autre', lw=1.2)
line(ax, [P1, P2], 'fixe', dash=True)
line(ax, [(cx, cy - 2.5), (cx + c, cy - 2.5)], 'resultat', lw=0)
ax.plot([cx, cx + c], [cy, cy], color=COL['resultat'], lw=2.4, zorder=4, solid_capstyle='round')
for P, role in ((P1, 'sujet'), (P2, 'autre')): ax.plot([P[0]], [P[1]], 'o', color=COL[role], ms=3.5, zorder=6)
text(ax, P1[0] + 3, P1[1] + 2, 'B = 30°', 'sujet', 's', ha='left'); text(ax, P2[0] + 3, P2[1] - 2, '−B = −30°', 'autre', 's', ha='left')
text(ax, cx + c / 2, cy + 3, '0,866', 'resultat', 's')
text(ax, cx + c + 12, cy + s / 2 - 1, 'hauteur 0,5', 'sujet', 's')
text(ax, cx + c + 12, cy - s / 2 + 1, 'hauteur −0,5', 'autre', 's')
save(fig, '34-062')
