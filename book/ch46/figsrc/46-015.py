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

fig, ax = canvas(92)
def titre(y, a, b, role):
    text(ax, 2, y + 4, a, role, 'm', ha='left', weight='bold'); text(ax, 2, y - 3, b, 'encre', 's', ha='left')
# row 1: whole shuffle
y = 76; titre(y, 'mélange entier', '4 boucles à la fois', 'fixe')
Q = sq(44, y, 11)
for i in range(4): edge_arrow(ax, Q[i], Q[(i + 1) % 4], 2.3, 'fixe', 0.0, 0.8)
for p in Q: disc(ax, p[0], p[1], 2.2, 'fixe', None)
a, b = (62, y + 5), (62, y - 5)
edge_arrow(ax, a, b, 2.3, 'fixe', 0.4, 0.8); edge_arrow(ax, b, a, 2.3, 'fixe', 0.4, 0.8)
disc(ax, a[0], a[1], 2.2, 'fixe', None); disc(ax, b[0], b[1], 2.2, 'fixe', None)
for x in (74, 83):
    disc(ax, x, y - 2, 2.2, 'fixe', None); loop(ax, x, y - 2, 2.2, 'fixe')
# row 2: path
y = 46; titre(y, 'trajet', "peut s'arrêter", 'autre')
X = [42, 58, 74]
for i in range(2): edge_arrow(ax, (X[i], y), (X[i + 1], y), 3.4, 'autre', 0.0, 1.1)
for i, x in enumerate(X): disc(ax, x, y, 3.4, 'autre', ['1', '3', '5'][i], 's')
line(ax, [(79.5, y - 5), (79.5, y + 5)], 'limite', lw=1.8)
# row 3: cycle
y = 16; titre(y, 'cycle', 'revient au départ', 'sujet')
Q = sq(60, y, 13); L = [1, 3, 5, 8]
for i in range(4): edge_arrow(ax, Q[i], Q[(i + 1) % 4], 3.6, 'sujet', 0.0, 1.1)
for i, p in enumerate(Q): disc(ax, p[0], p[1], 3.4, 'sujet', str(L[i]), 's')
save(fig, '46-015')
