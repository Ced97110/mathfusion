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

fig, ax = canvas(48)
text(ax, 44, 40, r'$]-\pi/2,\ \pi/2[$', 'sujet', 'xl', weight='bold')
f = numberline(ax, 12, 76, 20, -90, 90, 45, arrow_right=False)
line(ax, [(f(-90) + 2, 20), (f(90) - 2, 20)], 'sujet', 3.0)
for v in (-90, 90): dot(ax, (f(v), 20), 'limite', 1.8, filled=False)
text(ax, f(0), 28, 'dedans', 'sujet', 's')
text(ax, f(-90) + 3, 28, 'dehors', 'limite', 's'); text(ax, f(90) - 3, 28, 'dehors', 'limite', 's')
text(ax, 44, 5, 'bouts exclus', 'limite', 's')
save(fig, '33-064')
