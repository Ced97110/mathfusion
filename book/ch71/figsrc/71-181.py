import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
from matplotlib.patches import Ellipse
fig, ax = canvas(70)
text(ax, 22, 66, 'courbe 1', 'encre', 's'); text(ax, 66, 66, 'courbe 2', 'encre', 's')
box(ax, 4, 52, 36, 9, 'autre', label='36 − 100 = −64', size='m')
box(ax, 48, 52, 36, 9, 'autre', label='16 − 4 = 12', size='m')
arrow(ax, (22, 52), (22, 46), 'varie'); arrow(ax, (66, 52), (66, 46), 'varie')
text(ax, 22, 43, 'négatif', 'varie', 's'); text(ax, 66, 43, 'positif', 'varie', 's')
ax.add_patch(Ellipse((22, 26), 28, 16, ec=COL['sujet'], fc=FILL['sujet'], lw=1.3, zorder=2))
for sg in (1, -1):
    line(ax, [(66 + sg * 6 * math.cosh(t / 10), 26 + 7 * math.sinh(t / 10)) for t in range(-12, 13)], 'sujet', lw=1.3)
text(ax, 22, 9, 'ellipse', 'sujet', 'm'); text(ax, 66, 9, 'courbe ouverte', 'sujet', 'm')
save(fig, '71-181')
