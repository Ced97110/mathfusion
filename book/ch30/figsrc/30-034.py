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

fig, ax = canvas(57)
c = (40, 10); R = 32; a = math.radians(30)
H = (c[0] + R * math.cos(a), c[1]); P = pt(c, R, a); Q = pt(c, R, a + pi / 2); Hp = (c[0], c[1] + R * math.cos(a))
line(ax, [(c[0] - 34, c[1]), (c[0] + 44, c[1])], 'fixe', 0.6)
line(ax, [(c[0], c[1]), (c[0], c[1] + R + 3)], 'fixe', 0.6)
arc(ax, c, R, 0, pi * 0.72, 'fixe', 0.7)
poly(ax, [c, Hp, Q], 'varie')
poly(ax, [c, H, P], 'sujet')
line(ax, [c, Hp], 'resultat', 2.0)
arc(ax, c, R, a, a + pi / 2, 'varie', 1.2, head=True)
for p, r in ((P, 'sujet'), (Q, 'varie')): dot(ax, p, r)
text(ax, c[0] - 2.5, c[1] - 3, '$O$', 'encre', 's')
text(ax, H[0], H[1] - 3, '$H$', 'encre', 's')
text(ax, P[0] + 2.5, P[1] + 2.5, '$P$', 'sujet', 's')
text(ax, Q[0] - 1, Q[1] + 3.5, '$Q$', 'varie', 's')
text(ax, (c[0] + H[0]) / 2, c[1] - 3.2, '$OH$ = 0,866', 'sujet', 's')
text(ax, H[0] + 2.5, (c[1] + P[1]) / 2, '$HP$ = 0,5', 'sujet', 's', ha='left')
text(ax, *pt(c, R + 5, a + pi / 4), 'quart de tour', 'varie', 's')
text(ax, Q[0] - 2.5, Q[1], 'hauteur de $Q$ :\n0,866', 'resultat', 's', ha='right')
save(fig, '30-034')
