import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
def pt(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arcpts(c, r, a0, a1, n=60): return [pt(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
fig, ax = canvas(60)
c = (12, 8); R = 40
line(ax, arcpts(c, R, -2, 66, 60), 'fixe', lw=0.8)
line(ax, [c, pt(c, R, 0)], 'fixe', lw=1.0)
line(ax, [c, pt(c, R, 60)], 'fixe', lw=1.0, dash=True)
line(ax, [c, pt(c, R, 57.2958)], 'sujet', lw=1.3)
line(ax, arcpts(c, R, 0, 57.2958, 50), 'resultat', lw=2.2)
line(ax, arcpts(c, R, 57.2958, 60, 6), 'varie', lw=2.2)
line(ax, arcpts(c, 14, 0, 60, 30), 'fixe', lw=0.8)
text(ax, 26, 21, '60°', 'fixe', 's')
text(ax, 80, 50, '1 radian', 'sujet', 'm', ha='right')
arrow(ax, (62, 48), pt(c, 28, 50), 'sujet', curve=0.2)
text(ax, 86, 20, 'arc = r', 'resultat', 'm', ha='right')
text(ax, 86, 12, 'arc 60° ≈ 1,047 r', 'varie', 'm', ha='right')
text(ax, 80, 40, '60°', 'fixe', 's') if False else None
save(fig, '29-022')
