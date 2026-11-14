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

fig, ax = canvas(62); cy, R = 32, 15
text(ax, 22, 56, r'$\langle 4\rangle = \{0,\,4,\,8\}$', 'sujet', 'm', weight='bold')
text(ax, 66, 56, r'$\langle 5\rangle$ : les 12 heures', 'varie', 'm', weight='bold')
cx = 22
poly(ax, [pos(h, cx, cy, R) for h in (0, 4, 8)], 'sujet')
for h in range(12):
    p = pos(h, cx, cy, R)
    if h % 4 == 0: disc(ax, p[0], p[1], 2.9, 'sujet', str(h), 's')
    else: disc(ax, p[0], p[1], 1.6, 'fixe', None)
cx = 66
for h in range(12):
    edge_arrow(ax, pos(h, cx, cy, R), pos((h + 5) % 12, cx, cy, R), 2.2, 'varie', 0.0, 0.6)
for h in range(12):
    p = pos(h, cx, cy, R)
    if h == 0: disc(ax, p[0], p[1], 2.9, 'varie', '0', 's')
    else: disc(ax, p[0], p[1], 2.0, 'varie', None)
text(ax, 22, 8, '3 heures entre deux points', 'fixe', 's')
text(ax, 66, 8, 'un seul chemin fermé', 'varie', 's')
save(fig, '46-010')
