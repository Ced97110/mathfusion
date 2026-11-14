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

fig, ax = canvas(70)
c = (44, 35); R = 22
base(ax, c, R)
arc(ax, c, R, -90, 90, 'sujet', 2.4)
line(ax, [(c[0], c[1] - R - 3), (c[0], c[1] + R + 3)], 'limite', 0.9, dash=True)
dot(ax, P(c, R, 90), 'limite', 1.8, filled=False); dot(ax, P(c, R, -90), 'limite', 1.8, filled=False)
text(ax, c[0] - 12, c[1] + R + 3, '90°', 'limite'); text(ax, c[0] - 12, c[1] - R - 3, '−90°', 'limite')
text(ax, c[0] - 14, c[1] + 5, 'abscisse 0', 'limite', 's')
text(ax, 70, c[1] + R, '1 ÷ 0 : aucun', 'limite', 's'); text(ax, 70, c[1] + R - 4, 'résultat', 'limite', 's')
text(ax, 44, 66, 'droite verticale : pas de pente', 'limite', 's')
save(fig, '33-060')
