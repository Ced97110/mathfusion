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

fig, ax = canvas(72)
c = (44, 39); R = 22
base(ax, c, R)
arc(ax, c, R, -90, 90, 'fixe', 1.0)
arc(ax, c, R, 90, 270, 'autre', 2.4)
y = c[1] + 0.5 * R
line(ax, [(c[0] - R - 2, y), (c[0] + R + 2, y)], 'varie', 0.9, dash=True)
dot(ax, P(c, R, 150), 'limite', 1.7); dot(ax, P(c, R, 30), 'fixe')
text(ax, 44 - 22 + 1, y + 9, '150°', 'limite', 'l')
text(ax, 76, y + 4, 'hauteur 0,5', 'varie', 's')
text(ax, c[0] + R - 4, y - 4, '30°', 'fixe')
text(ax, c[0], c[1] + R + 5, '90°', 'autre'); text(ax, c[0], c[1] - R - 5, '270°', 'autre')
text(ax, 44, 3.5, 'moitié gauche : 150° n’est pas aigu', 'limite', 's')
save(fig, '33-050')
