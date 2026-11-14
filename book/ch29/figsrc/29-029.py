import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
def pt(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arcpts(c, r, a0, a1, n=60): return [pt(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
fig, ax = canvas(66)
c = (44, 29); R = 26; a0, a1 = 20, 95
disc(ax, c[0], c[1], R, 'fixe')
ax.add_patch(Wedge(c, R, a0, a1, fc=FILL['sujet'], ec=COL['sujet'], lw=1.4, zorder=2.5))
line(ax, arcpts(c, R, a0, a1, 50), 'varie', lw=2.4)
P = pt(c, R, a0); Q = pt(c, R, a1)
text(ax, P[0] + 5, P[1] + 1, 'Q', 'sujet', 'm'); text(ax, Q[0] - 3, Q[1] + 3, 'P', 'sujet', 'm')
t = pt(c, 15, 57); text(ax, t[0], t[1], 'secteur', 'sujet', 'm')
text(ax, 20, 52, 'arc PQ', 'varie', 's', ha='right') if False else None
text(ax, 64, 59, 'arc PQ', 'varie', 'm', ha='left')
text(ax, 40, 18, 'reste du disque', 'fixe', 's')
save(fig, '29-029')
