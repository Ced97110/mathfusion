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
V = (44, 16); tip = (V[0] + 34 * math.cos(math.radians(45.58)), V[1] + 34 * math.sin(math.radians(45.58)))
line(ax, [(6, 16), (82, 16)], 'fixe', 1.2); line(ax, [V, tip], 'encre', 1.5)
arc(ax, V, 14, 0, 45.58, 'sujet', 1.6); arc(ax, V, 10, 45.58, 180, 'autre', 1.6)
text(ax, 65.2, 21.7, '45,58°', 'sujet', 'm'); text(ax, 37.3, 32.7, '134,42°', 'autre', 'm')
text(ax, 28, 46, '134,42° = 180° − 45,58°', 'encre', 'm')
brace(ax, 8, 80, 12, 'fixe', label='ensemble : 180°')
save(fig, '36-089')
