import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pol(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role='varie', lw=0.9, n=30):
    line(ax, [pol(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw)
def sq(ax, p, d1, d2, s=2.2, role='fixe'):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)
fig, ax = canvas(62)
C = (34, 34); R = 22
P = [pol(C, R, 90 + 72 * i) for i in range(5)]
for tri in ((0, 1, 2), (0, 2, 3), (0, 3, 4)):
    poly(ax, [P[i] for i in tri], 'sujet')
poly(ax, P, 'fixe', fill=False, lw=1.6)
line(ax, [P[0], P[2]], 'sujet', lw=1.0); line(ax, [P[0], P[3]], 'sujet', lw=1.0)
for tri in ((0, 1, 2), (0, 2, 3), (0, 3, 4)):
    g = (sum(P[i][0] for i in tri) / 3, sum(P[i][1] for i in tri) / 3)
    text(ax, g[0], g[1], '180°', 'sujet', 's')
a1 = math.degrees(math.atan2(P[0][1] - P[1][1], P[0][0] - P[1][0])); a2 = math.degrees(math.atan2(P[2][1] - P[1][1], P[2][0] - P[1][0]))
arc(ax, P[1], 5, a2, a1 if a1 > a2 else a1 + 360, 'varie', lw=1.2)
text(ax, P[1][0] - 7, P[1][1] + 3, '108°', 'varie', 's')
text(ax, 72, 46, '3 × 180° = 540°', 'sujet', 's')
text(ax, 72, 36, '540° ÷ 5 = 108°', 'resultat', 's', weight='bold')
text(ax, 34, 6, '5 côtés, 5 angles égaux', 'fixe', 's')
save(fig, '26-130')
