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

fig, ax = canvas(58)
rows = [(42, r'$r=(A\,B\,C\,D)$', [4], 1, 2, r'$2^1=2$'),
        (25, r'$r^2=(A\,C)(B\,D)$', [2, 2], 2, 4, r'$2^2=4$'),
        (8, 'identité', [1, 1, 1, 1], 4, 16, r'$2^4=16$')]
for y, lab, groups, c, val, fm in rows:
    text(ax, 2, y + 11, lab, 'encre', 's', ha='left')
    x = 2
    for k in groups:
        w = k * 4.4 + 1.2
        rect(ax, x, y + 1, w, 7, 'sujet')
        for j in range(k): disc(ax, x + 0.6 + 2.2 + 4.4 * j, y + 4.5, 1.7, 'fixe')
        x += w + 1.6
    rect(ax, 52, y + 2.5, val * 1.25, 4, 'resultat')
    text(ax, 52 + val * 1.25 + 2, y + 4.5, fm, 'resultat', 's', ha='left')
save(fig, '49-250')
