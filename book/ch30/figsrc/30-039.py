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
c = (24, 33); R = 24
disc(ax, *c, R, 'fixe', fill=False)
line(ax, [(c[0] - R - 3, c[1]), (c[0] + R + 3, c[1])], 'fixe', 0.6)
line(ax, [(c[0], c[1] - R - 3), (c[0], c[1] + R + 3)], 'fixe', 0.6)
line(ax, [c, (c[0], c[1] + R)], 'sujet', 2.0)
top = (c[0], c[1] + R); bot = (c[0], c[1] - R)
dot(ax, top, 'limite', 1.5); dot(ax, bot, 'limite', 1.5)
dot(ax, c, 'resultat', 1.3)
text(ax, top[0] + 3, top[1] - 0.5, r'$P$ : 1,57', 'limite', 's', ha='left')
text(ax, bot[0] + 3, bot[1] + 0.5, r'$P$ : 4,71', 'limite', 's', ha='left')
text(ax, c[0] - 2, c[1] + 12, '$\\sin$ = 1', 'sujet', 's', ha='right')
text(ax, c[0] + 3, c[1] - 3.3, '$\\cos$ = 0', 'resultat', 's', ha='left')
text(ax, 70, 44, r'$\tan x$ = 1 $\div$ 0', 'limite', 'm')
text(ax, 70, 36, 'aucun nombre', 'limite', 's')
text(ax, 70, 24, r'$x=\pi/2+k\pi$', 'limite', 'm')
text(ax, 70, 17, 'valeurs interdites', 'limite', 's')
save(fig, '30-039')
