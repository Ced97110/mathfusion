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
k = 0.28; A = (8, 34); B = (A[0] + 90 * k, A[1])
C = (A[0] + 120 * k * math.cos(math.radians(50)), A[1] + 120 * k * math.sin(math.radians(50)))
poly(ax, [A, B, C], 'sujet'); line(ax, [A, B, C, A], 'sujet', 1.3)
arc(ax, A, 7, 0, 50, 'fixe')
text(ax, A[0] + 12, A[1] + 3.6, '50°', 'fixe', 's')
text(ax, 12.5, 50.5, '120 m', 'sujet', 's', ha='right')
text(ax, (A[0] + B[0]) / 2, A[1] - 3.5, '90 m', 'sujet', 's')
text(ax, B[0] + 3.5, B[1] - 2.2, '?', 'varie', 'l'); text(ax, C[0], C[1] + 3.6, '?', 'varie', 'l')
text(ax, 64, 58, 'aucun côté connu avec\nson angle en face', 'encre', 's')
text(ax, 64, 45, 'égalité vraie avec 70° et 44,81° :\n120 ÷ sin 70° = 90 ÷ sin 44,81°', 'resultat', 's')
sc = 76 / 180; x = 6
box(ax, x, 14, 50 * sc, 9, 'fixe', label='50°', size='s'); x += 50 * sc
box(ax, x, 14, 70 * sc, 9, 'limite', label='70°', size='s'); x += 70 * sc
box(ax, x, 14, 44.81 * sc, 9, 'limite', label='44,81°', size='s'); x += 44.81 * sc
box(ax, x, 14, 6 + 76 - x + 0.0, 9, 'fixe', fill=False, dash=True)
line(ax, [(82, 12), (82, 25)], 'fixe', 0.8, dash=True)
text(ax, 82, 28, '180°', 'fixe', 's')
text(ax, 86, 9, 'manque 15,19°', 'limite', 's', ha='right')
text(ax, 36, 28, 'les trois angles : 164,81°', 'limite', 's')
save(fig, '36-075')
