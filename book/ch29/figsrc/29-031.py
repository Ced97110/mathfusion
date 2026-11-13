import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
def pt(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arcpts(c, r, a0, a1, n=60): return [pt(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
fig, ax = canvas(64)
c = (14, 24); R = 34; a = 57.2958
line(ax, [c, pt(c, R, 0)], 'sujet', lw=1.3); line(ax, [c, pt(c, R, a)], 'sujet', lw=1.3)
line(ax, arcpts(c, R, -3, a + 8, 50), 'fixe', lw=0.7)
line(ax, arcpts(c, R, 0, a, 50), 'varie', lw=2.4)
line(ax, arcpts(c, 10, 0, a, 30), 'autre', lw=1.4)
text(ax, 36, 31, '1 radian', 'autre', 's') if False else None
text(ax, c[0] + 17, c[1] - 3.5, 'rayon r', 'sujet', 'm')
text(ax, 14, 18.5, 'O', 'sujet', 'm')
pp = pt(c, R + 3, a / 2); text(ax, pp[0] + 2, pp[1], 'arc', 'varie', 'm', ha='left')
text(ax, 60, 58, '1 radian', 'autre', 'l')
arrow(ax, (50, 55), pt(c, 12, 38), 'autre', curve=0.25)
y = 6
line(ax, [(c[0], y), (c[0] + R, y)], 'sujet', lw=2.4); line(ax, [(c[0], y + 6), (c[0] + R, y + 6)], 'varie', lw=2.4)
for x in (c[0], c[0] + R):
    line(ax, [(x, y - 1), (x, y + 7)], 'fixe', lw=0.6, dash=True)
text(ax, c[0] + R + 2, y, 'r', 'sujet', 'm', ha='left'); text(ax, c[0] + R + 2, y + 6, 'arc', 'varie', 'm', ha='left')
save(fig, '29-031')
