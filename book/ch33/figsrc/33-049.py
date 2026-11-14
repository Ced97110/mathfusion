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
c = (12, 12); R = 46
line(ax, [(c[0], c[1]), (c[0] + R + 3, c[1])], 'fixe', 0.6); line(ax, [(c[0], c[1]), (c[0], c[1] + R + 3)], 'fixe', 0.6)
arc(ax, c, R, 0, 90, 'resultat', 2.4)
A = c; Pt = P(c, R, 30); F = (Pt[0], c[1])
poly(ax, [A, F, Pt], 'sujet')
line(ax, [(F[0] - 2.5, F[1]), (F[0] - 2.5, F[1] + 2.5), (F[0], F[1] + 2.5)], 'sujet')
arc(ax, c, 11, 0, 30, 'sujet', 1.0)
text(ax, c[0] + 19, c[1] + 2.6, '30°', 'sujet', 's'); text(ax, Pt[0] - 3.4, Pt[1] - 5.5, '60°', 'sujet', 's')
text(ax, F[0] - 6, F[1] + 5.5, '90°', 'sujet', 's')
line(ax, [c, P(c, R, 60)], 'fixe', 0.8, True); dot(ax, P(c, R, 60), 'sujet'); dot(ax, Pt, 'sujet')
text(ax, *P(c, R + 5, 60), '60°', 'sujet', 's')
text(ax, c[0] + R + 6, c[1] + 0.5, '0°', 'resultat', 's'); text(ax, c[0], c[1] + R + 5, '90°', 'resultat', 's')
text(ax, 66, 50, '30° + 60° = 90°', 'sujet', 's')
text(ax, 44, 72, 'entre 0° et 90°', 'resultat', 'l')
save(fig, '33-049')
