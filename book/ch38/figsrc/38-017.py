import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig, ax = canvas(58)
ta, tb = math.tan(math.radians(18)), math.tan(math.radians(21.25))
gy = 18
A = (8, gy); H = (82, gy)
hh = (H[0] - A[0]) * ta
B = (H[0] - hh / tb, gy)
S = (H[0], gy + hh)
line(ax, [A, H], 'fixe', lw=1.0)
line(ax, [A, S], 'sujet', lw=1.3)
line(ax, [B, S], 'varie', lw=1.3)
ax.add_patch(Arc(A, 14, 14, theta1=0, theta2=18, ec=COL['sujet'], lw=1.2, zorder=3))
ax.add_patch(Arc(B, 22, 22, theta1=0, theta2=21.25, ec=COL['varie'], lw=1.3, zorder=3))
# angle en S, entre les deux visées : de 180+18 à 180+21,25 degrés
r = 34
ax.add_patch(Arc(S, 2 * r, 2 * r, theta1=198, theta2=201.25, ec=COL['resultat'], lw=2.0, zorder=3))
mid = math.radians(199.6)
M = (S[0] + r * math.cos(mid), S[1] + r * math.sin(mid))
arrow(ax, (M[0] - 4, M[1] + 12), (M[0], M[1] + 1.2), 'resultat', lw=0.9)
text(ax, M[0] - 4, M[1] + 15, '3,25° en $S$', 'resultat', 's')
for p, role in ((A, 'sujet'), (B, 'varie'), (S, 'resultat'), (H, 'fixe')):
    disc(ax, p[0], p[1], 1.2, role)
text(ax, A[0], gy - 4, '$A$', 'sujet', 's')
text(ax, B[0], gy - 4, '$B$', 'varie', 's')
text(ax, H[0], gy - 4, '$H$', 'fixe', 's')
text(ax, S[0], S[1] + 4, '$S$', 'resultat', 's')
text(ax, 44, 6, r'$\beta - \alpha$ = 21,25° − 18° = 3,25°', 'resultat', 'm')
save(fig, '38-017')
