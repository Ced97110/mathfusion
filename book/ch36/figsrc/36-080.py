import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, t0, t1, role='varie', lw=1.0, dash=False):
    ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t0, theta2=t1, color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3))
def ring(ax, c, r, role='varie', lw=1.0, dash=False):
    ax.add_patch(Circle(c, r, ec=COL[role], fc='none', lw=lw, ls='--' if dash else '-', zorder=3))
def side(ax, p, q, cen, s, role='encre', d=3.2, size='s'):
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2; vx, vy = mx - cen[0], my - cen[1]; n = math.hypot(vx, vy)
    text(ax, mx + d * vx / n, my + d * vy / n, s, role, size)
def inner(v, cen, k): return (v[0] + k * (cen[0] - v[0]), v[1] + k * (cen[1] - v[1]))
fig, ax = canvas(68)
s = 4.0; A = (10, 14)
P = lambda x, y: (A[0] + s * x, A[1] + s * y)
C, B1, B2 = P(8.66, 5), P(3.76, 0), P(13.56, 0)
line(ax, [A, (82, 14)], 'fixe', 1.2); line(ax, [A, C], 'fixe', 1.4)
ring(ax, C, 7 * s, 'varie', 1.3); line(ax, [C, B2], 'varie', 0.9, dash=True)
disc(ax, C[0], C[1], 1.0, 'sujet'); disc(ax, B1[0], B1[1], 1.7, 'resultat'); disc(ax, B2[0], B2[1], 1.7, 'resultat')
arc(ax, A, 7, 0, 30, 'fixe')
text(ax, 15.2, 16.3, '30°', 'fixe', 's'); text(ax, 22.3, 25.5, '10', 'fixe', 's')
text(ax, C[0] + 2.8, C[1] + 2.4, r'$C$', 'sujet', 's'); text(ax, 61, 24.5, 'rayon 7', 'varie', 's')
text(ax, B1[0], 10, r'$B_1$', 'resultat', 's'); text(ax, B2[0], 10, r'$B_2$', 'resultat', 's')
text(ax, 76, 9.5, 'demi-droite', 'fixe', 's')
text(ax, C[0], 65.6, 'cercle de centre C', 'varie', 's')
text(ax, C[0], 2.6, '2 points communs', 'resultat', 's')
save(fig, '36-080')
