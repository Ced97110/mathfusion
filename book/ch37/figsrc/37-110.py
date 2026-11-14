import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
import math
s = 0.42; ox, oy = 4, 33
A = (ox, oy); B = (ox + 60 * s, oy); C = (ox + 37.5 * s, oy + 33.07 * s)
poly(ax, [A, B, C], 'sujet')
from matplotlib.patches import Arc
ang = lambda P, Q: math.degrees(math.atan2(Q[1] - P[1], Q[0] - P[0])) % 360
ax.add_patch(Arc(C, 10, 10, theta1=ang(C, A), theta2=ang(C, B), ec=COL['varie'], lw=1.2, zorder=4))
text(ax, C[0], C[1] + 3.5, 'C', 'varie', weight='bold')
text(ax, (A[0] + B[0]) / 2, oy - 3, '60', 'sujet', 's')
text(ax, 8, 43, '50', 'sujet', 's'); text(ax, 31, 43, '40', 'sujet', 's')
bx, bw, h = 40, 46, 9.0
box(ax, bx, 49, bw, h, 'sujet', label=r'$\cos C = 1/8$', size='s')
box(ax, bx, 36, bw, h, 'sujet', label=r'$\sin C = 3\sqrt{7}/8$', size='s')
box(ax, bx, 23, bw, h, 'varie', label=r'$\Delta=\frac{1}{2}\times40\times50\times3\sqrt{7}/8$', size='s')
box(ax, bx, 8, bw, 10, 'resultat', label=r'$\Delta=375\sqrt{7}\approx 992{,}2$ m²', size='s')
for y0 in (49, 36, 23): arrow(ax, (bx + bw / 2, y0), (bx + bw / 2, y0 - 4), 'fixe')
box(ax, 4, 8, 26, 10, 'autre', label=r'Héron : $375\sqrt{7}$', size='s')
for dy in (-1.2, 1.2): line(ax, [(31, 13 + dy), (39, 13 + dy)], 'encre', lw=1.0)
save(fig, '37-110')
