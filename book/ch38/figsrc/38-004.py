import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(56)
line(ax, [(44, 6), (44, 50)], 'fixe', lw=0.6, dash=True)
# gauche : longueur parcourue au ruban
text(ax, 22, 48, 'longueur', 'sujet', 'l')
y = 28
line(ax, [(5, y), (39, y)], 'sujet', lw=2.0)
for i in range(8):
    x = 5 + i * 34 / 7
    line(ax, [(x, y - 1.4), (x, y + 1.4)], 'sujet', lw=0.8)
disc(ax, 5, y + 5, 1.5, 'varie')
arrow(ax, (8, y + 5), (36, y + 5), 'varie')
text(ax, 22, 9, 'on la parcourt', 'varie', 's')
# droite : angle mesuré de loin
text(ax, 66, 48, 'angle', 'autre', 'l')
O = (52, 28)
T1, T2 = (84, 40), (84, 16)
line(ax, [O, T1], 'autre', lw=1.4)
line(ax, [O, T2], 'autre', lw=1.4)
disc(ax, O[0], O[1], 1.5, 'varie')
disc(ax, T1[0], T1[1], 1.2, 'autre')
disc(ax, T2[0], T2[1], 1.2, 'autre')
import math
a1 = math.degrees(math.atan2(12, 32)); a2 = -a1
ax.add_patch(Arc(O, 20, 20, theta1=a2, theta2=a1, ec=COL['varie'], lw=1.2, zorder=3))
text(ax, 52, 9, 'on le mesure de loin', 'autre', 's', ha='left')
text(ax, 50, 33, 'vous', 'varie', 's', ha='center')
text(ax, 71, 39, 'visée', 'autre', 's')
text(ax, 71, 17.5, 'visée', 'autre', 's')
text(ax, 66, 28, r'angle', 'varie', 's')
save(fig, '38-004')
