import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, oy, d = 12, 10, 12
for i in range(5):
    for j in range(5): disc(ax, ox + i*d, oy + j*d, 1.1, 'fixe')
P = lambda a, b: (ox + a*d, oy + b*d)
line(ax, [P(1,0), P(3,3)], 'sujet', dash=True); line(ax, [P(2,3), P(3,3)], 'autre', dash=True)
arrow(ax, P(0,0), P(2,3), 'sujet', lw=1.3); arrow(ax, P(0,0), P(1,0), 'autre', lw=1.3)
arrow(ax, P(0,0), P(3,3), 'resultat', lw=1.3)
text(ax, P(2,3)[0] - 7, P(2,3)[1] + 2, '(2, 3)', 'sujet', 's')
text(ax, P(1,0)[0], P(1,0)[1] - 3.5, '(1, 0)', 'autre', 's')
text(ax, P(3,3)[0] + 7, P(3,3)[1] + 2, '(3, 3)', 'resultat', 's')
text(ax, 60, 64, r'$\mathbb{Z}\times\mathbb{Z}$ : couples d’entiers', 'encre', 's')
text(ax, 72, 24, 'on additionne', 'resultat', 's'); text(ax, 72, 19.5, 'l’ordre ne change rien', 'resultat', 's')
save(fig, '74-184')
