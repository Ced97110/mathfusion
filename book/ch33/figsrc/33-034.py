import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def arc(ax, cx, cy, R, a0, a1, role='fixe', lw=0.9, dash=False, n=60):
    line(ax, [P(cx, cy, R, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def dot(ax, x, y, role, r=1.1): ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))
def halves(ax, cx, cy, R, lw=2.0):
    arc(ax, cx, cy, R, 90, 270, 'fixe', 0.8); arc(ax, cx, cy, R, -90, 90, 'sujet', lw)
fig, ax = canvas(62)
text(ax, 27, 50, 'sin θ = 0,5', 'sujet', 's'); text(ax, 50, 50, '−90° ≤ θ ≤ 90°', 'sujet', 's'); text(ax, 75, 50, 'conclusion', 'fixe', 's')
rows = [(30, '30°', 'sujet', 'vrai', 'vrai', 'resultat', 'resultat', 'θ = arcsin 0,5'),
        (10, '150°', 'autre', 'vrai', 'faux', 'resultat', 'limite', 'pas l’arcsinus')]
for y, a, ra, c1, c2, r1, r2, concl in rows:
    box(ax, 2, y, 14, 12, ra, label=a)
    box(ax, 17, y, 20, 12, r1, label=c1); box(ax, 40, y, 20, 12, r2, label=c2)
    arrow(ax, (37.5, y + 6), (39.5, y + 6), 'fixe', lw=0.6); arrow(ax, (60.5, y + 6), (63.5, y + 6), 'fixe')
    box(ax, 64, y, 22, 12, r2, label=concl, size='s')
save(fig, '33-034')
