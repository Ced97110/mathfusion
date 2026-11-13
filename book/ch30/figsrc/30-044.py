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

fig, ax = canvas(70)
c = (10, 8); R = 30; a = math.radians(60)
P = pt(c, R, a); H = (P[0], c[1]); A = (c[0] + R, c[1]); T = (A[0], c[1] + R * math.sqrt(3))
line(ax, [(c[0] - 3, c[1]), (A[0] + 4, c[1])], 'fixe', 0.6)
arc(ax, c, R, 0, a + 0.35, 'fixe', 0.7)
line(ax, [(A[0], c[1] - 3), (A[0], c[1] + 56)], 'fixe', 1.2)
poly(ax, [c, H, P], 'sujet')
line(ax, [c, T], 'sujet', 1.0)
line(ax, [A, T], 'resultat', 2.4)
dot(ax, T, 'resultat', 1.3); dot(ax, P, 'sujet')
line(ax, [(A[0] - 1.5, c[1] + R), (A[0] + 1.5, c[1] + R)], 'encre', 1.0)
text(ax, A[0] + 3, c[1] + R, '1', 'encre', 's', ha='left')
text(ax, c[0] - 2.5, c[1] - 3, '$O$', 'encre', 's'); text(ax, A[0] + 1.5, c[1] - 3, '$A$', 'encre', 's')
text(ax, T[0] - 2.5, T[1] + 1, '$T$', 'resultat', 's', ha='right')
text(ax, H[0] + 1.5, (c[1] + P[1]) / 2 - 3, r'$\frac{\sqrt{3}}{2}$', 'sujet', 's', ha='left')
text(ax, (c[0] + H[0]) / 2, c[1] - 3.5, r'$\frac{1}{2}$', 'sujet', 's')
text(ax, 72, 56, r'$AT=\sqrt{3}$', 'resultat', 'l')
text(ax, 72, 49, '$\\approx$ 1,73', 'resultat', 'm')
text(ax, 72, 33, r'$\frac{\sqrt{3}/2}{1/2}=\sqrt{3}$', 'encre', 'm')
save(fig, '30-044')
