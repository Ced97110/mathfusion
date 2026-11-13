import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pol(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role='varie', lw=0.9, n=30):
    line(ax, [pol(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw)
def sq(ax, p, d1, d2, s=2.2, role='fixe'):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)
fig, ax = canvas(66)
O = (14, 8); R = 50
arrow(ax, (O[0] - 3, O[1]), (O[0] + R + 8, O[1]), 'fixe', lw=0.7); arrow(ax, (O[0], O[1] - 3), (O[0], O[1] + R + 6), 'fixe', lw=0.7)
arc(ax, O, R, 0, 90, 'sujet', lw=1.2)
p0 = pol(O, R, 0); p30 = pol(O, R, 30); p90 = pol(O, R, 90)
arc(ax, O, 0.82 * R, 1, 28, 'varie', lw=1.3); arrow(ax, pol(O, 0.82 * R, 27), pol(O, 0.82 * R, 30), 'varie')
arc(ax, O, 0.62 * R, 1, 88, 'varie', lw=1.3); arrow(ax, pol(O, 0.62 * R, 87), pol(O, 0.62 * R, 90), 'varie')
disc(ax, p0[0], p0[1], 1.6, 'sujet'); disc(ax, p30[0], p30[1], 1.6, 'resultat'); disc(ax, p90[0], p90[1], 1.6, 'resultat')
text(ax, p0[0], 3.5, '(1, 0)', 'sujet', 's')
text(ax, 71, 42, r'$(\cos\theta,\ \sin\theta)$', 'resultat', 's')
text(ax, 71, 36, '≈ (0,866 ; 0,5)', 'resultat', 's')
text(ax, 71, p90[1] - 2, '(0, 1)', 'resultat', 's')
text(ax, 71, p90[1] - 8, 'rotation de 90°', 'varie', 's')
text(ax, 71, 27, 'rotation de 30°', 'varie', 's')
save(fig, '26-129')
