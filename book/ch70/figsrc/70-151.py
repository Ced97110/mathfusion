import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
# left: vectors (2,1) and (1,2), area 3
o, u = (5, 8), 9
P = lambda a, b: (o[0] + a * u, o[1] + b * u)
poly(ax, [P(0, 0), P(2, 1), P(3, 3), P(1, 2)], 'resultat')
arrow(ax, P(0, 0), P(2, 1), 'sujet', lw=1.4)
arrow(ax, P(0, 0), P(1, 2), 'autre', lw=1.4)
text(ax, *P(1.5, 1.5), 'aire = 3', 'resultat', 's', weight='bold')
text(ax, P(2, 1)[0] + 5.5, P(2, 1)[1] - 3, '(2, 1)', 'sujet', 's')
text(ax, P(1, 2)[0] - 5.5, P(1, 2)[1] + 2.5, '(1, 2)', 'autre', 's')
text(ax, 20, 46, 'vecteurs non alignés', 'encre', 's')
# right: vectors (2,1) and (4,2), flat
o2, u2 = (50, 8), 5.5
Q = lambda a, b: (o2[0] + a * u2, o2[1] + b * u2)
line(ax, [Q(0, 0), Q(6, 3)], 'fixe', lw=2.6)
arrow(ax, Q(0, 0), Q(4, 2), 'autre', lw=1.4)
arrow(ax, Q(0, 0), Q(2, 1), 'sujet', lw=1.4)
text(ax, Q(2, 1)[0] + 1, Q(2, 1)[1] - 4.5, '(2, 1)', 'sujet', 's')
text(ax, Q(4, 2)[0] - 5, Q(4, 2)[1] + 5, '(4, 2)', 'autre', 's')
text(ax, 76, 11, 'aire = 0', 'resultat', 's', weight='bold')
text(ax, 67, 46, 'vecteurs alignés', 'encre', 's')
save(fig, '70-151')
