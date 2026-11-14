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

fig, ax = canvas(64)
c = (44, 10); R = 26
line(ax, [(c[0] - R - 4, c[1]), (c[0] + R + 4, c[1])], 'fixe', 0.5)
arc(ax, c, R, 0, 180, 'fixe', 1.0)
arc(ax, c, 7, 0, 120, 'varie', 1.6)
p = P(c, R, 120)
line(ax, [c, p], 'sujet', 1.0)
line(ax, [p, (p[0], c[1])], 'fixe', 0.8, dash=True)
dot(ax, (p[0], c[1]), 'varie', 1.2); dot(ax, p, 'resultat', 1.7)
text(ax, p[0] - 4, p[1] + 3, r'$P$', 'resultat')
text(ax, p[0], c[1] - 4, '−0,5', 'varie')
text(ax, c[0] + 12, c[1] + 8, '120°', 'varie')
text(ax, 44, 55, r'arccos(−0,5) = $2\pi/3$', 'resultat', 'l')
text(ax, 66, 30, r'120° = $2\pi/3$', 'resultat', 's')
save(fig, '33-057')
