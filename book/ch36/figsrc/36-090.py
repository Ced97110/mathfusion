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
fig, ax = canvas(52)
s = 5.0; A = (6, 18)
P = lambda x, y: (A[0] + s * x, A[1] + s * y)
C, B1, B2 = P(8.66, 5), P(3.76, 0), P(13.56, 0)
poly(ax, [B1, B2, C], 'fixe')
text(ax, 68, 45, 'triangle isocèle :\n$CB_1=CB_2=7$', 'encre', 's')
line(ax, [A, (82, 18)], 'fixe', 1.0); line(ax, [A, C], 'fixe', 1.2)
line(ax, [C, B1], 'autre', 1.6); line(ax, [C, B2], 'sujet', 1.6)
for Q in (B1, B2):
    m = ((C[0] + Q[0]) / 2, (C[1] + Q[1]) / 2); dx, dy = Q[0] - C[0], Q[1] - C[1]; n = math.hypot(dx, dy)
    for t in (-0.7, 0.7):
        mt = (m[0] + t * dx / n, m[1] + t * dy / n)
        line(ax, [(mt[0] - 1.6 * dy / n, mt[1] + 1.6 * dx / n), (mt[0] + 1.6 * dy / n, mt[1] - 1.6 * dx / n)], 'encre', 1.3)
arc(ax, B1, 5, 45.58, 180, 'autre', 1.5); arc(ax, B1, 8, 0, 45.58, 'sujet', 1.5); arc(ax, B2, 7, 134.42, 180, 'sujet', 1.5)
for Q in (A, B1, B2): disc(ax, Q[0], Q[1], 1.1, 'encre')
text(ax, A[0], 13.6, r'$A$', 'encre', 's'); text(ax, B1[0], 13.6, r'$B_1$', 'encre', 's'); text(ax, B2[0], 13.6, r'$B_2$', 'encre', 's')
text(ax, C[0], 46.6, r'$C$', 'encre', 's')
text(ax, B1[0] - 7, 9, '134,42°', 'autre', 's'); text(ax, B1[0] + 7, 9, '45,58°', 'sujet', 's'); text(ax, B2[0], 9, '45,58°', 'sujet', 's')
text(ax, 40.3, 28, '7', 'autre', 's'); text(ax, 58.3, 28, '7', 'sujet', 's')
text(ax, 44, 3.5, '134,42° + 45,58° = 180°', 'encre', 's')
save(fig, '36-090')
