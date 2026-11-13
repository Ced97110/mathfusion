import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig, ax = canvas(48)
k = 0.5
O = (56, 10)
tip = (O[0] + 70 * k * math.cos(math.radians(130)), O[1] + 70 * k * math.sin(math.radians(130)))
comp = (O[0] - 44.995 * k, O[1])
arrow(ax, (4, 10), (84, 10), 'fixe', lw=0.9)
line(ax, [tip, comp], 'fixe', dash=True)
arrow(ax, O, tip, 'autre', lw=1.4)
arrow(ax, (O[0], 6.5), (comp[0], 6.5), 'varie', lw=1.8)
ax.add_patch(Arc(O, 14, 14, theta1=0, theta2=130, color=COL['varie'], lw=1.1, zorder=3))
text(ax, 62, 17, '130°', 'varie', 's')
text(ax, tip[0] - 9, tip[1] + 1, '70 N', 'autre', 'm')
text(ax, (O[0] + comp[0]) / 2, 2.5, r'$-44{,}995$ : vers l’ouest', 'varie', 's')
text(ax, 74, 40, r'$\cos 130^\circ\approx-0{,}6428$', 'autre', 'm')
text(ax, 10, 13.5, 'ouest', 'fixe', 's')
text(ax, 80, 13.5, 'est', 'fixe', 's')
save(fig, '41-133')
