import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ox, oy, dx, dy = 10, 44, 8, 7
P = lambda a, b: (ox + a * dx, oy + b * dy)
for a in range(9):
    for b in range(5):
        disc(ax, *P(a, b), 0.6, 'fixe')
arrow(ax, P(0, 0), P(2, 1), 'varie', lw=1.3)
arrow(ax, P(2, 1), P(4, 2), 'varie', lw=1.3)
for a, b in ((0, 0), (4, 2), (8, 4)):
    disc(ax, *P(a, b), 1.8, 'sujet')
disc(ax, *P(2, 1), 1.8, 'varie')
text(ax, P(0, 0)[0], P(0, 0)[1] - 4.5, '(0 ; 0)', 'sujet', 's')
text(ax, P(2, 1)[0] - 4, P(2, 1)[1] + 3.5, 'u = (2 ; 1)', 'varie', 's')
text(ax, P(4, 2)[0] + 7, P(4, 2)[1] - 4, '(4 ; 2)', 'sujet', 's')
text(ax, 44, 34, 'N″ = multiples de (4 ; 2)', 'sujet', 'm')
text(ax, 44, 27, "(2 ; 1) n'est pas dans N″", 'varie', 'm')
text(ax, 44, 20, 'son double (4 ; 2) y est', 'resultat', 'm')
text(ax, 44, 11, "qu'est-ce qui décide ?", 'encre', 'm', weight='bold')
save(fig, '57-227')
