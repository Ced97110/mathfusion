import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
from matplotlib.patches import Arc
fig, ax = canvas(62)
ox, oy, s = 10, 8, 16
P = lambda x, y: (ox + s * x, oy + s * y)
O, U, V, H = P(0, 0), P(1, 3), P(4, 2), P(2, 1)
arrow(ax, O, V, 'autre', lw=1.4)
arrow(ax, O, U, 'sujet', lw=1.4)
line(ax, [U, H], 'fixe', lw=1.0, dash=True)
# angle droit en H (côtés le long de OH et de HU)
ux, uy = 2 / math.sqrt(5), 1 / math.sqrt(5)
q = 2.6
line(ax, [(H[0] - q * ux, H[1] - q * uy), (H[0] - q * ux - q * uy, H[1] - q * uy + q * ux), (H[0] - q * uy, H[1] + q * ux)], 'fixe', lw=0.8)
arrow(ax, O, H, 'resultat', lw=3.0)
ax.add_patch(Arc(O, 20, 20, theta1=math.degrees(math.atan2(1, 2)), theta2=math.degrees(math.atan2(3, 1)), color=COL['varie'], lw=1.4, zorder=4))
text(ax, O[0] - 2.5, O[1] - 2.5, r'$O$', 'encre', 'm')
text(ax, U[0] - 2.5, U[1] + 2.5, r'$U$', 'sujet', 'm')
text(ax, V[0] + 3, V[1] + 1.5, r'$V$', 'autre', 'm')
text(ax, H[0] + 2.5, H[1] - 3.5, r'$H$', 'resultat', 'm')
text(ax, O[0] + 15, O[1] + 14, r'$\theta$', 'varie', 'm')
text(ax, 38, 7, r'$OH\approx2{,}236$', 'resultat', 's')
text(ax, 46, 58, r'$OU\approx3{,}162$', 'sujet', 's')
save(fig, '41-093')
