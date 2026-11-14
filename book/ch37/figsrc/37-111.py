import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
import math
P = (6, 22); Q = (34, 22); R = (6, 43)
poly(ax, [P, Q, R], 'sujet')
from matplotlib.patches import Arc
ax.add_patch(Arc(Q, 12, 12, theta1=143.13, theta2=180, ec=COL['varie'], lw=1.2, zorder=4))
line(ax, [(P[0], P[1] + 2.5), (P[0] + 2.5, P[1] + 2.5), (P[0] + 2.5, P[1])], 'fixe', lw=0.8)
text(ax, 20, 18.5, '4', 'sujet', 's'); text(ax, 2.5, 33, '3', 'sujet', 's'); text(ax, 23, 36, '5', 'sujet', 's')
text(ax, 22, 8, r'coin $Q$ : $\cos=0{,}8$ ; $\sin=0{,}6$', 'varie', 's')
bx, bw = 42, 44
box(ax, bx, 36, bw, 16, 'autre', label=r'Héron : $s=6$ ; restes 3, 2, 1' + '\n' + r'$\sqrt{6\times3\times2\times1}=6$', size='s')
box(ax, bx, 10, bw, 16, 'sujet', label='cosinus :\n' + r'$\frac{1}{2}\times4\times5\times0{,}6=6$', size='s')
for yy in (29.2, 32.8): line(ax, [(bx + bw / 2 - 5, yy), (bx + bw / 2 + 5, yy)], 'encre', lw=1.0)
save(fig, '37-111')
