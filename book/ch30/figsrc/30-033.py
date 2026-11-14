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
c = (26, 34); R = 22
disc(ax, *c, R, 'fixe', fill=False)
line(ax, [(c[0] - R - 3, c[1]), (c[0] + R + 3, c[1])], 'fixe', 0.6)
line(ax, [(c[0], c[1] - R - 3), (c[0], c[1] + R + 3)], 'resultat', 1.5)
arc(ax, c, 12, 0, pi / 2, 'varie', 1.2, head=True)
arc(ax, c, 12, pi / 2, 3 * pi / 2, 'varie', 1.2, head=True)
text(ax, *pt(c, 17, pi / 4), '1,57', 'varie', 's')
text(ax, c[0] - 17.5, c[1], '3,14', 'varie', 's')
top = pt(c, R, pi / 2); bot = pt(c, R, 3 * pi / 2)
dot(ax, top, 'sujet', 1.5); dot(ax, bot, 'sujet', 1.5)
text(ax, top[0] + 3, top[1] + 2.5, r'$P$ : 1,57', 'sujet', 's', ha='left')
text(ax, bot[0] + 3, bot[1] - 2.5, r'$P$ : 4,71', 'sujet', 's', ha='left')
text(ax, c[0] + 1.5, c[1] - 7, r'$\cos = 0$', 'resultat', 's', ha='left')
text(ax, 70, 52, r'$x=\pi/2+k\pi$', 'resultat', 'l')
text(ax, 70, 42, 'un quart de tour,', 'encre', 's')
text(ax, 70, 37, r'puis $k$ demi-tours', 'encre', 's')
save(fig, '30-033')
