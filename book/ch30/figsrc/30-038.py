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

fig, ax = canvas(56)
c = (12, 8); R = 36; a = math.radians(60)
P = pt(c, R, a); H = (P[0], c[1])
arc(ax, c, R, 0, pi / 2, 'fixe', 0.7)
line(ax, [(c[0] - 6, c[1]), (c[0] + R + 4, c[1])], 'fixe', 0.6)
line(ax, [c, H], 'autre', 2.0); line(ax, [H, P], 'sujet', 2.0); line(ax, [c, P], 'fixe', 0.9)
sq(ax, H, (-1, 0), (0, 1), 2.2)
dot(ax, P, 'fixe')
arc(ax, c, 8, 0, a, 'varie', 1.1)
text(ax, c[0] + 11.5, c[1] + 3.2, '60°', 'varie', 's')
text(ax, c[0] - 2.5, c[1] - 3, '$O$', 'encre', 's'); text(ax, P[0] + 2.5, P[1] + 2, '$P$', 'encre', 's')
text(ax, H[0] + 1.5, (c[1] + P[1]) / 2, '$\\sin$ = 0,866', 'sujet', 's', ha='left')
text(ax, (c[0] + H[0]) / 2, c[1] - 3.2, '$\\cos$ = 0,5', 'autre', 's')
text(ax, 66, 46, r'$\tan x = \sin x \div \cos x$', 'encre', 's')
text(ax, 66, 34, r'0,866 $\div$ 0,5', 'encre', 'm')
text(ax, 66, 26, '= 1,732', 'resultat', 'l', weight='bold')
save(fig, '30-038')
