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
fig, ax = canvas(56)
s = 3.2; A = (36, 20); C = (A[0] + s * 10 * math.cos(math.radians(130)), A[1] + s * 10 * math.sin(math.radians(130)))
line(ax, [(2, 20), A], 'fixe', 0.8, dash=True); line(ax, [A, (82, 20)], 'fixe', 1.2); line(ax, [A, C], 'fixe', 1.8)
arc(ax, C, 12 * s, 300, 340, 'resultat', 1.4); arc(ax, C, 8 * s, 248, 292, 'limite', 1.4)
Bp = (A[0] + s * 2.81, 20)
disc(ax, Bp[0], 20, 1.6, 'resultat')
for x in (C[0] - s * 2.31, C[0] + s * 2.31): disc(ax, x, 20, 1.5, 'limite')
arc(ax, A, 7, 0, 130, 'fixe')
text(ax, 40.6, 30, '130°', 'fixe', 's'); text(ax, 28.4, 34.5, '10', 'fixe', 's')
text(ax, 48.5, 16, '2,81', 'resultat', 's')
text(ax, 20, 14, 'a = 8 : aucun triangle', 'limite', 's'); text(ax, 62, 8, 'a = 12 : 1 triangle', 'resultat', 's')
save(fig, '36-091')
