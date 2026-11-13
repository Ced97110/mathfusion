import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
X = lambda x: 34 + 14 * x; Y = lambda y: 12 + 12 * y
line(ax, [(X(1), 6), (X(1), 42)], 'fixe', dash=True); text(ax, X(1), 47, r'miroir : $x=1$', 'fixe', 's')
for (p, q, a, b, lp, lq, dy) in [((3, 2), (-1, 2), 'sujet', 'resultat', '(3, 2)', '(−1, 2)', 4),
                                 ((0, 0), (2, 0), 'sujet', 'resultat', '(0, 0)', '(2, 0)', -4.5)]:
    arrow(ax, (X(p[0]) + (-1.8 if q[0] < p[0] else 1.8), Y(p[1])), (X(q[0]) + (1.8 if q[0] < p[0] else -1.8), Y(q[1])), 'varie')
    disc(ax, X(p[0]), Y(p[1]), 1.4, a); disc(ax, X(q[0]), Y(q[1]), 1.4, b)
    text(ax, X(p[0]), Y(p[1]) + dy, lp, a, 's'); text(ax, X(q[0]), Y(q[1]) + dy, lq, b, 's')
text(ax, 48, 24, r'$(0,0)$ ne reste pas fixe', 'varie', 's', ha='center')
save(fig, '73-114')
