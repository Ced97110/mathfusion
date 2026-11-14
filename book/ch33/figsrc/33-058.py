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
a = math.radians(30); Lb = 44
A = (22, 46); B = (22 + Lb, 46); C = (22 + Lb / 2, 46 + Lb / 2 * math.tan(a))
poly(ax, [A, B, C], 'sujet')
text(ax, A[0] + 7, A[1] + 2, '30°', 'sujet'); text(ax, B[0] - 7, B[1] + 2, '30°', 'sujet'); text(ax, C[0], C[1] - 4, '120°', 'sujet')
f = numberline(ax, 10, 70, 22, 0, 210, 30, every=2, arrow_right=False, role='fixe')
line(ax, [(f(0), 22), (f(180), 22)], 'sujet', 3.0)
for v in (30, 90, 120): dot(ax, (f(v), 27), 'resultat')
dot(ax, (f(200), 27), 'limite')
text(ax, f(90), 10, 'arccos : 0° à 180°', 'sujet', 'm')
text(ax, 28, 34, 'angles possibles', 'resultat', 's')
text(ax, 63, 34, '200° : impossible', 'limite', 's')
save(fig, '33-058')
