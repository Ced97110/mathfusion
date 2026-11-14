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

fig, ax = canvas(72)
sizes = [1, 4, 4, 2, 4, 1]; sp, gap, x0 = 3.2, 1.6, 22
rows = [(56, r'$e$ : 16'), (48, r'$r$ : 2'), (40, r'$r^2$ : 4'), (32, r'$r^3$ : 2')]
fixed = {0: range(6), 1: (0, 5), 2: (0, 3, 5), 3: (0, 5)}
x = x0; xs = []
for g, n in enumerate(sizes):
    xs.append([x + sp * (i + 0.5) for i in range(n)])
    rect(ax, x, 27, sp * n, 34, 'fixe')
    text(ax, x + sp * n / 2, 22.5, '4', 'resultat', 's')
    x += sp * n + gap
for r, (y, lab) in enumerate(rows):
    text(ax, 2, y, lab, 'encre', 's', ha='left')
    for g in fixed[r]:
        for cx in xs[g]:
            disc(ax, cx, y, 1.2, 'resultat')
text(ax, 2, 64, 'ligne = rotation : points verts', 'encre', 's', ha='left')
text(ax, 44, 69, r'par ligne : $16+2+4+2=24$', 'resultat', 'm', weight='bold')
text(ax, 44, 15, 'colonne = coloration ; cadre : 4 points', 'fixe', 's')
text(ax, 44, 5, r'par cadre : $6\times4=24$', 'resultat', 'm', weight='bold')
save(fig, '49-243')
