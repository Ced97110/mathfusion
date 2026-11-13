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
k = 0.28; A = (6, 16); B = (A[0] + 90 * k, 16)
C = (A[0] + 120 * k * math.cos(math.radians(50)), 16 + 120 * k * math.sin(math.radians(50)))
cen = ((A[0] + B[0] + C[0]) / 3, (16 + 16 + C[1]) / 3)
poly(ax, [A, B, C], 'sujet'); line(ax, [A, B], 'sujet', 1.3); line(ax, [A, C], 'sujet', 1.3); line(ax, [B, C], 'sujet', 1.3)
side(ax, A, B, cen, '90', 'sujet'); side(ax, A, C, cen, '120', 'sujet', 3.6); side(ax, B, C, cen, '92,82', 'sujet', 6.5)
text(ax, A[0], 11, 'A 50°', 'fixe', 's'); text(ax, B[0] + 1, 11, 'B 82,03°', 'resultat', 's'); text(ax, C[0], C[1] + 4.5, 'C 47,97°', 'varie', 's')
for y, role, lab in ((43, 'fixe', '90 × 0,7660 = 68,94'), (31, 'sujet', 'sin C = 68,94 ÷ 92,82'), (19, 'varie', 'sin C ≈ 0,7428 → C ≈ 47,97°'), (7, 'resultat', 'B = 180° − 97,97° = 82,03°')):
    box(ax, 44, y, 42, 9, role, label=lab, size='s')
for y in (43, 31, 19): arrow(ax, (65, y), (65, y - 3), 'fixe')
save(fig, '36-096')
