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
c = (44, 16); R = 24
line(ax, [(c[0] - R - 4, c[1]), (c[0] + R + 4, c[1])], 'fixe', 0.5)
arc(ax, c, R, 0, 180, 'sujet', 2.4)
dot(ax, P(c, R, 0), 'sujet', 1.7); dot(ax, P(c, R, 180), 'sujet', 1.7)
text(ax, c[0] + R, c[1] - 5, r'$\pi$ (180°)', 'sujet'); text(ax, c[0] - R, c[1] - 5, '0 (0°)', 'sujet')
text(ax, 44, 52, r'$[0,\pi]$', 'sujet', 'xl', weight='bold')
text(ax, 44, 4, 'bouts compris', 'sujet', 's')
text(ax, 44, 26, 'les angles de 0° à 180°', 'fixe', 's')
save(fig, '33-055')
