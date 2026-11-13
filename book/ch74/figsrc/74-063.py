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
xs = [32, 48, 64, 80]
rows = [('F', r'$C_1$', False, False, False), ('N', r'$C_2$', False, False, True), ('A', r'$D_1$', True, False, False), ('H', r'$D_2$', True, True, True)]
text(ax, 2, 28, 'miroir ?', 'encre', 's', ha='left'); text(ax, 2, 18, 'demi-tour ?', 'encre', 's', ha='left')
for x, (ch, name, vm, hm, half) in zip(xs, rows):
    glyph(ax, x - dict(F=2, N=2.5, A=2.5, H=2.5)[ch], 38, 1.0, ch, 'sujet', 1.8)
    if vm: line(ax, [(x, 36), (x, 47)], 'resultat', lw=0.9, dash=True)
    if hm: line(ax, [(x - 5.5, 41.5), (x + 5.5, 41.5)], 'resultat', lw=0.9, dash=True)
    text(ax, x, 60, name, 'sujet', 'l')
    text(ax, x, 28, '✓' if (vm) else '–', 'resultat' if vm else 'fixe', 'm')
    text(ax, x, 18, '✓' if half else '–', 'resultat' if half else 'fixe', 'm')
    if half: disc(ax, x, 41.5, 0.8, 'varie')
save(fig, '74-063')
