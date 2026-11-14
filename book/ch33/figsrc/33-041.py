import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def arc(ax, cx, cy, R, a0, a1, role='fixe', lw=0.9, dash=False, n=60):
    line(ax, [P(cx, cy, R, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def dot(ax, x, y, role, r=1.1): ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))
def halves(ax, cx, cy, R, lw=2.0):
    arc(ax, cx, cy, R, 90, 270, 'fixe', 0.8); arc(ax, cx, cy, R, -90, 90, 'sujet', lw)
fig, ax = canvas(46); O = (8, 8); R1 = 20; R2 = 40
line(ax, [O, (O[0] + R2 + 2, 8)], 'fixe', 0.9); line(ax, [O, P(*O, R2 + 2, 30)], 'fixe', 0.9)
arc(ax, *O, R1, 0, 30, 'sujet', 2.4); arc(ax, *O, R2, 0, 30, 'autre', 2.4)
text(ax, 52, 24, 'rayon 2 : arc ≈ 1,05', 'autre', 's', ha='left'); arrow(ax, (51.5, 22), (47, 19), 'autre', lw=0.7)
text(ax, 52, 11, 'rayon 1 : arc ≈ 0,52', 'sujet', 's', ha='left'); arrow(ax, (51.5, 11), (29, 12.8), 'sujet', lw=0.7)
text(ax, 30, 3.5, 'même angle : 30°', 'fixe', 's'); text(ax, 44, 41, 'arc = angle si rayon 1', 'resultat', 'm')
save(fig, '33-041')
