import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$Q=x^2+y^2$ sur $\mathbb{F}_3$', 'encre', 'm')
P = lambda i, j: (14 + 13 * i, 10 + 13 * j)
for i in range(3):
    for j in range(3):
        q = (i * i + j * j) % 3
        disc(ax, *P(i, j), 2.4, 'sujet' if q == 1 else 'fixe')
    text(ax, P(i, 0)[0], 4, str(i), 'fixe', 's'); text(ax, 5, P(0, i)[1], str(i), 'fixe', 's')
disc(ax, *P(1, 0), 2.4, 'varie'); text(ax, P(1, 0)[0] + 4, P(1, 0)[1] - 3.5, r'$x$', 'varie', 's')
arrow(ax, (P(1, 0)[0] - 1.5, P(1, 0)[1] + 3), (P(0, 2)[0] + 2, P(0, 2)[1] - 3.5), 'resultat')
arrow(ax, (P(1, 0)[0], P(1, 0)[1] + 3.5), (P(1, 1)[0], P(1, 1)[1] - 3.5), 'limite')
disc(ax, 56, 44, 2.4, 'sujet'); text(ax, 61, 44, r'$Q(y)=1$', 'sujet', 's', ha='left')
disc(ax, 56, 36, 2.4, 'fixe'); text(ax, 61, 36, r'$Q(y)\neq1$', 'fixe', 's', ha='left')
arrow(ax, (53.5, 27), (58.5, 27), 'resultat'); text(ax, 61, 27, 'permis', 'resultat', 's', ha='left')
arrow(ax, (53.5, 19), (58.5, 19), 'limite'); text(ax, 61, 19, 'impossible', 'limite', 's', ha='left')
save(fig, '75-130')
