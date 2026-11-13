import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc, Rectangle
import math
fig, ax = canvas(70)
O = (44, 36)
k = 0.3
good = 180 - math.degrees(math.atan2(99.586, 6.428))   # 93,7°
bad = math.degrees(math.atan(99.586 / -6.428))          # -86,31°
ax.add_patch(Rectangle((6, O[1]), O[0] - 6, 30, fc=FILL['fixe'], ec='none', zorder=0))
arrow(ax, (6, O[1]), (82, O[1]), 'fixe', lw=0.9)
line(ax, [(O[0], 6), (O[0], 66)], 'fixe')
P = lambda r, a: (O[0] + r * math.cos(math.radians(a)), O[1] + r * math.sin(math.radians(a)))
arrow(ax, O, P(99.79 * k, 180 - math.degrees(math.atan2(99.586, 6.428)) if False else (180 - 86.31)), 'resultat', lw=1.8)
tipb = P(99.79 * k, bad)
ax.plot([O[0], tipb[0]], [O[1], tipb[1]], color=COL['limite'], lw=1.5, ls='--', zorder=3)
arrow(ax, (O[0] + 0.5 * (tipb[0] - O[0]), O[1] + 0.5 * (tipb[1] - O[1])), tipb, 'limite', lw=1.5)
ax.add_patch(Arc(O, 20, 20, theta1=0, theta2=93.7, color=COL['resultat'], lw=1.1, zorder=3))
ax.add_patch(Arc(O, 14, 14, theta1=bad, theta2=0, color=COL['limite'], lw=1.1, zorder=3))
text(ax, 22, 62, '2e quadrant', 'fixe', 's')
text(ax, 22, 47, r'$\langle -6{,}428\,;\,99{,}586\rangle$', 'resultat', 's')
text(ax, 66, 58, 'juste : 93,7°', 'resultat', 's')
text(ax, 66, 12, 'arctan : −86,31°', 'limite', 's')
box(ax, 4, 17, 34, 8, 'varie', label='−86,31° + 180° = 93,7°', size='s')
save(fig, '41-134')
