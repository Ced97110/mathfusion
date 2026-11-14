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
X = lambda d: 8 + 0.4 * d; Y = lambda v: 18 + 36 * v
line(ax, [(X(d), Y(math.sin(math.radians(d)))) for d in range(0, 181, 2)], 'fixe', 1.4)
numberline(ax, 8, 80, 18, 0, 180, step=30, labels=False, arrow_right=False)
line(ax, [(8, Y(0.5)), (80, Y(0.5))], 'varie', 0.9, dash=True)
for d, r in ((30, 'sujet'), (150, 'autre')):
    line(ax, [(X(d), 18), (X(d), Y(0.5))], r, 0.8, dash=True); disc(ax, X(d), Y(0.5), 1.7, r)
    text(ax, X(d), 13.8, f'{d}°', r, 's')
for d in (0, 90, 180): text(ax, X(d), 13.8, f'{d}°', 'fixe', 's')
text(ax, 4, Y(0.5), '0,5', 'varie', 's'); text(ax, 4, Y(1), '1', 'fixe', 's')
brace(ax, X(30), X(150), 10.8, 'fixe', label='30° + 150° = 180°')
text(ax, 25, 60, 'la calculatrice donne 30°', 'sujet', 's')
arrow(ax, (17, 58), (19.5, 38.5), 'sujet')
save(fig, '36-077')
