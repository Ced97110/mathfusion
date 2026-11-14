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

fig, ax = canvas(64); y = 34
box(ax, 2, 50, 40, 10, 'sujet', label='crochets : engendré par', size='s')
text(ax, 10, y, '⟨', 'sujet', 'xl', weight='bold'); text(ax, 17, y, '4', 'varie', 'xl', weight='bold'); text(ax, 24, y, '⟩', 'sujet', 'xl', weight='bold')
text(ax, 34, y, '=', 'encre', 'xl'); text(ax, 58, y, r'$\{0,\,4,\,8\}$', 'resultat', 'xl', weight='bold')
arrow(ax, (10, 49.5), (10, y + 5), 'sujet'); arrow(ax, (24, 49.5), (24, y + 5), 'sujet')
box(ax, 1, 8, 34, 11, 'varie', label='le geste : avancer de 4', size='s')
arrow(ax, (17, 19.5), (17, y - 5), 'varie')
box(ax, 40, 8, 47, 11, 'resultat', label='heures atteintes depuis 0', size='s')
arrow(ax, (58, 19.5), (58, y - 5), 'resultat')
save(fig, '46-011')
