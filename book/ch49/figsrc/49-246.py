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

fig, ax = canvas(56)
cy = 28
L = corners(22, cy, 9); R = corners(66, cy, 9)
poly(ax, L, 'fixe', fill=False); poly(ax, R, 'fixe', fill=False)
disc(ax, L[0][0], L[0][1], 3, 'sujet', label=r'$u$', size='s'); disc(ax, L[1][0], L[1][1], 3, 'varie', label=r'$v$', size='s')
disc(ax, L[2][0], L[2][1], 3, 'sujet'); disc(ax, L[3][0], L[3][1], 3, 'sujet')
arr(ax, L[0], L[1], 3.0, 'varie', lw=1.6)
for i, p in enumerate(R):
    disc(ax, p[0], p[1], 3, 'sujet', label=[r'$u$', r'$v$', None, None][i], size='s')
for i in range(4): arr(ax, R[i], R[(i + 1) % 4], 3.0, 'varie', lw=1.6 if i == 0 else 0.9)
text(ax, 22, 46, r'si $v$ est orange', 'limite', 's'); text(ax, 66, 46, r'si $v$ est bleu', 'resultat', 's')
text(ax, 22, 12, 'la coloration change', 'limite', 's')
text(ax, 66, 12, 'rien ne change', 'resultat', 's'); text(ax, 66, 6, 'on suit le cycle', 'varie', 's')
save(fig, '49-246')
