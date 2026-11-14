import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
def pt(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arcpts(c, r, a0, a1, n=60): return [pt(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
fig, ax = canvas(56)
c = (12, 8); R = 40; a0, a1 = 10, 65
ax.add_patch(Wedge(c, R, a0, a1, fc=FILL['resultat'], ec=COL['sujet'], lw=1.3, zorder=2))
t = pt(c, 22, 38); text(ax, t[0], t[1], 'A', 'resultat', 'xl')
m = pt(c, 22, 2); text(ax, 30, 5, 'r', 'sujet', 'm')
line(ax, arcpts(c, 11, a0, a1, 30), 'autre', lw=1.3)
q = pt(c, 16, 37); text(ax, 80, 46, 'A : aire du secteur', 'resultat', 'm', ha='right')
text(ax, 80, 36, 'dépend de r et de θ', 'fixe', 's', ha='right')
text(ax, 80, 28, 'en cm²', 'resultat', 's', ha='right')
save(fig, '29-030')
