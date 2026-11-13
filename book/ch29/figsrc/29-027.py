import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
def pt(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arcpts(c, r, a0, a1, n=60): return [pt(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
fig, ax = canvas(52)
for cx, a in ((6, 35), (50, 80)):
    c = (cx, 12); R = 30
    line(ax, [c, pt(c, R, 0)], 'sujet', lw=1.3); line(ax, [c, pt(c, R, a)], 'sujet', lw=1.3)
    line(ax, arcpts(c, 9, 0, a, 30), 'autre', lw=1.6)
    t = pt(c, 15, a / 2); text(ax, t[0] + 1, t[1], 'θ', 'autre', 'xl')
    text(ax, cx - 2.5, 9, 'O', 'sujet', 'm')
text(ax, 44, 3.5, 'θ : « thêta », un angle', 'autre', 'm')
text(ax, 44, 47, 'même lettre, angles différents', 'fixe', 's')
save(fig, '29-027')
