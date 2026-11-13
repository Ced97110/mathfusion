import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

import math
def P(c, R, d): return (c[0] + R * math.cos(math.radians(d)), c[1] + R * math.sin(math.radians(d)))
def arc(ax, c, R, a, b, role, lw=1.8, dash=False): line(ax, [P(c, R, a + (b - a) * i / 80) for i in range(81)], role, lw, dash)
def base(ax, c, R):
    disc(ax, c[0], c[1], R, "fixe", fill=False, lw=0.5)
    line(ax, [(c[0] - R - 3, c[1]), (c[0] + R + 3, c[1])], "fixe", 0.5)
    line(ax, [(c[0], c[1] - R - 3), (c[0], c[1] + R + 3)], "fixe", 0.5)
def dot(ax, p, role, r=1.4, filled=True):
    ax.add_patch(Circle(p, r, ec=COL[role], fc=FILL[role] if filled else "white", lw=1.0, zorder=4))

fig, ax = canvas(66)
c = (44, 33); R = 22
base(ax, c, R)
arc(ax, c, R, 0, 360, 'fixe', 1.0)
d = 45
line(ax, [P(c, R + 4, d + 180), P(c, R + 4, d)], 'varie', 1.2)
dot(ax, P(c, R, d), 'resultat', 1.8); dot(ax, P(c, R, d + 180), 'fixe', 1.8, filled=False)
text(ax, *P(c, R + 8, d), '45°', 'resultat'); text(ax, *P(c, R + 8, d + 180), '225°', 'fixe')
text(ax, c[0] + 3, c[1] - 3, r'$O$', 'fixe')
text(ax, 72, 12, 'on garde', 'resultat', 's'); text(ax, 16, 56, 'on écarte', 'fixe', 's')
text(ax, 44, 62, 'pente 1 : une seule droite', 'varie', 's')
save(fig, '33-059')
