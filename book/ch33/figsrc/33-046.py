import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def arc(ax, cx, cy, R, a0, a1, role='fixe', lw=0.9, dash=False, n=60):
    line(ax, [P(cx, cy, R, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def dot(ax, x, y, role, r=1.1): ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))
def halves(ax, cx, cy, R, lw=2.0):
    arc(ax, cx, cy, R, 90, 270, 'fixe', 0.8); arc(ax, cx, cy, R, -90, 90, 'sujet', lw)
fig, ax = canvas(60); cy, R = 36, 11
for n, cx in enumerate((15, 44, 73)):
    halves(ax, cx, cy, R, 1.8); text(ax, cx, cy + R + 6, f'condition {n + 1}', 'sujet', 's')
for h in (-1, -0.5, 0, 0.5, 1):
    a = math.degrees(math.asin(h)); p = P(15, cy, R, a)
    line(ax, [(15, p[1]), (15 + R + 2, p[1])], 'varie', 0.9); dot(ax, *p, 'resultat', 0.9)
text(ax, 15 + R + 5.2, cy + R, '1', 'varie', 's'); text(ax, 15 + R + 5.6, cy - R, '−1', 'varie', 's')
line(ax, [(44 - R - 2, cy + R / 2), (44 + R + 2, cy + R / 2)], 'varie', 1.0)
dot(ax, *P(44, cy, R, 30), 'resultat'); dot(ax, *P(44, cy, R, 150), 'fixe')
p = P(73, cy, R, 30); poly(ax, [(73, cy), p, (p[0], cy)], 'resultat'); text(ax, 77, cy - 3.2, '30°', 'resultat', 's')
arc(ax, 73, cy, 5, 0, 30, 'resultat', 1.0)
for cx, a, b in [(15, 'toutes les', 'hauteurs'), (44, 'une seule', 'fois'), (73, 'angles de', 'triangle')]:
    text(ax, cx, 15, a, 'encre', 's'); text(ax, cx, 11.5, b, 'encre', 's')
save(fig, '33-046')
