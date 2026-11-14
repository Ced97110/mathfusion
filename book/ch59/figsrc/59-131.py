import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u, ox, oy = 14.0, 6.0, 8.0
P = lambda a, b: (ox + a * u, oy + b * u)
poly(ax, [P(0, 0), P(2, 1), P(3, 2), P(1, 1)], 'sujet')
for a in range(4):
    for b in range(3):
        v = (a, b) in [(0, 0), (2, 1), (3, 2), (1, 1)]
        disc(ax, *P(a, b), 0.9, 'sujet' if v else 'fixe')
arrow(ax, P(0, 0), P(2, 1), 'sujet')
arrow(ax, P(0, 0), P(1, 1), 'sujet')
text(ax, P(2, 1)[0] + 3, P(2, 1)[1] - 4.5, '(2, 1)', 'sujet', 's')
text(ax, P(1, 1)[0] - 6, P(1, 1)[1] + 4, '(1, 1)', 'sujet', 's')
text(ax, 72, 42, 'aire = 1', 'resultat', 'm', weight='bold')
text(ax, 72, 34, r'$2\times1-1\times1=1$', 'encre', 's')
text(ax, 72, 25, '1 point par cellule', 'encre', 's')
text(ax, 72, 15, 'quotient : 1 élément', 'resultat', 's')
save(fig, '59-131')
