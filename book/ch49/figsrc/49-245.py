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

fig, ax = canvas(52)
cy = 28
P = square(ax, 22, cy, 9, ['sujet'] * 4, names='ABCD')
for i in range(4): arr(ax, P[i], P[(i + 1) % 4], 3.0, 'varie')
Q = square(ax, 66, cy, 9, ['sujet', 'varie', 'sujet', 'varie'], names='ABCD')
arr(ax, Q[0], Q[2], 3.0, 'encre', both=True, lw=0.8); arr(ax, Q[1], Q[3], 3.0, 'encre', both=True, lw=0.8)
text(ax, 22, 46, r'$r$ : 1 cycle', 'varie', 's')
text(ax, 66, 46, r'$r^2$ : 2 cycles', 'varie', 's')
brace(ax, 6, 82, 15, 'resultat', label='une couleur par cycle')
save(fig, '49-245')
