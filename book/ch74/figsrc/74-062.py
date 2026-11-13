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

fig, ax = canvas(98)
box(ax, 2, 50, 84, 46, 'resultat', fill=False)
text(ax, 44, 91, r'groupe fini : $C_n$ ou $D_n$', 'resultat', 'm')
cx, cy = 22, 71
for k in range(3):
    a = 90 + 120 * k
    ax.add_patch(Polygon([(cx, cy), polar(cx, cy, 10, a), polar(cx, cy, 5.5, a + 40)], closed=True, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
text(ax, cx, 55, r'$C_n$ : rotations', 'sujet', 's')
cx = 66
ngon(ax, cx, cy, 10, 3, 'autre')
line(ax, [(cx, cy + 14), (cx, cy - 8)], 'resultat', lw=1.1)
text(ax, cx, 55, r'$D_n$ : avec miroirs', 'autre', 's')
box(ax, 2, 4, 84, 40, 'limite', fill=False)
text(ax, 44, 39, 'groupe infini : aucun des deux', 'limite', 'm')
for i in range(5):
    glyph(ax, 8 + i * 15, 14, 1.0, 'F', 'limite', 1.4)
text(ax, 80, 25, '…', 'limite', 'l'); text(ax, 5, 25, '…', 'limite', 'l', ha='left')
arrow(ax, (10, 10), (60, 10), 'varie', lw=0.9, curve=0)
text(ax, 72, 10, 'glissements', 'varie', 's')
save(fig, '74-062')
