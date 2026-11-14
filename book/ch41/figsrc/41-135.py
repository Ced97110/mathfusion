import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig, ax = canvas(62)
k = 5.0
O = (20, 30)
u = (1, -1); v = (4, 5)
tu = (O[0] + u[0] * k, O[1] + u[1] * k)
tv = (O[0] + v[0] * k, O[1] + v[1] * k)
arrow(ax, (4, O[1]), (44, O[1]), 'fixe', lw=0.8)
arrow(ax, (O[0], 16), (O[0], 60), 'fixe', lw=0.8)
arrow(ax, O, tu, 'sujet', lw=1.5)
arrow(ax, O, tv, 'autre', lw=1.5)
a1 = math.degrees(math.atan2(-1, 1)); a2 = math.degrees(math.atan2(5, 4))
ax.add_patch(Arc(O, 22, 22, theta1=a1, theta2=a2, color=COL['varie'], lw=1.3, zorder=3))
text(ax, 34, 29, r'$\theta$', 'varie', 'l')
text(ax, 29, 22.5, r'$u=\langle 1,-1\rangle$', 'sujet', 's')
text(ax, 33, 58, r'$v=\langle 4,5\rangle$', 'autre', 's')
box(ax, 48, 48, 38, 9, 'fixe', label=r'$u\cdot v=4-5=-1$', size='s')
box(ax, 48, 34, 38, 9, 'fixe', label=r'$\|u\|\|v\|=\sqrt{2}\sqrt{41}$', size='s')
box(ax, 48, 20, 38, 9, 'fixe', label=r'$\cos\theta\approx-0{,}1104$', size='s')
box(ax, 48, 6, 38, 9, 'resultat', label=r'$\theta\approx 96{,}3°$', size='m')
for y in (47.5, 33.5, 19.5):
    arrow(ax, (67, y), (67, y - 3.5), 'fixe')
save(fig, '41-135')
