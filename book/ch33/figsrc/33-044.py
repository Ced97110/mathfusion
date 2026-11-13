import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def arc(ax, cx, cy, R, a0, a1, role='fixe', lw=0.9, dash=False, n=60):
    line(ax, [P(cx, cy, R, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def dot(ax, x, y, role, r=1.1): ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))
def halves(ax, cx, cy, R, lw=2.0):
    arc(ax, cx, cy, R, 90, 270, 'fixe', 0.8); arc(ax, cx, cy, R, -90, 90, 'sujet', lw)
fig, ax = canvas(66); cx, cy, R = 30, 32, 20; yl = cy - 0.5 * R
halves(ax, cx, cy, R); line(ax, [(cx - R - 9, yl), (cx + R + 9, yl)], 'varie', 1.0)
arc(ax, cx, cy, R + 4, -30, 0, 'resultat', 1.6); arc(ax, cx, cy, R + 7, 0, 330, 'limite', 1.0, True)
a = P(cx, cy, R, -30); d = P(cx, cy, R, 210); dot(ax, *a, 'resultat'); dot(ax, *d, 'limite')
text(ax, a[0] + 3, a[1] - 3.8, '−30°', 'resultat', 's'); text(ax, 21, yl - 3.5, '210°', 'limite', 's')
text(ax, *P(cx, cy, R + 12, 120), '330°', 'limite', 's')
text(ax, 72, yl, 'hauteur −0,5', 'varie', 's'); text(ax, 70, 12, 'arcsin(−0,5) = −π/6', 'resultat', 's')
save(fig, '33-044')
