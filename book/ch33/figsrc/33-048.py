import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def arc(ax, cx, cy, R, a0, a1, role='fixe', lw=0.9, dash=False, n=60):
    line(ax, [P(cx, cy, R, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def dot(ax, x, y, role, r=1.1): ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))
def halves(ax, cx, cy, R, lw=2.0):
    arc(ax, cx, cy, R, 90, 270, 'fixe', 0.8); arc(ax, cx, cy, R, -90, 90, 'sujet', lw)
fig, ax = canvas(58); cy, R = 38, 15; yh = cy + R / 2
for cx in (22, 66): line(ax, [(cx - R - 3, yh), (cx + R + 3, yh)], 'varie', 1.0)
arc(ax, 22, cy, R, 0, 360, 'sujet', 2.0)
halves(ax, 66, cy, R)
for cx, ra, rb in [(22, 'varie', 'varie'), (66, 'resultat', 'fixe')]:
    p = P(cx, cy, R, 30); q = P(cx, cy, R, 150); dot(ax, *p, ra); dot(ax, *q, rb)
    text(ax, p[0] + 4.5, yh + 3, '30°', ra, 's'); text(ax, q[0] - 4.5, yh + 3, '150°', rb, 's')
text(ax, 22, 14, 'deux moitiés :', 'sujet', 's'); text(ax, 22, 10, 'deux angles', 'varie', 's')
text(ax, 66, 14, 'moitié droite :', 'sujet', 's'); text(ax, 66, 10, 'un seul angle', 'resultat', 's')
save(fig, '33-048')
