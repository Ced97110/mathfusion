import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pol(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role='varie', lw=0.9, n=30):
    line(ax, [pol(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw)
def sq(ax, p, d1, d2, s=2.2, role='fixe'):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)
fig, ax = canvas(56)
O = (10, 10); u = 2.5
Q = pol(O, 20 * u, 30); P = pol(O, 10 * u, 30)
arrow(ax, (O[0] - 3, O[1]), (82, O[1]), 'fixe', lw=0.7); arrow(ax, (O[0], O[1] - 3), (O[0], 53), 'fixe', lw=0.7)
line(ax, [O, Q], 'sujet', lw=1.5)
line(ax, [O, (Q[0], O[1])], 'autre', lw=2.0)
line(ax, [(Q[0], O[1]), Q], 'varie', lw=2.0)
line(ax, [P, (P[0], O[1])], 'varie', lw=1.0, dash=True); line(ax, [(P[0], P[1]), (O[0], P[1])], 'autre', lw=0.8, dash=True)
disc(ax, P[0], P[1], 1.3, 'sujet'); disc(ax, Q[0], Q[1], 1.3, 'sujet')
arc(ax, O, 9, 0, 30, 'fixe'); text(ax, 23, 12.6, '30°', 'fixe', 's')
text(ax, 21, 29, '10', 'sujet', 's'); text(ax, 40, 40, '20', 'sujet', 's')
text(ax, P[0] + 11, P[1] - 7, '(8,66 ; 5)', 'sujet', 's')
text(ax, Q[0] + 15, Q[1] + 4, '(17,32 ; 10)', 'sujet', 's')
text(ax, 33, 5, r'$r\cos\theta$', 'autre', 's'); text(ax, Q[0] + 8, 25, r'$r\sin\theta$', 'varie', 's')
text(ax, 44, 51, r'$(r\cos\theta,\ r\sin\theta)$', 'resultat', 'm', weight='bold')
save(fig, '26-125')
