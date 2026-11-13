import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import itertools as it
from matplotlib.patches import Polygon as Pg
fig, ax = canvas(98)
N = 6.0
corners = list(it.product([0, N], repeat=3))
PLANES = [((1, 1, 1, 9), 'sujet', r'$x + y + z = 9$'), ((2, 1, 0, 8), 'varie', r'$2x + y = 8$'), ((1, 0, 2, 11), 'autre', r'$x + 2z = 11$')]

def plane_pts(a, b, c, d):
    f = lambda p: a * p[0] + b * p[1] + c * p[2] - d
    pts = []
    for p, q in it.combinations(corners, 2):
        if sum(p[i] != q[i] for i in range(3)) != 1: continue
        fp, fq = f(p), f(q)
        if fp * fq < 0:
            t = fp / (fp - fq); pts.append(tuple(p[i] + t * (q[i] - p[i]) for i in range(3)))
        elif fp == 0: pts.append(p)
        elif fq == 0: pts.append(q)
    return list(dict.fromkeys(tuple(round(v, 6) for v in p) for p in pts))

def draw_plane(spec, role, org, u, alpha):
    P = lambda p: iso(p[0], p[1], p[2], org, u)
    pp = [P(p) for p in plane_pts(*spec)]
    cx = sum(q[0] for q in pp) / len(pp); cy = sum(q[1] for q in pp) / len(pp)
    pp.sort(key=lambda q: math.atan2(q[1] - cy, q[0] - cx))
    ax.add_patch(Pg(pp, closed=True, ec=COL[role], fc=FILL[role], alpha=alpha, lw=0.9, zorder=2))

def cube_frame(org, u):
    P = lambda p: iso(p[0], p[1], p[2], org, u)
    for p, q in it.combinations(corners, 2):
        if sum(p[i] != q[i] for i in range(3)) == 1: line(ax, [P(p), P(q)], 'fixe', lw=0.4)

# top row: one plane per panel, equation under it
u1 = 2.5
for i, (spec, role, eq) in enumerate(PLANES):
    org = (15 + i * 29, 62)
    cube_frame(org, u1); draw_plane(spec, role, org, u1, 0.8)
    text(ax, org[0], 58, eq, role, 's')
# bottom: the three planes together, common point
u2 = 3.6; org = (24, 8)
cube_frame(org, u2)
for spec, role, eq in PLANES: draw_plane(spec, role, org, u2, 0.5)
pt = iso(3, 2, 4, org, u2)
disc(ax, pt[0], pt[1], 1.3, 'resultat')
text(ax, 66, 30, 'point commun', 'resultat', 's')
text(ax, 66, 24, r'$(3\ ;\ 2\ ;\ 4)$', 'resultat', 's')
arrow(ax, (50, 28), (pt[0] + 1.6, pt[1] + 0.3), 'resultat')
save(fig, '24-082')
