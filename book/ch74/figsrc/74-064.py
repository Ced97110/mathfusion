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

fig, ax = canvas(56)
cy = 32
data = [(3, 'triangle', r'$D_3$'), (4, 'carré', r'$D_4$'), (5, 'étoile de mer', r'$D_5$'), (6, 'flocon', r'$D_6$')]
for i, (n, nom, d) in enumerate(data):
    cx = 11 + i * 22
    if n == 3: tips = ngon(ax, cx, cy, 9, 3, 'sujet')
    elif n == 4: tips = ngon(ax, cx, cy, 9, 4, 'sujet', 45)
    elif n == 5:
        pts = [polar(cx, cy, 10 if k % 2 == 0 else 4.2, 90 + 36 * k) for k in range(10)]
        ax.add_patch(Polygon(pts, closed=True, ec=COL['sujet'], fc=FILL['sujet'], lw=0.9, zorder=2))
        tips = pts[::2]
    else:
        tips = [polar(cx, cy, 10, 90 + 60 * k) for k in range(6)]
        for t in tips:
            line(ax, [(cx, cy), t], 'sujet', lw=1.2)
        for k in range(6):
            a = 90 + 60 * k
            for f in (0.55,):
                b = polar(cx, cy, 10 * f, a)
                line(ax, [b, polar(*b, 3, a + 50)], 'sujet', lw=1.0); line(ax, [b, polar(*b, 3, a - 50)], 'sujet', lw=1.0)
    for t in tips:
        disc(ax, t[0], t[1], 1.0, 'varie')
    text(ax, cx, 17, nom, 'encre', 's'); text(ax, cx, 10, d, 'sujet', 'l')
text(ax, 44, 50, r'$n$ pointes orange : groupe $D_n$', 'varie', 's')
save(fig, '74-064')
