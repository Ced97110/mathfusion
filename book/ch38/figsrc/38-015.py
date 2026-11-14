import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig, ax = canvas(50)
gy = 12
A = (10, gy)
L = 66
S = (A[0] + L * math.cos(math.radians(18)), gy + L * math.sin(math.radians(18)))
H = (S[0], gy)
line(ax, [A, H], 'fixe', lw=1.0)
poly(ax, [A, S, H], 'fixe')
line(ax, [A, S], 'sujet', lw=1.6)
ax.add_patch(Arc(A, 40, 40, theta1=0, theta2=18, ec=COL['varie'], lw=1.3, zorder=3))
disc(ax, A[0], A[1], 1.4, 'sujet')
disc(ax, S[0], S[1], 1.3, 'sujet')
text(ax, A[0], gy - 5, '$A$', 'sujet', 'm')
text(ax, S[0], S[1] + 4, '$S$', 'sujet', 'm')
text(ax, 38, gy + 5.2, r'$\alpha$ = 18°', 'varie', 'm')
text(ax, 36, 33, 'visée $AS$', 'sujet', 's')
text(ax, 60, gy - 5, 'sol', 'fixe', 's')
save(fig, '38-015')
