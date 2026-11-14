import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig, ax = canvas(56)
ta, tb = math.tan(math.radians(18)), math.tan(math.radians(21.25))
gy = 20
A = (12, gy); H = (82, gy)
h_mm = (H[0] - A[0]) * ta                      # hauteur à l'échelle, vraie pour 18°
B = (H[0] - h_mm / tb, gy)                     # vraie pour 21,25°
S = (H[0], gy + h_mm)
poly(ax, [A, B, S], 'sujet')
line(ax, [A, H], 'fixe')
line(ax, [A, S], 'sujet', lw=1.0)
line(ax, [B, S], 'sujet', lw=1.0)
line(ax, [A, B], 'sujet', lw=2.4)
line(ax, [S, H], 'resultat', lw=1.6, dash=True)
ax.add_patch(Arc(A, 18, 18, theta1=0, theta2=18, ec=COL['varie'], lw=1.2, zorder=3))
ax.add_patch(Arc(B, 9, 9, theta1=0, theta2=21.25, ec=COL['varie'], lw=1.2, zorder=3))
for p in (A, B, S, H):
    disc(ax, p[0], p[1], 1.0, 'sujet' if p != H else 'fixe')
text(ax, A[0], gy - 4, '$A$', 'sujet', 's')
text(ax, B[0], gy - 4, '$B$', 'sujet', 's')
text(ax, H[0], gy - 4, '$H$', 'fixe', 's')
text(ax, S[0] + 1.5, S[1] + 3.5, '$S$', 'sujet', 's')
text(ax, A[0] - 3, gy - 9.5, '18°', 'varie', 's')
text(ax, B[0] + 6, gy - 9.5, '21,25°', 'varie', 's')
text(ax, (A[0] + B[0]) / 2, 5.5, 'base 1 000 m', 'sujet', 's')
text(ax, H[0] - 2, gy + h_mm / 2, 'ℎ ≈ 1 976 m', 'resultat', 's', ha='right')
text(ax, 44, 52, 'une base + des angles → ℎ', 'encre', 's')
save(fig, '38-005')
