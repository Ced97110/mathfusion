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
c = (8, 10); R = 30; a = math.radians(60)
P = pt(c, R, a); H = (P[0], c[1]); A = (c[0] + R, c[1]); T = (A[0], c[1] + R * math.tan(a))
poly(ax, [c, A, T], 'autre'); poly(ax, [c, H, P], 'sujet')
line(ax, [(c[0] - 3, c[1]), (A[0] + 4, c[1])], 'fixe', 0.6)
sq(ax, H, (-1, 0), (0, 1), 2.2); sq(ax, A, (-1, 0), (0, 1), 2.2)
arc(ax, c, 9, 0, a, 'varie', 1.1)
text(ax, c[0] + 12, c[1] + 3.2, r'$\theta$', 'varie', 's')
text(ax, c[0] - 2.5, c[1] - 3, '$O$', 'encre', 's'); text(ax, H[0], c[1] - 3, '$H$', 'sujet', 's'); text(ax, A[0] + 1.5, c[1] - 3, '$A$', 'autre', 's')
text(ax, P[0] - 2.5, P[1] + 2.5, '$P$', 'sujet', 's'); text(ax, T[0] - 2.5, T[1] + 3, '$T$', 'autre', 's')
text(ax, (c[0] + A[0]) / 2 + 6, c[1] - 7, '$OA$ = 1', 'autre', 's')
text(ax, H[0] + 12, (c[1] + P[1]) / 2 + 7, '', 'sujet', 's') if False else None
text(ax, 66, 54, 'même angle en $O$', 'varie', 's')
text(ax, 66, 49, 'angle droit en $H$, $A$', 'fixe', 's')
text(ax, 66, 40, 'même forme', 'encre', 'm')
text(ax, 66, 28, r'$\frac{AT}{OA}=\frac{HP}{OH}$', 'encre', 'l')
text(ax, 66, 17, r'$AT$ = $\tan\theta$', 'resultat', 'l')
save(fig, '30-042')
