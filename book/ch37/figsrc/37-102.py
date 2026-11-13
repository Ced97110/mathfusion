import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
u = 11.0; ox, oy = 9, 12
P = lambda x, y: (ox + u * x, oy + u * y)
from matplotlib.patches import Arc
A, B, C = P(0, 0), P(6, 0), P(5, 4)
poly(ax, [A, B, C], 'sujet')
ax.add_patch(Arc(A, 24, 24, theta1=0, theta2=38.66, ec=COL['varie'], lw=1.3, zorder=4))
text(ax, A[0] - 3, A[1] - 2.5, 'A', 'sujet', weight='bold')
text(ax, (A[0] + B[0]) / 2, A[1] - 3.5, r'$p = 6$', 'sujet')
text(ax, 25, 40, r'$q \approx 6{,}40$', 'sujet')
text(ax, 24, 8, r'$\alpha = 0°$', 'fixe', 's')
text(ax, 24, 17.5, r'$\beta-\alpha = 38{,}66°$', 'varie', 's', ha='left')
text(ax, 30, 66, r'$\Delta=\frac{1}{2}\,pq\,\sin(\beta-\alpha) = 12$', 'resultat', 'm')
save(fig, '37-102')
