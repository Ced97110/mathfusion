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

fig, ax = canvas(80)
text(ax, 44, 72, 'se lit « arccosinus de x »', 'sujet', 'l')
box(ax, 2, 50, 27, 10, 'varie', label='x : un cosinus', size='s')
box(ax, 37, 50, 16, 10, 'sujet', label='arccos', size='m', weight='bold')
box(ax, 61, 50, 25, 10, 'sujet', label='un angle', size='m')
arrow(ax, (30, 55), (36, 55), 'varie'); arrow(ax, (54, 55), (60, 55), 'sujet')
for i, s in enumerate(['arccos 0,5 = 60°', 'arccos (−0,5) = 120°', 'arccos 1 = 0°']):
    box(ax, 18, 33 - i * 12, 52, 9, 'resultat', label=s)
save(fig, '33-054')
