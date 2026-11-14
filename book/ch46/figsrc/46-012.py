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

fig, ax = canvas(62); cy, R = 30, 12
text(ax, 20, 50, r'$\langle 5\rangle$', 'sujet', 'xl', weight='bold')
text(ax, 68, 50, r'$\mathbb{Z}/12\mathbb{Z}$', 'autre', 'xl', weight='bold')
text(ax, 44, cy, '=', 'resultat', 'xl', weight='bold')
for h in range(12):
    p = pos(h, 20, cy, R); disc(ax, p[0], p[1], 2.2, 'sujet', None)
    p = pos(h, 68, cy, R); disc(ax, p[0], p[1], 2.2, 'autre', None)
text(ax, 20, 11, '0, 5, 10, 3, 8, 1,', 'sujet', 's')
text(ax, 20, 5, '6, 11, 4, 9, 2, 7', 'sujet', 's')
text(ax, 68, 8, 'les 12 heures', 'autre', 's')
save(fig, '46-012')
