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
cy = 30; h = 10
Q = square(ax, 22, cy, h, ['sujet', 'sujet', 'varie', 'varie'], names='ABCD')
line(ax, [(22, cy + h + 5), (22, cy - h - 5)], 'fixe', dash=True)
arr(ax, Q[0], Q[1], 3.0, 'encre', both=True); arr(ax, Q[3], Q[2], 3.0, 'encre', both=True)
text(ax, 22, 51, 'axe médian', 'encre', 's')
for y, lab in ((46, r'paire $A\,B$ : 2 choix'), (28, r'paire $C\,D$ : 2 choix')):
    text(ax, 48, y, lab, 'encre', 's', ha='left')
    rect(ax, 48, y - 9, 12, 7, 'fixe')
    disc(ax, 52.2, y - 5.5, 1.8, 'sujet'); disc(ax, 56.4, y - 5.5, 1.8, 'varie')
text(ax, 54, 32.5, r'$\times$', 'encre', 's')
text(ax, 66, 9, r'$2\times2=4$ colorations', 'resultat', 's')
save(fig, '49-252')
