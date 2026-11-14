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

fig, ax = canvas(68)
c = (10, 14); R = 14; a = math.radians(60)
P = pt(c, R, a)
line(ax, [(c[0] - 3, c[1]), (c[0] + 2 * R + 4, c[1])], 'fixe', 0.6)
arc(ax, c, R, 0, pi / 2, 'fixe', 0.8)
A1 = (c[0] + R, c[1]); A2 = (c[0] + 2 * R, c[1])
T1 = (A1[0], c[1] + R * math.tan(a)); T2 = (A2[0], c[1] + 2 * R * math.tan(a))
line(ax, [(A1[0], c[1]), (A1[0], c[1] + 28)], 'fixe', 1.2)
line(ax, [(A2[0], c[1]), (A2[0], c[1] + 52)], 'fixe', 1.2)
line(ax, [c, T2], 'sujet', 1.3)
line(ax, [A1, T1], 'resultat', 2.4); line(ax, [A2, T2], 'autre', 2.4)
dot(ax, T1, 'resultat', 1.3); dot(ax, T2, 'autre', 1.3)
text(ax, c[0] - 2.5, c[1] - 3, '$O$', 'encre', 's')
text(ax, A1[0], c[1] - 3.5, 'à 1', 'fixe', 's'); text(ax, A2[0] + 1, c[1] - 3.5, 'à 2', 'fixe', 's')
text(ax, T1[0] - 2, T1[1] + 2, '1,732', 'resultat', 's', ha='right')
text(ax, T2[0] + 3, T2[1] - 1, '3,464', 'autre', 's', ha='left')
text(ax, 62, 30, r'$\tan 60°$ = 1,732', 'resultat', 's')
text(ax, 62, 24, r'à 2 : 2 $\times$ 1,732', 'autre', 's')
save(fig, '30-043')
