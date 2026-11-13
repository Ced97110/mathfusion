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

fig, ax = canvas(62); cx, cy, R = 20, 33, 14
text(ax, 20, 56, 'horloge : geste +4', 'encre', 's', weight='bold')
text(ax, 66, 56, r'cartes : mélange $\sigma$', 'encre', 's', weight='bold')
for h in range(12):
    if h % 4:
        p = pos(h, cx, cy, R); disc(ax, p[0], p[1], 1.4, 'fixe', None)
for h in (0, 4, 8):
    edge_arrow(ax, pos(h, cx, cy, R), pos((h + 4) % 12, cx, cy, R), 3.2, 'varie')
for h in (0, 4, 8):
    p = pos(h, cx, cy, R); disc(ax, p[0], p[1], 3.0, 'sujet', str(h), 's')
Q = sq(66, 33, 18); L = [1, 3, 5, 8]
for i in range(4):
    edge_arrow(ax, Q[i], Q[(i + 1) % 4], 3.5, 'varie')
for i in range(4):
    disc(ax, Q[i][0], Q[i][1], 3.4, 'sujet', str(L[i]), 's')
text(ax, 44, 8, 'on répète un seul geste', 'varie', 'm')
save(fig, '46-008')
