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
c50, s50 = math.cos(math.radians(50)), math.sin(math.radians(50))
def tri(O, k, role):
    A = O; B = (O[0] + 90 * k, O[1]); C = (O[0] + 120 * c50 * k, O[1] + 120 * s50 * k)
    poly(ax, [A, B, C], role); return A, B, C
A1, B1, C1 = tri((4, 10), 0.25, 'sujet'); cen1 = ((A1[0] + B1[0] + C1[0]) / 3, (A1[1] + B1[1] + C1[1]) / 3)
A2, B2, C2 = tri((32, 10), 0.5, 'autre'); cen2 = ((A2[0] + B2[0] + C2[0]) / 3, (A2[1] + B2[1] + C2[1]) / 3)
side(ax, A1, B1, cen1, '90', 'sujet'); side(ax, A1, C1, cen1, '120', 'sujet', 3.4); side(ax, B1, C1, cen1, '92,82', 'sujet', 4.2)
side(ax, A2, B2, cen2, '180', 'autre'); side(ax, A2, C2, cen2, '240', 'autre', 3.8); side(ax, B2, C2, cen2, '185,64', 'autre', 4.2)
text(ax, *inner(A2, cen2, 0.45), '50°', 'fixe', 's')
text(ax, *inner(B2, cen2, 0.4), '82,03°', 'fixe', 's')
text(ax, C2[0], C2[1] + 3.4, '47,97°', 'fixe', 's')
text(ax, 30, 63, 'mêmes angles, deux tailles', 'encre', 'm')
save(fig, '36-074')
