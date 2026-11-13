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
fig, ax = canvas(62)
s = 4.4; A = (6, 14); C = (44.1, 36); B = (44.1, 14)
poly(ax, [A, B, C], 'sujet')
line(ax, [A, (82, 14)], 'fixe', 1.0); line(ax, [A, C], 'fixe', 1.8); line(ax, [C, B], 'resultat', 2.0)
ring(ax, C, 5 * s, 'varie', 1.2); disc(ax, B[0], B[1], 1.6, 'resultat')
line(ax, [(B[0] - 2.2, 14), (B[0] - 2.2, 16.2), (B[0], 16.2)], 'encre', 0.8)
arc(ax, A, 4, 0, 30, 'fixe')
text(ax, 14.3, 16.4, '30°', 'fixe', 's'); text(ax, 21.5, 29, '10', 'fixe', 's')
text(ax, 46.5, 25, 'a = h = 5', 'resultat', 's', ha='left')
text(ax, 48.2, 11.6, r'$B$', 'resultat', 's'); text(ax, 44, 6.5, 'angle droit en B', 'resultat', 's')
save(fig, '36-085')
