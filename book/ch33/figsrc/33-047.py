import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def arc(ax, cx, cy, R, a0, a1, role='fixe', lw=0.9, dash=False, n=60):
    line(ax, [P(cx, cy, R, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def dot(ax, x, y, role, r=1.1): ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))
def halves(ax, cx, cy, R, lw=2.0):
    arc(ax, cx, cy, R, 90, 270, 'fixe', 0.8); arc(ax, cx, cy, R, -90, 90, 'sujet', lw)
fig, ax = canvas(60); cy, R = 36, 14
cxa, cxb = 20, 56
halves(ax, cxa, cy, R); line(ax, [(cxa + R + 4, cy - R), (cxa + R + 4, cy + R)], 'resultat', 2.6)
text(ax, cxa + R + 4, cy + R + 3, '1', 'resultat', 's'); text(ax, cxa + R + 4, cy - R - 3, '−1', 'resultat', 's')
arc(ax, cxb, cy, R, 90, 270, 'fixe', 0.8); arc(ax, cxb, cy, R, -90, 90, 'fixe', 0.8); arc(ax, cxb, cy, R, 0, 90, 'sujet', 2.0)
line(ax, [(cxb + R + 4, cy), (cxb + R + 4, cy + R)], 'resultat', 2.6)
text(ax, cxb + R + 4, cy + R + 3, '1', 'resultat', 's'); text(ax, cxb + R + 4, cy - 3, '0', 'resultat', 's')
line(ax, [(cxb - R - 2, cy - R / 2), (cxb + R + 2, cy - R / 2)], 'limite', 1.0, True); text(ax, 82, cy - R / 2, '−0,5', 'limite', 's')
text(ax, cxa, 20, 'moitié droite', 'sujet', 's'); text(ax, cxa, 15, 'de −1 à 1 : toutes', 'resultat', 's')
text(ax, 60, 20, 'seulement 0° à 90°', 'sujet', 's'); text(ax, 60, 15, '−0,5 : aucun angle', 'limite', 's')
save(fig, '33-047')
