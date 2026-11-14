import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
import math
fig, ax = canvas(56)
k = 3.2; L = (14, 22); R = (66, 22); th = math.degrees(math.atan2(4, 3))
def vec(o, v, role): arrow(ax, o, (o[0] + v[0] * k, o[1] + v[1] * k), role, lw=1.3)
vec(L, (3, 4), 'sujet'); vec(L, (5, 0), 'autre'); vec(R, (-4, 3), 'sujet'); vec(R, (0, 5), 'autre')
ax.add_patch(Wedge(L, 7, 0, th, fc=FILL['resultat'], ec=COL['resultat'], lw=0.6, zorder=1))
ax.add_patch(Wedge(R, 7, 90, 90 + th, fc=FILL['resultat'], ec=COL['resultat'], lw=0.6, zorder=1))
text(ax, L[0] + 9.6, L[1] + 16.5, r'$x$', 'sujet'); text(ax, L[0] + 18, L[1], r'$y$', 'autre')
text(ax, R[0] - 14, R[1] + 10, r'$Ax$', 'sujet'); text(ax, R[0], R[1] + 19, r'$Ay$', 'autre')
text(ax, L[0] + 12.5, L[1] + 6, '53,13°', 'resultat', 's'); text(ax, R[0] - 6, R[1] + 12, '53,13°', 'resultat', 's')
arrow(ax, (34, 40), (50, 40), 'varie', lw=1.3); text(ax, 42, 44.5, r'$A$', 'varie', 'l')
text(ax, 22, 9, r'$\cos\theta=0{,}6$', 'sujet'); text(ax, 66, 9, r'$\cos\theta=0{,}6$', 'resultat')
text(ax, 44, 9, '=', 'resultat', 'l')
save(fig, '73-092')
