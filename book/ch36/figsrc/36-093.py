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
fig, ax = canvas(70)
k = 0.33; A = (6, 30); B = (A[0] + 90 * k, 30)
C = (A[0] + 120 * k * math.cos(math.radians(50)), 30 + 120 * k * math.sin(math.radians(50)))
cen = ((A[0] + B[0] + C[0]) / 3, (30 + 30 + C[1]) / 3)
poly(ax, [A, B, C], 'sujet'); line(ax, [B, C], 'resultat', 2.0); arc(ax, A, 7, 0, 50, 'fixe')
text(ax, 17, 33.4, '50°', 'fixe', 's')
side(ax, A, B, cen, '90', 'sujet'); side(ax, A, C, cen, '120', 'sujet', 4.2); side(ax, B, C, cen, '92,82', 'resultat', 6.5)
for y, role, lab in ((56, 'sujet', '120² + 90² = 22 500'), (44, 'varie', '− correction 13 884,2'), (32, 'fixe', 'a² = 8 615,8'), (20, 'resultat', 'a = √8 615,8 ≈ 92,82')):
    box(ax, 48, y, 38, 9, role, label=lab, size='s')
for y in (56, 44, 32): arrow(ax, (67, y), (67, y - 3), 'fixe')
f = numberline(ax, 8, 80, 9, 30, 210, step=30, labels=False, arrow_right=False)
disc(ax, f(92.82), 9, 1.6, 'resultat')
text(ax, f(92.82), 13.5, '92,82', 'resultat', 's'); text(ax, f(30), 5.6, '30', 'fixe', 's'); text(ax, f(210), 5.6, '210', 'fixe', 's')
text(ax, 60, 13.5, 'a reste entre 30 et 210', 'fixe', 's')
save(fig, '36-093')
