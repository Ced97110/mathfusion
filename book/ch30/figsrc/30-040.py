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

fig, ax = canvas(76)
c = (16, 28); R = 20; a = math.radians(60)
P = pt(c, R, a); A = (c[0] + R, c[1]); T = (A[0], c[1] + R * math.tan(a))
line(ax, [(c[0] - 4, c[1]), (c[0] + R + 5, c[1])], 'fixe', 0.6)
arc(ax, c, R, 0, pi / 2, 'fixe', 0.8)
line(ax, [(A[0], c[1] - 4), (A[0], c[1] + 40)], 'fixe', 1.4)
line(ax, [c, P], 'sujet', 1.4); line(ax, [P, T], 'varie', 1.1, dash=True)
line(ax, [A, T], 'resultat', 2.2)
dot(ax, P, 'sujet'); dot(ax, T, 'resultat', 1.3)
text(ax, c[0] - 2.5, c[1] - 3, '$O$', 'encre', 's'); text(ax, A[0] + 1.5, A[1] - 3, '$A$', 'encre', 's')
text(ax, P[0] - 2.5, P[1] + 2.5, '$P$', 'sujet', 's'); text(ax, T[0] - 2.5, T[1] + 3, '$T$', 'resultat', 's')
text(ax, A[0] + 2.5, (A[1] + T[1]) / 2, '$AT$ = 1,73', 'resultat', 's', ha='left')
gx, gy = 69, c[1]; s = 8.5
for sg in (-1, 1):
    line(ax, [(gx + sg * pi / 2 * s, gy - 22), (gx + sg * pi / 2 * s, gy + 38)], 'limite', 0.9, dash=True)
line(ax, [(gx - 15, gy), (gx + 17, gy)], 'fixe', 0.6)
xs = [-1.38 + i * 2.76 / 80 for i in range(81)]
line(ax, [(gx + t * s, gy + R * math.tan(t)) for t in xs if -21 < R * math.tan(t) < 37], 'sujet', 1.4)
line(ax, [(A[0], T[1]), (gx + (pi / 3) * s, T[1])], 'fixe', 0.6, dash=True)
dot(ax, (gx + (pi / 3) * s, T[1]), 'resultat', 1.1)
text(ax, gx - pi / 2 * s, gy - 25, r'$-\pi/2$', 'limite', 's'); text(ax, gx + pi / 2 * s, gy - 25, r'$\pi/2$', 'limite', 's')
text(ax, gx, gy + 41.5, 'graphe de tan', 'sujet', 's')
save(fig, '30-040')
