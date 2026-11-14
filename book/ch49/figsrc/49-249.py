import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle

def corners(cx, cy, h):
    return [(cx - h, cy + h), (cx + h, cy + h), (cx + h, cy - h), (cx - h, cy - h)]  # A B C D

def square(ax, cx, cy, h, roles, names=None, rd=3.0):
    P = corners(cx, cy, h)
    poly(ax, P, 'fixe', fill=False)
    for i, (p, ro) in enumerate(zip(P, roles)):
        disc(ax, p[0], p[1], rd, ro, label=(names[i] if names else None), size='s')
    return P

def arr(ax, p, q, rd=3.0, role='varie', curve=0.0, both=False, lw=1.0):
    dx, dy = q[0] - p[0], q[1] - p[1]; n = math.hypot(dx, dy); ux, uy = dx / n, dy / n
    s = (p[0] + ux * (rd + 0.7), p[1] + uy * (rd + 0.7)); e = (q[0] - ux * (rd + 0.7), q[1] - uy * (rd + 0.7))
    arrow(ax, s, e, role, lw=lw, curve=curve, both=both)

def rect(ax, x, y, w, h, role, fill=True, lw=0.6):
    ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc=FILL[role] if fill else 'none', lw=lw, zorder=2))

fig, ax = canvas(44)
cy = 27; h = 7; rd = 2.2
xs = [16, 44, 72]
P = square(ax, xs[0], cy, h, ['fixe'] * 4, rd=rd)
for p in P: disc(ax, p[0], p[1], 3.7, 'varie', fill=False)
P = square(ax, xs[1], cy, h, ['fixe'] * 4, rd=rd)
for i in range(4): arr(ax, P[i], P[(i + 1) % 4], rd, 'varie')
P = square(ax, xs[2], cy, h, ['fixe'] * 4, rd=rd)
arr(ax, P[0], P[2], rd, 'varie', both=True); arr(ax, P[1], P[3], rd, 'varie', both=True)
for x, nm, c in zip(xs, ['identité', 'quart de tour', 'demi-tour'], [4, 1, 2]):
    text(ax, x, 12, nm, 'encre', 's')
    text(ax, x, 5, r'$c(g)=%d$' % c, 'resultat', 'm')
save(fig, '49-249')
