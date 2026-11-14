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

fig, ax = canvas(58); cy, R = 33, 8.5
for k, (s, div, role) in enumerate([(4, 4, 'limite'), (5, 1, 'resultat'), (6, 6, 'limite'), (7, 1, 'resultat')]):
    cx = 11 + 22 * k
    vis = sorted({(i * s) % 12 for i in range(12)})
    order = [(i * s) % 12 for i in range(len(vis))] + [0]
    line(ax, [pos(h, cx, cy, R) for h in order], role, lw=0.6)
    for h in range(12):
        p = pos(h, cx, cy, R)
        disc(ax, p[0], p[1], 1.5, role if h in vis else 'fixe', None)
    text(ax, cx, 51, f'pas {s}', 'encre', 'm', weight='bold')
    text(ax, cx, 20, f'diviseur {div}', role, 's')
    text(ax, cx, 12, f'{len(vis)} heures', role, 's')
save(fig, '46-004')
