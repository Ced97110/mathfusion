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
fig, ax = canvas(46)
s = 3.0; A = (10, 24); C = (A[0] + s * 8.66, A[1] + s * 5)
line(ax, [(2, 24), A], 'fixe', 0.8, dash=True); line(ax, [A, (82, 24)], 'fixe', 1.2); line(ax, [A, C], 'fixe', 1.8)
arc(ax, C, 10 * s, 210, 330, 'varie', 1.4); arc(ax, C, 11 * s, 207, 333, 'autre', 1.2)
disc(ax, A[0], 24, 1.6, 'sujet'); disc(ax, 10 + s * 17.32, 24, 1.5, 'resultat')
disc(ax, 10 - s * 1.14, 24, 1.5, 'limite'); disc(ax, 10 + s * 18.46, 24, 1.5, 'resultat')
arc(ax, A, 5, 0, 30, 'fixe')
text(ax, 19, 25.4, '30°', 'fixe', 's'); text(ax, 21, 35.3, '10', 'fixe', 's')
text(ax, 10, 27.5, r'$A$', 'sujet', 's'); text(ax, 4, 28.8, '−1,14', 'limite', 's')
text(ax, 36, 14.5, 'a = 10 : passe par A', 'varie', 's'); text(ax, 36, 2.8, 'a = 11 : derrière A', 'autre', 's')
save(fig, '36-088')
