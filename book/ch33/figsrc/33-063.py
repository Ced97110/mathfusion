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
c = (30, 35); R = 22
base(ax, c, R)
arc(ax, c, R, -90, 90, 'sujet', 2.4)
for d, role in ((45, 'resultat'), (-45, 'resultat')):
    line(ax, [c, P(c, R, d)], 'varie', 1.2); dot(ax, P(c, R, d), role)
text(ax, *P(c, R + 7, 45), '45°', 'resultat'); text(ax, *P(c, R + 7, -45), '−45°', 'resultat')
text(ax, 62, 64, 'arctan', 'sujet', 'xl', weight='bold'); text(ax, 80, 64, r'$x$', 'varie', 'xl', weight='bold')
text(ax, 62, 56, 'l’angle', 'sujet', 's'); text(ax, 80, 56, 'une pente', 'varie', 's', ha='center')
box(ax, 58, 42, 28, 8, 'resultat', label='arctan 1 = 45°', size='s')
box(ax, 58, 30, 28, 8, 'resultat', label='arctan (−1) = −45°', size='s')
save(fig, '33-063')
