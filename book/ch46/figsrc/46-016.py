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

fig, ax = canvas(78)
# i parcourt 1..8
text(ax, 44, 73, r'$i$ prend tour à tour 1, 2, ..., 8', 'varie', 'm')
xs = [10 + 9.7 * k for k in range(8)]
for k, x in enumerate(xs):
    disc(ax, x, 64, 3.6, 'varie', str(k + 1), 's')
for k in range(7):
    arrow(ax, (xs[k] + 3.8, 64), (xs[k + 1] - 3.8, 64), 'varie', lw=0.7)
def row(y, a, b, eq):
    disc(ax, 10, y, 4.6, 'varie', a, 'm')
    arrow(ax, (16, y), (41, y), 'varie', lw=1.2)
    text(ax, 28.5, y + 4.5, r'$\sigma$', 'varie', 'm')
    box(ax, 42, y - 5, 18, 10, 'resultat', label=b, size='m')
    if eq: text(ax, 74, y, eq, 'encre', 'm')
row(46, r'$i$', r'$\sigma(i)$', None)
text(ax, 44, 55, 'pour chaque $i$ : un $\\sigma(i)$', 'fixe', 's')
row(27, '1', '3', r'$\sigma(1) = 3$')
row(8, '3', '5', r'$\sigma(3) = 5$')
save(fig, '46-016')
