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

fig, ax = canvas(66)
rows = [[1, 2, 3], [2, 1, 3], [3, 1, 2]]; Y = [56, 34, 12]; X = [12, 24, 36]
for r, vals in enumerate(rows):
    for k, v in enumerate(vals):
        box(ax, X[k] - 4.5, Y[r], 9, 9, 'resultat' if r == 2 else 'sujet', label=str(v))
swaps = [(0, 1), (0, 2)]
for r, (p, q) in enumerate(swaps):
    for k in range(3):
        t = q if k == p else p if k == q else k
        arrow(ax, (X[k], Y[r]), (X[t], Y[r + 1] + 9.5), 'varie' if t != k else 'fixe', lw=0.9)
text(ax, 66, Y[0] + 4.5, 'départ', 'encre', 's')
text(ax, 66, Y[1] + 4.5, 'échange places 1 et 2', 'varie', 's')
text(ax, 66, Y[2] + 4.5, 'puis échange places 1 et 3', 'varie', 's')
text(ax, 44, 3, 'résultat : 1→2, 2→3, 3→1', 'resultat', 's')
save(fig, '46-007')
