import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# 41-034 : au-delà de 90°, le cercle unité donne les signes : (cos 120°, sin 120°) = (−0,5 ; 0,866)
fig, ax = canvas(96)
C = (44, 56); R = 26
th = math.radians(120)
P = (C[0] + R * math.cos(th), C[1] + R * math.sin(th))      # (cos, sin) à l'échelle du cercle
ax.add_patch(Circle(C, R, ec=COL['fixe'], fc='none', lw=0.9, zorder=1))
arrow(ax, (C[0] - R - 6, C[1]), (C[0] + R + 8, C[1]), 'fixe', lw=0.7)
arrow(ax, (C[0], C[1] - R - 4), (C[0], C[1] + R + 6), 'fixe', lw=0.7)
Fx = (P[0], C[1]); Fy = (C[0], P[1])
line(ax, [P, Fx], 'fixe', dash=True); line(ax, [P, Fy], 'fixe', dash=True)
line(ax, [C, Fx], 'sujet', lw=2.2)       # cos < 0 : vers l'ouest
line(ax, [C, Fy], 'resultat', lw=2.2)    # sin > 0 : vers le nord
arrow(ax, C, P, 'varie', lw=1.4)
ax.add_patch(Arc(C, 14, 14, theta1=0, theta2=120, ec=COL['fixe'], lw=1.0, zorder=3))
text(ax, C[0] + 12, C[1] + 9.5, '$\\theta$ = 120°', 'fixe', 's')
text(ax, P[0] - 1, P[1] + 4, '(−0,5 ; 0,866)', 'varie', 's', ha='right')
text(ax, C[0] + 3, C[1] - 3, 'est', 'fixe', 's', ha='left')
text(ax, C[0] - R - 4, C[1] + 3.2, 'ouest', 'fixe', 's')
text(ax, 44, 22, 'cos θ = −0,5  →  a = −50', 'sujet', 's')
text(ax, 44, 14, 'sin θ ≈ 0,866  →  b = 86,60', 'resultat', 's')
text(ax, 44, 6, 'norme 100, angle 120°', 'fixe', 's')
save(fig, '41-034')
