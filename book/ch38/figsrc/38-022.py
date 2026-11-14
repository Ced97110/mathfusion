import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Ellipse
import math
fig, ax = canvas(64)
cx = 40
# axe vertical et cercle horizontal (bleu)
line(ax, [(cx, 6), (cx, 58)], 'sujet', lw=1.0, dash=True)
ax.add_patch(Ellipse((cx, 16), 40, 8, ec=COL['sujet'], fc=FILL['sujet'], lw=1.0, zorder=1))
arrow(ax, (cx - 14, 12.5), (cx + 14, 12.5), 'sujet', lw=1.0, curve=0.35)
text(ax, 66, 14, 'cercle', 'sujet', 's')
text(ax, 66, 9, 'horizontal', 'sujet', 's')
text(ax, cx, 3, 'axe vertical', 'sujet', 's')
# axe horizontal (vers vous) et cercle vertical (orange)
C = (cx, 38)
disc(ax, C[0], C[1], 10, 'varie')
for k in range(24):
    a = math.radians(15 * k)
    line(ax, [(C[0] + 8.6 * math.cos(a), C[1] + 8.6 * math.sin(a)), (C[0] + 10 * math.cos(a), C[1] + 10 * math.sin(a))], 'varie', lw=0.5)
tip = (C[0] + 20 * math.cos(math.radians(30)), C[1] + 20 * math.sin(math.radians(30)))
line(ax, [C, tip], 'encre', lw=2.2)
disc(ax, C[0], C[1], 1.6, 'varie')
text(ax, 80, 52, 'lunette', 'encre', 's')
text(ax, 12, 52, 'cercle vertical', 'varie', 's')
text(ax, 12, 47, 'axe horizontal', 'varie', 's')
text(ax, 12, 42, '(vers vous)', 'varie', 's')
save(fig, '38-022')
