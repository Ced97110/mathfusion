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
k = 0.3; A = (8, 12); B = (A[0] + 90 * k, 12)
C90 = (8, 12 + 120 * k); C50 = (8 + 120 * k * math.cos(math.radians(50)), 12 + 120 * k * math.sin(math.radians(50)))
poly(ax, [A, B, C50], 'sujet'); line(ax, [A, B], 'fixe', 1.4); line(ax, [A, C50], 'sujet', 1.4); line(ax, [B, C50], 'sujet', 1.8)
line(ax, [A, C90], 'autre', 1.0, dash=True); line(ax, [B, C90], 'autre', 1.2, dash=True)
arc(ax, A, 6, 0, 50, 'sujet', 1.3); arc(ax, A, 9, 50, 90, 'autre', 1.3)
text(ax, 17.5, 15.2, '50°', 'sujet', 's'); text(ax, 13.2, 25, '90°', 'autre', 's')
text(ax, 4, 30, '120', 'fixe', 's'); text(ax, (A[0] + B[0]) / 2, 8, '90', 'fixe', 's')
box(ax, 50, 36, 36, 8, 'autre', label='150', size='s'); box(ax, 50, 24, 22.3, 8, 'sujet', label='92,82', size='s')
box(ax, 72.3, 24, 13.7, 8, 'varie', label='−57,18', size='s')
text(ax, 68, 17, 'la correction retire 57,18', 'varie', 's')
save(fig, '36-094')
