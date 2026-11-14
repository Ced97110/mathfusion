import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
def pt(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arcpts(c, r, a0, a1, n=60): return [pt(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
fig, ax = canvas(62)
c = (44, 31); R = 22
line(ax, arcpts(c, R, 130, 390, 120), 'fixe', lw=0.9)
line(ax, arcpts(c, R, 30, 130, 60), 'sujet', lw=2.2)
P = pt(c, R, 30); Q = pt(c, R, 130)
for p in (P, Q): disc(ax, p[0], p[1], 1.1, 'sujet')
text(ax, P[0] + 4, P[1] + 1, 'B', 'sujet', 'l'); text(ax, Q[0] - 4, Q[1] + 1, 'A', 'sujet', 'l')
text(ax, 44, 59, 'arc AB', 'sujet', 'l')
arrow(ax, (44, 56.5), (44, c[1] + R * math.sin(math.radians(80)) + 1.5), 'sujet')
text(ax, 44, 27, 'le reste du cercle', 'fixe', 'm')
save(fig, '29-017')
