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
s = 4.4; A = (6, 12)
P = lambda x, y: (A[0] + s * x, A[1] + s * y)
C, B1, B2 = P(8.66, 5), P(3.76, 0), P(13.56, 0)
poly(ax, [A, B2, C], 'sujet'); poly(ax, [A, B1, C], 'autre')
line(ax, [A, (82, 12)], 'fixe', 1.0)
line(ax, [A, C], 'fixe', 1.8)
line(ax, [C, B2], 'sujet', 1.3); line(ax, [C, B1], 'autre', 1.3)
arc(ax, A, 11, 0, 30, 'fixe'); arc(ax, B2, 6, 134.42, 180, 'sujet'); arc(ax, B1, 4, 45.58, 180, 'autre')
text(ax, A[0] + 7.2, A[1] + 1.9, '30°', 'fixe', 's')
text(ax, 22.8, 26.9, '10 cm', 'fixe', 's')
text(ax, 58.5, 26.2, '7 cm', 'sujet', 's')
text(ax, B1[0], 7.2, '134,42°', 'autre', 's')
text(ax, B2[0], 7.2, '45,58°', 'sujet', 's')
text(ax, 44, 47, 'même sinus : 0,7143', 'encre', 'm')
save(fig, '36-073')
