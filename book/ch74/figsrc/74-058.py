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

fig, ax = canvas(56)
cy = 32; h = 5.5; rr = 8
for cx, lab in [(16, r'$90°+90°=180°$'), (44, 'inverse de 90° : 270°'), (72, 'identité : 0°')]:
    sq(ax, cx, cy, h, 'sujet')
    text(ax, cx, 12, lab, 'encre', 's')
cx = 16
disc(ax, *polar(cx, cy, rr, 45), 1.1, 'fixe'); disc(ax, *polar(cx, cy, rr, 135), 1.1, 'fixe'); disc(ax, *polar(cx, cy, rr, 225), 1.1, 'resultat')
arc(ax, cx, cy, 12, 48, 130, 'varie'); arc(ax, cx, cy, 12, 138, 220, 'varie')
cx = 44
disc(ax, *polar(cx, cy, rr, 45), 1.1, 'fixe'); disc(ax, *polar(cx, cy, rr, 315), 1.1, 'resultat')
arc(ax, cx, cy, 12, 48, 308, 'varie')
cx = 72
disc(ax, *polar(cx, cy, rr, 45), 1.1, 'resultat')
text(ax, 44, 51, r'chaque composée, inverse, identité : $X$ reste $X$', 'resultat', 's')
text(ax, 44, 5, 'départ : gris ; arrivée : vert', 'fixe', 's')
save(fig, '74-058')
