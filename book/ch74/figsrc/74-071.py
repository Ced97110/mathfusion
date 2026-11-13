import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ox, oy, u = 22, 8, 11
g = lambda a, b: (ox + a*u, oy + b*u)
for i in range(-1, 6):
    for j in range(5): disc(ax, *g(i, j), 0.8, 'sujet')
arrow(ax, g(0, 0), g(1, 0), 'varie', lw=1.3); arrow(ax, g(0, 0), g(0, 1), 'varie', lw=1.3)
text(ax, g(0.5, 0)[0], g(0.5, 0)[1] + 3.8, '$x$', 'varie', 'm')
text(ax, g(0, 0.5)[0] - 3.5, g(0.5, 0.5)[1] - 1.5, '$y$', 'varie', 'm')
disc(ax, *g(3, 2), 1.6, 'resultat'); text(ax, g(3, 2)[0], g(3, 2)[1] + 4.5, '(3 ; 2)', 'resultat', 's')
disc(ax, *g(-1, 4), 1.6, 'resultat'); text(ax, g(-1, 4)[0] + 8, g(-1, 4)[1] + 4, '(−1 ; 4)', 'resultat', 's')
disc(ax, *g(0.5, 0), 1.3, 'limite', fill=False, lw=1.0)
text(ax, g(0.5, 0)[0] + 4, 3.8, '(0,5 ; 0) : hors de $L$', 'limite', 's', ha='left')
text(ax, 84, 57, '$L$ : points isolés', 'sujet', 'm', ha='right')
save(fig, '74-071')
