import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, r, a0, a1, role, lw=1.0):
    n = max(8, int(abs(a1 - a0) / 4))
    pts = [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts[:-1], role, lw)
    arrow(ax, pts[-2], pts[-1], role, lw)
def polar(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def sq(ax, cx, cy, h, role):
    pts = [polar(cx, cy, h * math.sqrt(2), 45 + 90 * k) for k in range(4)]
    ax.add_patch(Polygon(pts, closed=True, ec=COL[role], fc=FILL[role], lw=0.9, zorder=2))

fig, ax = canvas(52)
text(ax, 44, 47, r'$C_4$ : 4 rotations, aucun miroir', 'sujet', 'l')
cy = 26
for i, ang in enumerate([0, 90, 180, 270]):
    cx = 11 + i * 22
    for k in range(4):
        a = ang + 90 * k
        P0 = (0, 0); P1 = (9, 0); P2 = (9, 4.5)
        rot = lambda p: (cx + p[0] * math.cos(math.radians(a)) - p[1] * math.sin(math.radians(a)), cy + p[0] * math.sin(math.radians(a)) + p[1] * math.cos(math.radians(a)))
        role = 'varie' if k == 0 else 'sujet'
        ax.add_patch(Polygon([rot(P0), rot(P1), rot(P2)], closed=True, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    disc(ax, cx, cy, 0.9, 'encre')
    text(ax, cx, 8, f'{ang}°', 'encre', 'm')
save(fig, '74-060')
