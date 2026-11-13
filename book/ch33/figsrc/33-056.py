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

fig, ax = canvas(68)
c = (44, 33); R = 24
base(ax, c, R)
arc(ax, c, R, 0, 360, 'fixe', 1.0)
p = P(c, R, 60)
line(ax, [(c[0], c[1]), p], 'fixe', 0.9)
line(ax, [p, (p[0], c[1])], 'fixe', 0.8, dash=True)
line(ax, [(c[0], c[1]), (p[0], c[1])], 'varie', 2.6)
dot(ax, p, 'sujet', 1.7)
text(ax, p[0] + 5, p[1] + 3, r'$P$', 'sujet')
text(ax, (c[0] + p[0]) / 2, c[1] - 4, r'$x$ = 0,5', 'varie')
text(ax, c[0] - R, c[1] - 4, '−1', 'fixe'); text(ax, c[0] + R + 1, c[1] - 4, '1', 'fixe')
text(ax, 44, 65, r'$x$ : un cosinus (abscisse de $P$)', 'varie', 's')
save(fig, '33-056')
