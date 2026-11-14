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
s = 3.0; A = (12, 24); C = (A[0] + s * 8.66, A[1] + s * 5)
Bp = (A[0] + s * 19.57, 24); Bm = (A[0] - s * 2.25, 24)
line(ax, [(3, 24), A], 'fixe', 0.8, dash=True); line(ax, [A, (82, 24)], 'fixe', 1.2); line(ax, [A, C], 'fixe', 1.8)
arc(ax, C, 12 * s, 204.6, 335.4, 'varie', 1.3)
line(ax, [C, Bp], 'varie', 0.8, dash=True); disc(ax, Bp[0], 24, 1.6, 'resultat'); disc(ax, Bm[0], 24, 1.6, 'limite')
arc(ax, A, 5, 0, 30, 'fixe')
text(ax, 21, 25.4, '30°', 'fixe', 's'); text(ax, 22.4, 35.4, '10', 'fixe', 's')
text(ax, 57.5, 33.3, 'a = 12', 'varie', 's'); text(ax, Bp[0], 28, '19,57', 'resultat', 's')
text(ax, Bm[0] + 0.5, 28.5, '−2,25', 'limite', 's'); text(ax, 1.5, 33, 'hors demi-droite', 'limite', 's', ha='left')
text(ax, 38, 9, 'un seul triangle', 'resultat', 'm')
save(fig, '36-087')
