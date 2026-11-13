import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
def pt(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arcpts(c, r, a0, a1, n=60): return [pt(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
fig, ax = canvas(62)
c = (14, 8); R = 46; a0, a1 = 8, 62
ax.add_patch(Wedge(c, R, a0, a1, fc=FILL['sujet'], ec='none', zorder=1))
line(ax, [c, pt(c, R, a0)], 'sujet', lw=1.3); line(ax, [c, pt(c, R, a1)], 'sujet', lw=1.3)
line(ax, arcpts(c, R, a0, a1, 50), 'varie', lw=2.4)
line(ax, arcpts(c, 12, a0, a1, 30), 'autre', lw=1.5)
text(ax, 8, 6, 'O', 'sujet', 'm')
P = pt(c, R, a0); Q = pt(c, R, a1)
text(ax, P[0] + 4, P[1] - 1, 'P', 'sujet', 'm'); text(ax, Q[0] + 2, Q[1] + 3, 'Q', 'sujet', 'm')
t = pt(c, 19, (a0 + a1) / 2); text(ax, t[0] + 1, t[1], 'θ', 'autre', 'l')
aa = pt(c, 28, 36); text(ax, aa[0], aa[1] + 2, 'A', 'sujet', 'xl'); text(ax, aa[0], aa[1] - 4, 'aire', 'sujet', 's')
s = pt(c, R + 3, (a0 + a1) / 2); text(ax, s[0] + 3, s[1], 's', 'varie', 'l')
m = pt(c, 24, 4); text(ax, m[0], m[1] - 3, 'r', 'sujet', 'm')
save(fig, '29-026')
