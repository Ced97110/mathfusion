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

fig, ax = canvas(62)
cy = 32; h = 9; rd = 3.0
P = square(ax, 22, cy, h, ['sujet'] * 4, names='ABCD')
line(ax, [(22 - h - 5, cy + h + 5), (22 + h + 5, cy - h - 5)], 'fixe', dash=True)
for i in (0, 2): disc(ax, P[i][0], P[i][1], 4.3, 'varie', fill=False)
arr(ax, P[1], P[3], rd, 'varie', both=True)
Q = square(ax, 66, cy, h, ['sujet'] * 4, names='ABCD')
line(ax, [(66, cy + h + 5), (66, cy - h - 5)], 'fixe', dash=True)
arr(ax, Q[0], Q[1], rd, 'varie', both=True); arr(ax, Q[3], Q[2], rd, 'varie', both=True)
text(ax, 22, 54, 'axe diagonal', 'encre', 's'); text(ax, 66, 54, 'axe médian', 'encre', 's')
text(ax, 22, 12, '3 cycles', 'resultat', 'm'); text(ax, 66, 12, '2 cycles', 'resultat', 'm')
save(fig, '49-251')
