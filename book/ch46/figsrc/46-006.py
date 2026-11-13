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

fig, ax = canvas(62)
text(ax, 22, 56, 'échange de 2 cartes', 'encre', 'm', weight='bold')
text(ax, 66, 56, 'rotation de 3 cartes', 'encre', 'm', weight='bold')
a, b, c = (12, 40), (32, 40), (22, 26)
disc(ax, a[0], a[1], 3.6, 'sujet', '1'); disc(ax, b[0], b[1], 3.6, 'sujet', '2'); disc(ax, c[0], c[1], 3.6, 'fixe', '3')
edge_arrow(ax, a, b, 3.8, 'varie', 0.35); edge_arrow(ax, b, a, 3.8, 'varie', 0.35)
loop(ax, c[0], c[1], 3.6, 'fixe', up=False)
P = [(66, 43), (78, 24), (54, 24)]
for i, p in enumerate(P):
    edge_arrow(ax, p, P[(i + 1) % 3], 3.8, 'varie', 0.0)
for i, p in enumerate(P):
    disc(ax, p[0], p[1], 3.6, 'sujet', str(i + 1))
text(ax, 22, 8, 'répété 2 fois : retour', 'resultat', 's')
text(ax, 66, 8, 'répété 3 fois : retour', 'resultat', 's')
save(fig, '46-006')
