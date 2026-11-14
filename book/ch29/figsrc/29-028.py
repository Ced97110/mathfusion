import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
def pt(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arcpts(c, r, a0, a1, n=60): return [pt(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
fig, ax = canvas(62)
c = (44, 6); R = 36; a0, a1 = 55, 125
line(ax, arcpts(c, R, a0, a1, 50), 'varie', lw=2.4)
P = pt(c, R, a0); Q = pt(c, R, a1)
for p in (P, Q): disc(ax, p[0], p[1], 1.1, 'sujet')
text(ax, P[0] + 4, P[1] + 1, 'Q', 'sujet', 'l'); text(ax, Q[0] - 4, Q[1] + 1, 'P', 'sujet', 'l')
text(ax, 44, 48, 'arc PQ', 'varie', 'm')
L = R * math.radians(a1 - a0)
x0 = 44 - L / 2; y = 22
line(ax, [(x0, y), (x0 + L, y)], 'varie', lw=2.4)
for x in (x0, x0 + L): line(ax, [(x, y - 1.8), (x, y + 1.8)], 'varie', lw=1.2)
text(ax, 44, y - 5, 's', 'varie', 'xl')
text(ax, 44, 12.5, 'longueur de l’arc, en cm', 'encre', 's') if False else None
save(fig, '29-028')
