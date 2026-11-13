import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def arc(ax, cx, cy, R, a0, a1, role='fixe', lw=0.9, dash=False, n=60):
    line(ax, [P(cx, cy, R, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def dot(ax, x, y, role, r=1.1): ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))
def halves(ax, cx, cy, R, lw=2.0):
    arc(ax, cx, cy, R, 90, 270, 'fixe', 0.8); arc(ax, cx, cy, R, -90, 90, 'sujet', lw)
fig, ax = canvas(56); O = (8, 6); R = 40
arc(ax, *O, R, 0, 90, 'fixe', 0.6, True)
line(ax, [O, (O[0] + R, 6)], 'fixe', 0.9); line(ax, [O, P(*O, R, 30)], 'fixe', 0.9)
arc(ax, *O, R, 0, 30, 'sujet', 2.4); arc(ax, *O, 10, 0, 30, 'fixe', 0.9)
text(ax, *P(*O, 15, 15), '30°', 'fixe', 's'); text(ax, 28, 2.3, 'rayon 1', 'fixe', 's')
text(ax, 51, 16, 'arc ≈ 0,52', 'sujet', 'm', ha='left')
text(ax, 62, 48, 'angle 30° = π/6 ≈ 0,52', 'fixe', 's'); text(ax, 62, 42, 'angle et arc : même nombre', 'resultat', 's')
save(fig, '33-040')
