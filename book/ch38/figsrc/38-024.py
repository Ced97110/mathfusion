import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig, ax = canvas(56)
# un triangle sur le terrain : une base mesurée + deux angles
A, B, P = (8, 14), (34, 14), (28, 40)
poly(ax, [A, B, P], 'sujet')
line(ax, [A, B], 'sujet', lw=2.4)
for q, a1, a2 in ((A, 0, math.degrees(math.atan2(26, 20))), (B, 180 - math.degrees(math.atan2(26, 6)), 180)):
    ax.add_patch(Arc(q, 12, 12, theta1=a1, theta2=a2, ec=COL['varie'], lw=1.3, zorder=3))
for q in (A, B, P):
    disc(ax, q[0], q[1], 1.2, 'sujet')
text(ax, 21, 8, 'base mesurée', 'sujet', 's')
text(ax, 21, 3, 'angles mesurés', 'varie', 's')
arrow(ax, (40, 28), (50, 28), 'varie')
# ce que la méthode donne
text(ax, 68, 52, 'topographie', 'resultat', 'l')
for i, w in enumerate(('positions', 'distances', 'hauteurs', 'surfaces')):
    box(ax, 52, 36 - i * 10, 32, 7, 'resultat', label=w, size='s')
save(fig, '38-024')
