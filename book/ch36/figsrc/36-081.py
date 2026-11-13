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
fig, ax = canvas(66)
s = 4.0; A = (10, 14)
P = lambda x, y: (A[0] + s * x, A[1] + s * y)
C, F, B1, B2 = P(8.66, 5), P(8.66, 0), P(3.76, 0), P(13.56, 0)
line(ax, [A, (82, 14)], 'fixe', 1.2); line(ax, [A, C], 'fixe', 1.4); line(ax, [C, F], 'fixe', 0.8, dash=True)
ring(ax, C, 4 * s, 'varie', 1.0, dash=True); ring(ax, C, 5 * s, 'varie', 1.2); ring(ax, C, 7 * s, 'varie', 1.4)
disc(ax, C[0], C[1], 1.0, 'sujet')
for p in (F, B1, B2): disc(ax, p[0], p[1], 1.6, 'resultat')
for r in (4, 5, 7):
    a = math.radians(60); text(ax, C[0] + (r * s + 2.2) * math.cos(a), C[1] + (r * s + 2.2) * math.sin(a), str(r), 'varie', 's')
arc(ax, A, 4, 0, 30, 'fixe'); text(ax, 18.3, 16.4, '30°', 'fixe', 's')
text(ax, C[0] + 2.4, 24, '5', 'fixe', 's', ha='left')
text(ax, 16, 2.6, '4 : aucun point', 'varie', 's'); text(ax, 44, 2.6, '5 : un point', 'resultat', 's'); text(ax, 72, 2.6, '7 : deux points', 'resultat', 's')
save(fig, '36-081')
