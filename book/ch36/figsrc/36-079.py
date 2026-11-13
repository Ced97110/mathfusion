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
fig, ax = canvas(54)
s = 4.4; A = (6, 20)
P = lambda x, y: (A[0] + s * x, A[1] + s * y)
C, F, B1, B2 = P(8.66, 5), P(8.66, 0), P(3.76, 0), P(13.56, 0)
line(ax, [A, (82, 20)], 'fixe', 1.0); line(ax, [A, C], 'sujet', 1.8)
line(ax, [C, F], 'varie', 0.9, dash=True)
line(ax, [C, B1], 'varie', 0.8, dash=True); line(ax, [C, B2], 'varie', 0.8, dash=True)
arc(ax, C, 7 * s, 225.6, 314.4, 'varie', 1.3)
disc(ax, B1[0], B1[1], 1.4, 'resultat'); disc(ax, B2[0], B2[1], 1.4, 'resultat')
arc(ax, A, 11, 0, 30, 'fixe')
text(ax, A[0] + 7.2, A[1] + 1.9, '30°', 'fixe', 's')
text(ax, 23.4, 33.8, '10', 'sujet', 's')
text(ax, F[0] + 2.2, 31, '5', 'varie', 's', ha='left')
text(ax, 57.5, 32.5, '7', 'varie', 's')
text(ax, B1[0], 16.3, '3,76', 'resultat', 's'); text(ax, B2[0], 16.3, '13,56', 'resultat', 's')
brace(ax, A[0], F[0], 13, 'fixe', label='8,66')
text(ax, 44, 4.5, 'deux positions pour B', 'resultat', 's')
save(fig, '36-079')
