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

fig, ax = canvas(40)
cy = 25
combos = [('sujet', 'sujet'), ('sujet', 'varie'), ('varie', 'sujet'), ('varie', 'varie')]
for k, (a, b) in enumerate(combos):
    cx = 12 + 21 * k
    P = square(ax, cx, cy, 6, [a, b, a, b], names='ABCD' if k == 0 else None, rd=2.4)
    arr(ax, P[0], P[2], 2.4, 'encre', both=True, lw=0.7)
    arr(ax, P[1], P[3], 2.4, 'encre', both=True, lw=0.7)
text(ax, 44, 38, r'$r^2$ échange les diagonales', 'varie', 'm')
brace(ax, 4, 84, 14, 'resultat', label=r'$2\times2=4$ colorations fixes')
save(fig, '49-241')
