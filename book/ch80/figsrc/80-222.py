import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def hasse(ax, cx, y0, dx, dy, roles=None, hot=None, bw=7.5, bh=5.0, size='m'):
    roles = roles or {}; hot = hot or {}
    pos = {1: (cx, y0), 2: (cx - dx, y0 + dy), 3: (cx, y0 + dy), 5: (cx + dx, y0 + dy),
           6: (cx - dx, y0 + 2 * dy), 10: (cx, y0 + 2 * dy), 15: (cx + dx, y0 + 2 * dy), 30: (cx, y0 + 3 * dy)}
    edges = [(1, 2), (1, 3), (1, 5), (2, 6), (3, 6), (2, 10), (5, 10), (3, 15), (5, 15), (6, 30), (10, 30), (15, 30)]
    for a, b in edges:
        (xa, ya), (xb, yb) = pos[a], pos[b]
        line(ax, [(xa, ya + bh / 2), (xb, yb - bh / 2)], hot.get((a, b), 'fixe'), lw=1.6 if (a, b) in hot else 0.8)
    for n, (x, y) in pos.items():
        box(ax, x - bw / 2, y - bh / 2, bw, bh, roles.get(n, 'fixe'), label=str(n), size=size)
    return pos

def seg(ax, p, q, rp=0.0, rq=0.0, role='fixe', lw=0.8):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    line(ax, [(p[0] + ux * rp, p[1] + uy * rp), (q[0] - ux * rq, q[1] - uy * rq)], role, lw=lw)

def steps(ax, y_top, items, h=11, gap=4, nums=True):
    x0 = 12 if nums else 4
    cx = (x0 + 86) / 2; y = y_top
    for i, (role, l1, l2) in enumerate(items):
        yb = y - h
        box(ax, x0, yb, 86 - x0, h, role, lw=1.6 if role == 'varie' else 0.8)
        if l2:
            text(ax, cx, yb + h * 0.7, l1, role, 's'); text(ax, cx, yb + h * 0.27, l2, 'encre', 's')
        else:
            text(ax, cx, yb + h / 2, l1, role, 's')
        if nums: disc(ax, 7, yb + h / 2, 3, role, label=str(i + 1), size='s')
        if i < len(items) - 1: arrow(ax, (cx, yb), (cx, yb - gap), 'fixe')
        y = yb - gap

GX = {2: 40, 3: 53, 5: 66}
def grow(ax, y, name, present, role):
    text(ax, 30, y + 3.5, name, 'encre', 's', ha='right')
    for p, x in GX.items():
        if p in present: box(ax, x - 5.5, y, 11, 7, role, label=str(p), size='s')
        else: box(ax, x - 5.5, y, 11, 7, 'fixe', fill=False, dash=True, lw=0.5)

fig, ax = canvas(60)
A, Bp, C = (9, 8), (59, 8), (34, 51.3)
mid = lambda p, q: ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
P = {'100': A, '010': Bp, '001': C, '110': mid(A, Bp), '011': mid(Bp, C), '101': mid(A, C)}
P['111'] = ((A[0] + Bp[0] + C[0]) / 3, (A[1] + Bp[1] + C[1]) / 3)
G = P['111']; rin = math.hypot(P['110'][0] - G[0], P['110'][1] - G[1])
ax.add_patch(Circle(G, rin, ec=COL['fixe'], fc='none', lw=0.8, zorder=1))
trip = [('100', '110', '010'), ('010', '011', '001'), ('001', '101', '100'),
        ('100', '111', '011'), ('010', '111', '101'), ('001', '111', '110')]
for t in trip:
    seg(ax, P[t[0]], P[t[1]], 4.2, 4.2); seg(ax, P[t[1]], P[t[2]], 4.2, 4.2)
for k, (x, y) in P.items(): disc(ax, x, y, 4.2, 'sujet', label=k, size='s')
text(ax, 76, 53, '7 points', 'sujet', 's')
text(ax, 76, 46, '+', 'encre', 'm')
box(ax, 66, 33, 20, 8, 'autre', dash=True, label='000', size='m')
text(ax, 76, 28, 'pas un point', 'autre', 's')
text(ax, 76, 21, '= 8 listes', 'resultat', 's')
save(fig, '80-222')
