import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
def pt(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arcpts(c, r, a0, a1, n=60): return [pt(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
fig, ax = canvas(50)
a = 57.2958
for x0, R, lab in ((4, 12, 'r = 3 cm'), (24, 20, 'r = 6 cm'), (54, 28, 'r = 100 cm')):
    c = (x0, 12)
    ax.add_patch(Wedge(c, R, 0, a, fc=FILL['sujet'], ec=COL['sujet'], lw=0.9, zorder=2))
    line(ax, arcpts(c, R, 0, a, 40), 'varie', lw=2.0)
    line(ax, arcpts(c, 4.5, 0, a, 20), 'autre', lw=1.0)
    text(ax, c[0] + R / 2, 7, lab, 'sujet', 's')
text(ax, 30, 45, 'même angle : arc = r', 'autre', 'm')
save(fig, '29-024')
