import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# Échelle 1 mm = 3,6 km/h : a = 50 mm ; v = 27,78 mm à 60°. Coin opposé = a + v.
fig, ax = canvas(52)
k = 3.6
O = (8, 10)
A = (O[0] + 180 / k, O[1])
V = (O[0] + 100 / k * math.cos(math.radians(60)), O[1] + 100 / k * math.sin(math.radians(60)))
R = (A[0] + V[0] - O[0], A[1] + V[1] - O[1])
poly(ax, [O, A, R, V], 'sujet')
def dashed(p, q, role):
    line(ax, [p, q], role, lw=0.9, dash=True)
    arrow(ax, (q[0] + (p[0] - q[0]) * 0.1, q[1] + (p[1] - q[1]) * 0.1), q, role, lw=0.9)
dashed(V, R, 'sujet')   # copie de a
dashed(A, R, 'varie')   # copie de v
arrow(ax, O, A, 'sujet', lw=1.5)
arrow(ax, O, V, 'varie', lw=1.5)
arrow(ax, O, R, 'resultat', lw=1.7)
disc(ax, O[0], O[1], 1.1, 'encre')
ax.add_patch(Arc(O, 14, 14, theta1=0, theta2=60, color=COL['fixe'], lw=0.8, zorder=3))
text(ax, 4.5, 6.5, r'$O$', 'encre', 'm')
text(ax, 33, 6, r'$a$ : 180', 'sujet', 's')
text(ax, 12.5, 26, r'$v$ : 100', 'varie', 's', ha='right')
text(ax, 18.5, 17.5, '60°', 'fixe', 's')
text(ax, 44, 22, r'$r$', 'resultat', 'l')
text(ax, R[0], R[1] + 5, 'même coin', 'encre', 's')
text(ax, 72, 8, r'$r$ < 280', 'resultat', 's')
save(fig, '41-008')
