import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
# axes du chapitre 19 : (5, 4) = 5 fois la flèche (1, 0) et 4 fois la flèche (0, 1)
x0, y0, u = 8, 8, 7.6
P = lambda a, b: (x0 + a * u, y0 + b * u)
for a in range(0, 7):
    line(ax, [P(a, 0), P(a, 5)], 'fixe', lw=0.2)
for b in range(0, 6):
    line(ax, [P(0, b), P(6, b)], 'fixe', lw=0.2)
for k in range(5):
    arrow(ax, P(k, 0), P(k + 1, 0), 'sujet', lw=1.5)
for k in range(4):
    arrow(ax, P(5, k), P(5, k + 1), 'autre', lw=1.5)
arrow(ax, P(0, 0), P(0, 1), 'autre', lw=2.2)
disc(ax, *P(5, 4), 1.7, 'resultat')
text(ax, P(0, 0)[0] - 2.5, P(0, 0)[1] - 2.5, 'O', 'encre', 's')
text(ax, P(0.5, 0)[0], P(0.5, 0)[1] - 3.2, r'$e_1$', 'sujet', 's', weight='bold')
text(ax, P(0, 0.5)[0] + 3.0, P(0, 0.5)[1], r'$e_2$', 'autre', 's', weight='bold')
text(ax, P(2.5, 0)[0], P(2.5, 0)[1] - 3.6, r'$5\,e_1$', 'sujet', 'm', weight='bold')
text(ax, P(5, 2)[0] + 2.2, P(5, 2)[1], r'$4\,e_2$', 'autre', 'm', weight='bold', ha='left')
text(ax, P(5, 4)[0] - 2.5, P(5, 4)[1] + 3.2, '(5, 4)', 'resultat', 's', weight='bold', ha='right')
text(ax, 72, 46, 'axes du chapitre 19', 'fixe', 's', ha='center')
save(fig, '58-030')
