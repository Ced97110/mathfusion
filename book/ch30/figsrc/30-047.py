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

fig, ax = canvas(64)
c = (12, 8); k = 44; a = math.radians(60)
H = (c[0] + 0.5 * k, c[1]); P = (H[0], c[1] + 0.866 * k)
ext = (c[0] + (56 - c[1]) / math.tan(a), 56)
line(ax, [(c[0] - 3, c[1]), (c[0] + 62, c[1])], 'fixe', 0.6)
line(ax, [(c[0], c[1] - 2), (c[0], c[1] + 52)], 'fixe', 0.6)
line(ax, [c, ext], 'sujet', 1.6)
line(ax, [c, H], 'fixe', 1.8); line(ax, [H, P], 'varie', 1.8)
sq(ax, H, (-1, 0), (0, 1), 2.0)
dot(ax, P, 'sujet')
arc(ax, c, 14, 0, a, 'resultat', 1.3)
text(ax, c[0] + 17, c[1] + 4, '60°', 'resultat', 's')
arc(ax, c, 22, a, pi / 2, 'limite', 1.3)
text(ax, c[0] + 5.5, c[1] + 25, '30°', 'limite', 's')
text(ax, (c[0] + H[0]) / 2, c[1] - 3.2, 'avance 0,5', 'fixe', 's')
text(ax, H[0] + 1.5, (c[1] + P[1]) / 2, 'monte\n0,866', 'varie', 's', ha='left')
text(ax, 62, 56, 'pente = 1,732', 'sujet', 'm')
text(ax, 62, 50, r'= $\tan 60°$', 'resultat', 's')
text(ax, 62, 36, 'depuis la verticale :', 'limite', 's')
text(ax, 62, 31, r'$\tan 30°$ = 0,577', 'limite', 's')
text(ax, 62, 26, 'pas la pente', 'limite', 's')
save(fig, '30-047')
