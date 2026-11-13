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

fig, ax = canvas(60)
c = (44, 18); R = 22
base(ax, c, R)
arc(ax, c, R, 0, 180, 'sujet', 2.4)
x = c[0] + 0.5 * R
line(ax, [(x, c[1] - 3), (x, c[1] + R + 3)], 'varie', 0.9, dash=True)
dot(ax, P(c, R, 60), 'resultat', 1.7)
text(ax, c[0] + R + 6, c[1] + 3, '0°', 'sujet'); text(ax, c[0] - R - 6, c[1] + 3, '180°', 'sujet')
text(ax, c[0] - R, c[1] - 4, '−1', 'fixe'); text(ax, c[0] + R, c[1] - 4, '1', 'fixe')
text(ax, x + 0.5, c[1] - 4, '0,5', 'varie')
text(ax, x + 9, c[1] + R * 0.87 + 4, '60°', 'resultat')
text(ax, c[0], 47, 'moitié haute : un seul point', 'sujet')
save(fig, '33-051')
