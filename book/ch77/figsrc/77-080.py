import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
u = 17; O = (10, 14)
P = lambda a, b: (O[0] + a * u, O[1] + b * u)
arrow(ax, (4, O[1]), (O[0] + 3 * u, O[1]), 'fixe', lw=0.7); arrow(ax, (O[0], 8), (O[0], O[1] + 1.75 * u), 'fixe', lw=0.7)
poly(ax, [P(0, 0), P(2, 0), P(2, 1), P(0, 1)], 'varie')
poly(ax, [P(0, 0), P(1, 0), P(1, 1), P(0, 1)], 'sujet')
for p, s, dx, dy, ro in [((1, 0), '1', 0, -3.4, 'sujet'), ((0, 1), r'$\sqrt{2}$', -4.6, 0, 'sujet'), ((1, 1), r'$1+\sqrt{2}$', 0, 3.4, 'sujet'),
                         ((2, 0), '2', 0, -3.4, 'varie'), ((2, 1), r'$2+\sqrt{2}$', 0, 3.4, 'varie')]:
    disc(ax, *P(*p), 0.9, ro); text(ax, P(*p)[0] + dx, P(*p)[1] + dy, s, ro, 's')
text(ax, P(0.5, 0.5)[0] + 2, P(0.5, 0.5)[1] + 2.5, 'aire 1', 'sujet', 's')
text(ax, P(1.5, 0.5)[0], P(1.5, 0.5)[1], 'aire 2', 'varie', 'm')
arrow(ax, (P(1, 0)[0] - 1.2, P(1, 0)[1] + 1.2), (P(0, 1)[0] + 1.2, P(0, 1)[1] - 1.2), 'varie', curve=0.35)
arrow(ax, (P(0, 1)[0] + 1.2, P(0, 1)[1] + 1.4), (P(2, 0)[0] - 1.4, P(2, 0)[1] + 1.2), 'varie', curve=-0.45)
arrow(ax, (P(1, 1)[0] + 1.4, P(1, 1)[1]), (P(2, 1)[0] - 1.4, P(2, 1)[1]), 'varie')
text(ax, 72, 40, r'$\times\sqrt{2}$', 'varie', 'm'); text(ax, 72, 31, r'$\det=-2$', 'resultat', 'm')
text(ax, 72, 22, 'axe horizontal : 1', 'fixe', 's'); text(ax, 72, 17.5, r'axe vertical : $\sqrt{2}$', 'fixe', 's')
save(fig, '77-080')
