import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def arc(ax, cx, cy, R, a0, a1, role='fixe', lw=0.9, dash=False, n=60):
    line(ax, [P(cx, cy, R, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def dot(ax, x, y, role, r=1.1): ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))
def halves(ax, cx, cy, R, lw=2.0):
    arc(ax, cx, cy, R, 90, 270, 'fixe', 0.8); arc(ax, cx, cy, R, -90, 90, 'sujet', lw)
fig, ax = canvas(64); cx, cy, R = 26, 32, 20
halves(ax, cx, cy, R)
for s in (1, -1): line(ax, [(cx - R - 3, cy + s * 0.5 * R), (cx + R + 3, cy + s * 0.5 * R)], 'varie', 1.0)
for a, role, s in [(30, 'resultat', '30°'), (150, 'fixe', '150°'), (-30, 'resultat', '−30°'), (210, 'fixe', '210°')]:
    x, y = P(cx, cy, R, a); dot(ax, x, y, role)
    text(ax, x + (4.5 if a in (30, -30) else -4.5), y + (3 if a in (30, 150) else -3), s, role, 's')
text(ax, 72, 56, 'moitié droite', 'sujet', 's')
text(ax, 72, 42, 'arcsin 0,5 = π/6', 'resultat', 's'); text(ax, 72, 38, '(π/6 = 30°)', 'fixe', 's')
text(ax, 70, 22, 'arcsin(−0,5) = −π/6', 'resultat', 's'); text(ax, 70, 18, '(−π/6 = −30°)', 'fixe', 's')
save(fig, '33-043')
