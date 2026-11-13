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
fig, ax = canvas(48)
y = 20
f = numberline(ax, 8, 78, y, 0, 13, step=1, labels=False, arrow_right=False)
box(ax, f(0), 26, f(5) - 3.2 - f(0), 8, 'fixe', label='0 triangle', size='s')
box(ax, f(5) + 3.2, 26, f(10) - f(5) - 3.2, 8, 'resultat', label='2 triangles', size='s')
box(ax, f(10), 26, f(13) - f(10), 8, 'fixe', label='1 triangle', size='s')
disc(ax, f(5), 30, 2.6, 'fixe', label='1', size='s')
text(ax, f(0), 16.2, '0', 'fixe', 's'); text(ax, f(5), 16.2, 'h = 5', 'varie', 's'); text(ax, f(10), 16.2, 'b = 10', 'sujet', 's')
arrow(ax, (f(7), 6), (f(7), 18.4), 'varie'); text(ax, f(7), 3.2, 'a = 7', 'varie', 's')
text(ax, 44, 42, 'h < a < b : deux triangles', 'resultat', 'm')
save(fig, '36-083')
