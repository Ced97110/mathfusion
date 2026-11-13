import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def arc(ax, cx, cy, R, a0, a1, role='fixe', lw=0.9, dash=False, n=60):
    line(ax, [P(cx, cy, R, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def dot(ax, x, y, role, r=1.1): ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))
def halves(ax, cx, cy, R, lw=2.0):
    arc(ax, cx, cy, R, 90, 270, 'fixe', 0.8); arc(ax, cx, cy, R, -90, 90, 'sujet', lw)
fig, ax = canvas(50); O = (10, 18)
line(ax, [O, (40, 18)], 'fixe', 0.9); line(ax, [O, P(*O, 30, 30)], 'sujet', 1.6); arc(ax, *O, 12, 0, 30, 'sujet', 1.4)
text(ax, *P(*O, 17, 15), 'θ', 'sujet', 'l'); text(ax, 25, 6, 'θ : thêta, un angle', 'sujet', 's')
for y, a, s in [(38, 30, 'θ = 30°'), (26, -30, 'θ = −30°'), (14, 0, 'θ = 0°')]:
    line(ax, [(52, y), (66, y)], 'fixe', 0.9)
    line(ax, [(52, y), P(52, y, 14, a)], 'sujet', 1.4)
    if a: arc(ax, 52, y, 6, 0, a, 'sujet', 1.2)
    text(ax, 76, y, s, 'sujet', 's')
text(ax, 70, 47, 'entre −90° et 90°', 'fixe', 's')
save(fig, '33-037')
