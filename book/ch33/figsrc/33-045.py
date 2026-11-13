import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def arc(ax, cx, cy, R, a0, a1, role='fixe', lw=0.9, dash=False, n=60):
    line(ax, [P(cx, cy, R, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def dot(ax, x, y, role, r=1.1): ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))
def halves(ax, cx, cy, R, lw=2.0):
    arc(ax, cx, cy, R, 90, 270, 'fixe', 0.8); arc(ax, cx, cy, R, -90, 90, 'sujet', lw)
fig, ax = canvas(70); cx, cy, R = 30, 34, 26; yh = cy + 0.5 * R
halves(ax, cx, cy, R); line(ax, [(cx - R - 3, yh), (cx + R + 3, yh)], 'varie', 1.0)
line(ax, [(cx, cy), (cx + R, cy)], 'fixe', 0.7, True)
p = P(cx, cy, R, 30); q = P(cx, cy, R, 150); line(ax, [(cx, cy), p], 'resultat', 1.2)
dot(ax, *p, 'resultat', 1.2); dot(ax, *q, 'fixe', 1.2); dot(ax, cx, cy, 'encre', 0.9)
arc(ax, cx, cy, 10, 0, 30, 'resultat', 1.2); text(ax, *P(cx, cy, 15, 15), 'θ', 'resultat', 's')
text(ax, cx - 3, cy - 3.2, 'O', 'encre', 's'); text(ax, p[0] + 3.5, yh + 3.2, 'P', 'resultat', 'm'); text(ax, q[0] - 3, yh + 3.2, 'Q', 'fixe', 'm')
text(ax, 73, yh, 'hauteur 0,5', 'varie', 's'); text(ax, 72, 58, 'moitié droite', 'sujet', 's')
text(ax, 72, 22, 'θ = 30°', 'resultat', 's'); text(ax, 70, 10, 'Q : moitié gauche, écarté', 'fixe', 's')
save(fig, '33-045')
