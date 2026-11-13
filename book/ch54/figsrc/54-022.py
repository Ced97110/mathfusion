import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
O = (10, 12); ua, ub = 12, 9
X = lambda a: O[0] + ua * a
Y = lambda b: O[1] + ub * b
for a in range(6):
    for b in range(8):
        disc(ax, X(a), Y(b), 0.4, 'fixe')
arrow(ax, O, (X(5.6), O[1]), 'fixe', lw=0.7)
arrow(ax, O, (O[0], Y(7.6)), 'fixe', lw=0.7)
line(ax, [(X(0), Y(0)), (X(4.6), Y(6.9))], 'sujet', lw=1.2)
p4 = (X(4), Y(6)); p2 = (X(2), Y(3))
d = (p2[0] - p4[0], p2[1] - p4[1]); n = math.hypot(*d); u = (d[0] / n, d[1] / n)
arrow(ax, (p4[0] + 2.2 * u[0], p4[1] + 2.2 * u[1]), (p2[0] - 2.2 * u[0], p2[1] - 2.2 * u[1]), 'varie', lw=1.6)
disc(ax, *p4, 1.5, 'sujet')
disc(ax, *p2, 1.5, 'resultat')
text(ax, p4[0] + 3, p4[1], '4/6', 'sujet', 'm', ha='left')
text(ax, p2[0] + 3, p2[1] - 1, '2/3', 'resultat', 'm', ha='left')
t = text(ax, 14, 58, '÷ 2 pour chaque nombre', 'varie', 's', ha='left')
t.set_bbox(dict(fc='white', ec='none', pad=0.8))
t = text(ax, 84, 24, 'même droite : $b/a=1{,}5$', 'sujet', 's', ha='right')
t.set_bbox(dict(fc='white', ec='none', pad=0.8))
text(ax, 44, 4, r'$4\times3=12=6\times2$', 'fixe', 's')
save(fig, '54-022')
