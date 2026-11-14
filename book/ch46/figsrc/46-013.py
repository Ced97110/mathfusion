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

fig, ax = canvas(68)
text(ax, 44, 63, "geste +4 : ordre 3", 'sujet', 'm', weight='bold')
for i, v in enumerate(['4', '8', '0']):
    box(ax, 8 + 12 * i, 47, 10, 8, 'resultat' if v == '0' else 'varie', label=v)
brace(ax, 8, 42, 46, 'sujet', '3 pas')
text(ax, 44, 33, "geste +5 : ordre 12", 'sujet', 'm', weight='bold')
for i in range(12):
    lab = '5' if i == 0 else '0' if i == 11 else None
    box(ax, 4 + 6.9 * i, 17, 6.4, 8, 'resultat' if i == 11 else 'varie', label=lab, r=0.5, size='s')
brace(ax, 4, 4 + 6.9 * 11 + 6.4, 16, 'sujet', '12 pas')
save(fig, '46-013')
