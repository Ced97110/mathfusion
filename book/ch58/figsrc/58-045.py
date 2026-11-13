import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
ox, oy, k = 8, 12, 14.0
P = lambda a, b: (ox + a * k, oy + b * k)
for i in range(0, 6): line(ax, [P(i, 0), P(i, 3.4)], 'fixe', lw=0.2)
for j in range(0, 4): line(ax, [P(0, j), P(5.4, j)], 'fixe', lw=0.2)
# écriture unique : 3 sacs de riz, 2 sacs de lentilles
arrow(ax, P(0, 0), P(3, 0), 'resultat', lw=1.6)
arrow(ax, P(3, 0), P(3, 2), 'resultat', lw=1.6)
disc(ax, *P(3, 2), 1.5, 'resultat')
text(ax, P(3, 2)[0] - 2, P(3, 2)[1] + 4.5, '(3, 2)', 'resultat', 'm')
text(ax, P(1.5, 0)[0], P(0, 0)[1] - 3.5, r'$3\,e_1$', 'resultat', 's')
text(ax, P(3, 1)[0] - 6, P(3, 1)[1], r'$2\,e_2$', 'resultat', 's')
# autre écriture : 4 sacs de riz
line(ax, [P(3, 0), P(4, 0), P(4, 2)], 'limite', lw=1.4, dash=True)
disc(ax, *P(4, 2), 1.5, 'limite', fill=False)
text(ax, P(4, 2)[0] + 8, P(4, 2)[1] + 4.5, '(4, 2)', 'limite', 'm')
text(ax, P(4, 1)[0] + 8, P(4, 1)[1], r'$2\,e_2$', 'limite', 's')
text(ax, P(3.5, 0)[0] + 7, P(0, 0)[1] - 3.5, r'$4\,e_1$', 'limite', 's')
text(ax, 62, 58, '4 sacs de riz : un autre point', 'limite', 's')
save(fig, '58-045')
