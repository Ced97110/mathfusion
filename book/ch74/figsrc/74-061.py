import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, r, a0, a1, role, lw=1.0):
    n = max(8, int(abs(a1 - a0) / 4))
    pts = [polar(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, pts[:-1], role, lw)
    arrow(ax, pts[-2], pts[-1], role, lw)
def polar(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def ngon(ax, cx, cy, r, n, role, a0=90):
    pts = [polar(cx, cy, r, a0 + 360 * k / n) for k in range(n)]
    ax.add_patch(Polygon(pts, closed=True, ec=COL[role], fc=FILL[role], lw=0.9, zorder=2))
    return pts
def glyph(ax, ox, oy, s, ch, role, lw=1.6):
    G = dict(F=[[(0, 0), (0, 7), (4, 7)], [(0, 3.6), (3, 3.6)]],
             N=[[(0, 0), (0, 7), (5, 0), (5, 7)]],
             A=[[(0, 0), (2.5, 7), (5, 0)], [(1, 2.8), (4, 2.8)]],
             H=[[(0, 0), (0, 7)], [(5, 0), (5, 7)], [(0, 3.6), (5, 3.6)]])
    for sg in G[ch]:
        line(ax, [(ox + s * x, oy + s * y) for x, y in sg], role, lw)

fig, ax = canvas(66)
cy = 38; R = 12
for cx in (22, 66):
    ngon(ax, cx, cy, R, 3, 'sujet')
cx = 22
for k in range(3):
    arc(ax, cx, cy, 16, 100 + 120 * k, 200 + 120 * k, 'varie')
text(ax, cx, 56, '3 rotations', 'varie', 'm'); text(ax, cx, 14, r'0°, 120°, 240°', 'varie', 's')
cx = 66
for k in range(3):
    a = 90 + 120 * k
    line(ax, [polar(cx, cy, R * 1.4, a), polar(cx, cy, -R * 0.7, a)], 'resultat', lw=1.1)
text(ax, cx, 56, '3 réflexions', 'resultat', 'm'); text(ax, cx, 14, 'axes par le centre', 'resultat', 's')
text(ax, 44, 5, r'$3+3=6=2n$', 'sujet', 'l')
save(fig, '74-061')
