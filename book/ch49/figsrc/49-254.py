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
sizes = [1, 4, 4, 2, 4, 1]; sp, gap, x0 = 3.6, 1.8, 11
def row(y, role):
    x = x0
    for n in sizes:
        rect(ax, x, y - 3.5, sp * n, 7, role)
        for i in range(n): disc(ax, x + sp * (i + 0.5), y, 1.2, 'sujet')
        x += sp * n + gap
row(43, 'fixe'); row(15, 'resultat')
text(ax, 44, 52, '4 rotations : 6 orbites', 'encre', 's')
arrow(ax, (44, 36), (44, 29), 'varie'); text(ax, 48, 32.5, '+ réflexions', 'varie', 's', ha='left')
text(ax, 44, 24, '8 symétries : 6 orbites', 'encre', 's')
text(ax, 44, 5, 'aucune orbite réunie', 'resultat', 'm')
save(fig, '49-254')
