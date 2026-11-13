import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
# même point (5, 4) atteint par les sacs (5 e1 puis 4 e2) et par les lots (f1 puis 3 f2)
x0, y0, u = 6, 10, 7.2
P = lambda a, b: (x0 + a * u, y0 + b * u)
for a in range(0, 7):
    line(ax, [P(a, 0), P(a, 5)], 'fixe', lw=0.25)
for b in range(0, 6):
    line(ax, [P(0, b), P(6, b)], 'fixe', lw=0.25)
# description par les sacs : 5 pas de e1, puis 4 pas de e2
arrow(ax, P(0, 0), P(5, 0), 'sujet', lw=1.6)
arrow(ax, P(5, 0), P(5, 4), 'autre', lw=1.6)
# description par les lots : f1 = (2, 1) puis trois fois f2 = (1, 1)
pts = [(0, 0), (2, 1), (3, 2), (4, 3), (5, 4)]
for (a, b), (c, d) in zip(pts[:-1], pts[1:]):
    arrow(ax, P(a, b), P(c, d), 'varie', lw=1.3)
disc(ax, *P(5, 4), 1.6, 'resultat')
text(ax, P(5, 4)[0] + 4, P(5, 4)[1], '(5, 4)', 'resultat', 's', weight='bold', ha='left')
text(ax, P(0, 0)[0] - 2.2, P(0, 0)[1] - 3, 'O', 'encre', 's')
# lecture
text(ax, 50, 60, r'sacs $e_1,\ e_2$ : 5 et 4', 'encre', 's', ha='left')
text(ax, 50, 55, r'lots $f_1,\ f_2$ : 1 et 3', 'varie', 's', ha='left')
text(ax, 50, 50, 'même point', 'resultat', 's', ha='left')
save(fig, '58-016')
