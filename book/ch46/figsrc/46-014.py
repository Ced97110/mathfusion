import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

_disc = disc
def disc(ax, x, y, r, role='fixe', label=None, size='m', lw=0.8):
    _disc(ax, x, y, r, role, True, label, size, lw)
def pos(h, cx, cy, R):
    a = math.radians(90 - 30 * h)
    return (cx + R * math.cos(a), cy + R * math.sin(a))

def edge_arrow(ax, p, q, r, role='varie', curve=0.0, lw=1.0, both=False):
    dx, dy = q[0] - p[0], q[1] - p[1]; L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
    arrow(ax, (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r), role, lw=lw, curve=curve, both=both)

def arc(ax, c, R, h0, h1, role):
    n = 40
    pts = [pos(h0 + (h1 - h0) * i / n, c[0], c[1], R) for i in range(n + 1)]
    line(ax, pts[:-3], role, lw=1.0)
    arrow(ax, pts[-4], pts[-1], role, lw=1.0)

def loop(ax, x, y, r, role='fixe', up=True):
    s = 1 if up else -1
    cy = y + s * (r + 2.0); n = 30
    pts = []
    for i in range(n + 1):
        a = math.radians(-60 + 300 * i / n) if up else math.radians(60 - 300 * i / n)
        pts.append((x + 2.4 * math.cos(a), cy + 2.4 * math.sin(a)))
    line(ax, pts[:-3], role, lw=0.9)
    arrow(ax, pts[-4], pts[-1], role, lw=0.9)

def sq(cx, cy, s):
    return [(cx - s / 2, cy + s / 2), (cx + s / 2, cy + s / 2), (cx + s / 2, cy - s / 2), (cx - s / 2, cy - s / 2)]

fig, ax = canvas(60)
Q = sq(22, 32, 22); L = [1, 3, 5, 8]
for i in range(4):
    edge_arrow(ax, Q[i], Q[(i + 1) % 4], 3.7, 'sujet', 0.0, 1.1)
for i in range(4):
    disc(ax, Q[i][0], Q[i][1], 3.6, 'sujet', str(L[i]))
n2, n6 = (58, 44), (58, 22)
edge_arrow(ax, n2, n6, 3.7, 'autre', 0.35, 1.1); edge_arrow(ax, n6, n2, 3.7, 'autre', 0.35, 1.1)
disc(ax, 58, 44, 3.6, 'autre', '2'); disc(ax, 58, 22, 3.6, 'autre', '6')
for x, v in ((78, 4), (78, 7)):
    pass
disc(ax, 78, 22, 3.6, 'fixe', '4'); loop(ax, 78, 22, 3.6, 'fixe')
disc(ax, 78, 44, 3.6, 'fixe', '7'); loop(ax, 78, 44, 3.6, 'fixe')
save(fig, '46-014')
