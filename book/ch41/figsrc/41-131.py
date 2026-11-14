import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig, ax = canvas(60)
k = 0.4
O = (44, 8)
def pol(n, ang):
    return (O[0] + n * k * math.cos(math.radians(ang)), O[1] + n * k * math.sin(math.radians(ang)))
F1 = pol(60, 50)
F2 = pol(70, 130)
S = (O[0] + (-6.428) * k, O[1] + 99.586 * k)
line(ax, [O, (O[0], O[1] + 44)], 'fixe', dash=True)
line(ax, [F1, S], 'fixe', dash=True)
line(ax, [F2, S], 'fixe', dash=True)
arrow(ax, O, F1, 'sujet', lw=1.3)
arrow(ax, O, F2, 'autre', lw=1.3)
arrow(ax, O, S, 'resultat', lw=1.6)
ax.add_patch(Arc(O, 20, 20, theta1=50, theta2=90, color=COL['fixe'], lw=0.9, zorder=3))
ax.add_patch(Arc(O, 20, 20, theta1=90, theta2=130, color=COL['fixe'], lw=0.9, zorder=3))
text(ax, 49.5, 21, '40°', 'fixe', 's')
text(ax, 38.5, 21, '40°', 'fixe', 's')
text(ax, 70, 26, r'$F_1$ = 60 N', 'sujet', 'm')
text(ax, 17, 30, r'$F_2$ = 70 N', 'autre', 'm')
text(ax, 44, 54.5, 'somme ≈ 99,79 N', 'resultat', 'm')
text(ax, 68, 45, '≠ 60 + 70 = 130', 'limite', 's')
text(ax, 44, 3, 'nord', 'fixe', 's')
save(fig, '41-131')
