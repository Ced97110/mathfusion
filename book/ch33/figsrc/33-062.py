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

fig, ax = canvas(76)
c = (36, 38); R = 22
base(ax, c, R)
arc(ax, c, R, -90, 90, 'fixe', 1.0)
for t, lab, dx, dy in ((0.08, '0,08', 0, -3), (1.0, '1', 0, 2), (1000.0, '1 000', -3, 4)):
    d = math.degrees(math.atan(t))
    line(ax, [c, P(c, R + 3, d)], 'varie', 1.4)
    dot(ax, P(c, R, d), 'sujet')
    p = P(c, R + 3, d)
    text(ax, p[0] + dx + 2, p[1] + dy, lab, 'varie', 's', ha='left')
text(ax, 44, 72, r'$x$ : la pente d’une droite', 'varie', 's')
text(ax, 44, 5, 'hauteur ÷ abscisse', 'varie', 's')
save(fig, '33-062')
