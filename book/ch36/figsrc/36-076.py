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
A = (8, 16); B = (26, 16); C = (8 + 24 * math.cos(math.radians(50)), 16 + 24 * math.sin(math.radians(50)))
cen = ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)
poly(ax, [A, B, C], 'sujet'); line(ax, [A, B], 'sujet', 1.2); line(ax, [A, C], 'sujet', 1.2); line(ax, [B, C], 'resultat', 2.0)
arc(ax, A, 6, 0, 50, 'resultat', 1.4)
text(ax, 20.5, 19.6, '50°', 'resultat', 's')
side(ax, A, B, cen, '90', 'sujet'); side(ax, A, C, cen, '120', 'sujet', 4.2); side(ax, B, C, cen, 'a = 92,82', 'resultat', 8)
box(ax, 46, 46, 38, 9, 'varie', label='loi des cosinus', size='s')
box(ax, 46, 27, 38, 10, 'resultat', label='côté 92,82 + angle 50°', size='s')
box(ax, 46, 8, 38, 9, 'sujet', label='loi des sinus', size='s')
arrow(ax, (65, 46), (65, 37.5), 'varie'); arrow(ax, (65, 27), (65, 17.5), 'resultat')
save(fig, '36-076')
