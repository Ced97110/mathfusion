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
text(ax, 44, 51, r'$|\mathrm{Fix}\ g| = m^{c(g)}$ : un choix de $m$ par cycle', 'sujet', 's')
pal = ['sujet', 'varie', 'autre']
rows = [(36, r'$r$ : 1 cycle, $m=2$', 2, 1, r'$2^1=2$'), (22, r'$r$ : 1 cycle, $m=3$', 3, 1, r'$3^1=3$'), (8, r'$r^2$ : 2 cycles, $m=3$', 3, 2, r'$3^2=9$')]
for y, lab, m, c, res in rows:
    text(ax, 2, y + 3.5, lab, 'encre', 's', ha='left')
    x = 38; w = m * 4.2 + 1.6
    for j in range(c):
        rect(ax, x, y, w, 7, 'fixe')
        for k in range(m): disc(ax, x + 1.6 + 4.2 * k + 0.5, y + 3.5, 1.6, pal[k])
        x += w
        if j < c - 1:
            text(ax, x + 2.5, y + 3.5, r'$\times$', 'encre', 's'); x += 5
    text(ax, x + 3, y + 3.5, res, 'resultat', 'm', ha='left')
save(fig, '49-247')
