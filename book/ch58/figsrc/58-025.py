import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
# Fig. 58.1 : w = 2u + v ; deux pointillés parallèles à v et à u se coupent en un seul point
x0, y0, u = 8, 8, 7.4
P = lambda a, b: (x0 + a * u, y0 + b * u)
for a in range(0, 7):
    line(ax, [P(a, 0), P(a, 5)], 'fixe', lw=0.2)
for b in range(0, 6):
    line(ax, [P(0, b), P(6, b)], 'fixe', lw=0.2)
# pointillés : de 2u parallèle à v, de v parallèle à u
line(ax, [P(4, 2), P(5, 4)], 'autre', lw=1.0, dash=True)
line(ax, [P(1, 2), P(5, 4)], 'sujet', lw=1.0, dash=True)
# marche : deux fois u, puis une fois v
arrow(ax, P(0, 0), P(2, 1), 'sujet', lw=1.8)
arrow(ax, P(2, 1), P(4, 2), 'sujet', lw=1.8)
arrow(ax, P(4, 2), P(5, 4), 'autre', lw=1.8)
arrow(ax, P(0, 0), P(1, 2), 'autre', lw=1.0)
disc(ax, *P(5, 4), 1.7, 'resultat')
text(ax, P(0, 0)[0] - 2.5, P(0, 0)[1] - 2.5, 'O', 'encre', 's')
text(ax, P(1, 0.5)[0] + 2.5, P(1, 0.5)[1] - 2.6, r'$u$', 'sujet', 'm', weight='bold')
text(ax, P(3, 1.5)[0] + 2.2, P(3, 1.5)[1] - 3.0, r'$2u$', 'sujet', 'm', weight='bold')
text(ax, P(0.5, 1)[0] - 2.6, P(0.5, 1)[1] + 1, r'$v$', 'autre', 'm', weight='bold')
text(ax, P(4.5, 3)[0] + 2.8, P(4.5, 3)[1] - 1.5, r'$v$', 'autre', 'm', weight='bold')
text(ax, P(5, 4)[0] + 3.2, P(5, 4)[1] + 2.5, r'$w$', 'resultat', 'm', weight='bold')
text(ax, 70, 44, r'$w = 2u + v$', 'encre', 'l', weight='bold')
text(ax, 70, 36, 'un seul point', 'resultat', 's')
save(fig, '58-025')
