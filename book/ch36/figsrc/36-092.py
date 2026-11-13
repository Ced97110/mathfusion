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
fig, ax = canvas(58)
k = 12; Pp = (8, 12); Q = (8 + 6 * k, 12); R = (8 + 3.5833 * k, 12 + 1.7776 * k)
poly(ax, [Pp, Q, R], 'fixe'); line(ax, [Pp, R], 'fixe', 1.2); line(ax, [Q, R], 'fixe', 1.2); line(ax, [Pp, Q], 'resultat', 2.4)
a1 = math.degrees(math.atan2(Pp[1] - R[1], Pp[0] - R[0])) % 360; a2 = math.degrees(math.atan2(Q[1] - R[1], Q[0] - R[0])) % 360
arc(ax, R, 7, a1, a2, 'sujet', 1.6)
text(ax, 51, 22, '117,28°', 'sujet', 's'); text(ax, 44, 7.8, '6', 'resultat', 'm')
text(ax, 25.5, 26.5, '4', 'fixe', 'm'); text(ax, 69.5, 26.5, '3', 'fixe', 'm')
text(ax, 44, 45, r'$6^2 = 36 > 3^2 + 4^2 = 25$', 'sujet', 'l')
text(ax, 44, 53, 'face au plus grand côté', 'resultat', 'm')
save(fig, '36-092')
