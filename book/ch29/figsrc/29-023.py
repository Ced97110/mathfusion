import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
def pt(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arcpts(c, r, a0, a1, n=60): return [pt(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
fig, ax = canvas(62)
c = (10, 8); a = 57.2958
for R, role, lab in ((14, 'sujet', 'arc 3 cm'), (28, 'varie', 'arc 6 cm')):
    line(ax, arcpts(c, R, 0, a, 40), role, lw=2.0)
    line(ax, arcpts(c, R + 2.5, -3, a + 3, 30), 'fixe', lw=0.5) if False else None
line(ax, [c, pt(c, 54, 0)], 'fixe', lw=1.0); line(ax, [c, pt(c, 54, a)], 'fixe', lw=1.0)
line(ax, arcpts(c, 7, 0, a, 20), 'autre', lw=1.0)
text(ax, c[0] + 14, c[1] - 3.5, '3 cm', 'sujet', 's'); text(ax, c[0] + 28, c[1] - 3.5, '6 cm', 'varie', 's')
arrow(ax, (c[0] + 15, c[1] + 4.5), (c[0] + 27, c[1] + 4.5), 'varie')
text(ax, 28, 18, '×2', 'varie', 's')
text(ax, 76, 46, 'même angle', 'autre', 'm', ha='right')
p1 = pt(c, 14, a / 2); p2 = pt(c, 28, a / 2)
text(ax, p1[0] + 3, p1[1] + 7, 'arc 3 cm', 'sujet', 's', ha='left') if False else None
text(ax, 72, 24, 'r = 3 cm : arc 3 cm', 'sujet', 's', ha='right') if False else None
text(ax, 86, 28, 'arc 3 cm', 'sujet', 'm', ha='right'); text(ax, 86, 20, 'arc 6 cm', 'varie', 'm', ha='right')
save(fig, '29-023')
