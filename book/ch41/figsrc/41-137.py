import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig, ax = canvas(62)
k = 3.0
def vec(O, c):
    return (O[0] + c[0] * k, O[1] + c[1] * k)
OL, OR = (20, 34), (62, 34)
# gauche : orthogonaux
arrow(ax, OL, vec(OL, (4, 3)), 'sujet', lw=1.5)
arrow(ax, OL, vec(OL, (3, -4)), 'autre', lw=1.5)
a = (4 / 5, 3 / 5); b = (3 / 5, -4 / 5); s = 3.0
sq = [(OL[0] + s * a[0], OL[1] + s * a[1]), (OL[0] + s * (a[0] + b[0]), OL[1] + s * (a[1] + b[1])), (OL[0] + s * b[0], OL[1] + s * b[1])]
ax.plot([p[0] for p in sq], [p[1] for p in sq], color=COL['resultat'], lw=1.0, zorder=4)
text(ax, 38.5, 43, r'$\langle 4,3\rangle$', 'sujet', 's')
text(ax, 29, 18.5, r'$\langle 3,-4\rangle$', 'autre', 's')
text(ax, 24, 56, 'orthogonaux', 'resultat', 'm')
text(ax, 24, 10, r'$4\times3+3\times(-4)=0$', 'resultat', 's')
# droite : pas orthogonaux
arrow(ax, OR, vec(OR, (4, 3)), 'sujet', lw=1.5)
arrow(ax, OR, vec(OR, (3, 4)), 'autre', lw=1.5)
ax.add_patch(Arc(OR, 14, 14, theta1=math.degrees(math.atan2(3, 4)), theta2=math.degrees(math.atan2(4, 3)), color=COL['limite'], lw=1.1, zorder=3))
text(ax, 80.5, 41, r'$\langle 4,3\rangle$', 'sujet', 's')
text(ax, 65, 51, r'$\langle 3,4\rangle$', 'autre', 's')
text(ax, 66, 58, 'pas orthogonaux', 'limite', 'm')
text(ax, 66, 24, r'$4\times3+3\times4=24$', 'limite', 's')
save(fig, '41-137')
