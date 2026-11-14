import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
pi = math.pi
def pt(c, r, a): return (c[0] + r * math.cos(a), c[1] + r * math.sin(a))
def arc(ax, c, r, a0, a1, role='fixe', lw=0.9, dash=False, head=False, n=60):
    line(ax, [pt(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
    if head:
        s = 1 if a1 > a0 else -1
        arrow(ax, pt(c, r, a1 - s * 0.12), pt(c, r, a1), role, lw)
def sq(ax, corner, d1, d2, s=2.2, role='fixe'):
    p1 = (corner[0] + d1[0] * s, corner[1] + d1[1] * s); p3 = (corner[0] + d2[0] * s, corner[1] + d2[1] * s)
    p2 = (p1[0] + d2[0] * s, p1[1] + d2[1] * s)
    line(ax, [p1, p2, p3], role, 0.7)
def dot(ax, p, role='sujet', r=1.1): disc(ax, p[0], p[1], r, role)

fig, ax = canvas(62)
c = (15, 24); R = 15; a = math.radians(60)
P = pt(c, R, a); A = (c[0] + R, c[1]); T = (A[0], c[1] + R * math.tan(a))
line(ax, [(c[0] - 3, c[1]), (c[0] + R + 4, c[1])], 'fixe', 0.6)
arc(ax, c, R, 0, pi / 2, 'fixe', 0.8)
line(ax, [(A[0], c[1] - 4), (A[0], c[1] + 30)], 'fixe', 1.4)
line(ax, [c, P], 'sujet', 1.4); line(ax, [P, T], 'varie', 1.2, dash=True)
dot(ax, P, 'sujet'); dot(ax, T, 'resultat', 1.3)
text(ax, c[0] - 2.5, c[1] - 3, '$O$', 'encre', 's'); text(ax, A[0] + 1.5, A[1] - 3, '$A$', 'encre', 's')
text(ax, P[0] - 2.5, P[1] + 2.5, '$P$', 'sujet', 's'); text(ax, T[0] + 3, T[1] + 1, '$T$', 'resultat', 's')
text(ax, 22, 59, '60° : elles se coupent', 'resultat', 's')
c2 = (60, 24); g = c2[0] + R
disc(ax, *c2, R, 'fixe', fill=False)
line(ax, [(g, c2[1] - 4), (g, c2[1] + 30)], 'fixe', 1.4)
line(ax, [c2, (c2[0], c2[1] + R)], 'sujet', 1.4); line(ax, [(c2[0], c2[1] + R), (c2[0], c2[1] + 30)], 'varie', 1.2, dash=True)
dot(ax, (c2[0], c2[1] + R), 'sujet')
text(ax, c2[0] - 2.5, c2[1] - 3, '$O$', 'encre', 's'); text(ax, c2[0] - 3, c2[1] + R, '$P$', 'sujet', 's')
text(ax, 66, 59, '90° : parallèles', 'limite', 's')
text(ax, 66, 8, 'pas de $T$', 'limite', 's')
save(fig, '30-041')
