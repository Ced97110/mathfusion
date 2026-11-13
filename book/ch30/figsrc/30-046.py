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

fig, ax = canvas(66)
k = 24
O = (5, 12); H = (O[0] + 0.5 * k, O[1]); Pp = (H[0], O[1] + 0.866 * k)
poly(ax, [O, H, Pp], 'autre')
sq(ax, H, (-1, 0), (0, 1), 2.0)
text(ax, (O[0] + H[0]) / 2, O[1] - 3.2, '0,5', 'autre', 's', ha='center')
text(ax, H[0] + 1.5, (O[1] + Pp[1]) / 2, '0,866', 'autre', 's', ha='left')
text(ax, 17, 52, 'avant :', 'autre', 's'); text(ax, 17, 47.5, 'un rapport', 'autre', 's')
text(ax, 18, 4.5, r'0,866 $\div$ 0,5 = 1,732', 'autre', 's')
arrow(ax, (31, 33), (37, 33), 'fixe')
c = (50, 22); R = 12; a = math.radians(60)
A = (c[0] + R, c[1]); T = (A[0], c[1] + R * math.tan(a))
arc(ax, c, R, 0, pi / 2, 'fixe', 0.8)
line(ax, [(c[0] - 2, c[1]), (A[0] + 3, c[1])], 'fixe', 0.6)
line(ax, [(A[0], c[1] - 4), (A[0], c[1] + 30)], 'sujet', 1.5)
line(ax, [c, T], 'fixe', 0.8, dash=True)
line(ax, [A, T], 'resultat', 2.4)
dot(ax, A, 'sujet', 1.5); dot(ax, T, 'resultat', 1.3)
text(ax, A[0] + 2.5, A[1] - 4, 'touche en $A$', 'sujet', 's', ha='left')
text(ax, T[0] + 3, (A[1] + T[1]) / 2, '1,732', 'resultat', 's', ha='left')
text(ax, 66, 62, 'maintenant :', 'sujet', 's'); text(ax, 66, 57.5, 'une longueur', 'sujet', 's')
save(fig, '30-046')
