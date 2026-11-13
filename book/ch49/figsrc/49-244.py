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

fig, ax = canvas(60)
rows = [(38, r'$e$'), (30, r'$r$'), (22, r'$r^2$'), (14, r'$r^3$')]
for y, lab in rows: text(ax, 4, y, lab, 'encre', 's', ha='left')
rect(ax, 16, 9, 12, 33, 'fixe'); rect(ax, 38, 9, 36, 33, 'fixe')
square(ax, 22, 48, 2.2, ['sujet'] * 4, rd=1.0)
for y, _ in rows: disc(ax, 22, y, 1.6, 'resultat')
for k in range(4):
    cx = 43 + 9 * k
    roles = ['sujet'] * 4; roles[k] = 'varie'
    square(ax, cx, 48, 2.2, roles, rd=0.9)
    disc(ax, cx, 38, 1.6, 'resultat')
text(ax, 22, 5, r'$1\times4=4$', 'resultat', 's')
text(ax, 56, 5, r'$4\times1=4$', 'resultat', 's')
text(ax, 50, 57, r'chaque cadre : $|G|=4$ points', 'resultat', 's')
save(fig, '49-244')
