import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
# parallélogramme O, 2u, w, v : côtés opposés parallèles et égaux
x0, y0, u = 8, 9, 7.6
P = lambda a, b: (x0 + a * u, y0 + b * u)
for a in range(0, 7):
    line(ax, [P(a, 0), P(a, 5)], 'fixe', lw=0.2)
for b in range(0, 6):
    line(ax, [P(0, b), P(6, b)], 'fixe', lw=0.2)
poly(ax, [P(0, 0), P(4, 2), P(5, 4), P(1, 2)], 'resultat', fill=True, lw=0.6)
arrow(ax, P(0, 0), P(4, 2), 'sujet', lw=1.8)
arrow(ax, P(1, 2), P(5, 4), 'sujet', lw=1.8)
arrow(ax, P(0, 0), P(1, 2), 'autre', lw=1.8)
arrow(ax, P(4, 2), P(5, 4), 'autre', lw=1.8)
for p in [(0, 0), (4, 2), (5, 4), (1, 2)]:
    disc(ax, *P(*p), 1.2, 'encre')
text(ax, P(0, 0)[0] - 2.5, P(0, 0)[1] - 2.5, 'O', 'encre', 's')
text(ax, P(4, 2)[0] + 1.5, P(4, 2)[1] - 3.2, r'$2u$', 'sujet', 'm', weight='bold')
text(ax, P(5, 4)[0] + 3.0, P(5, 4)[1] + 2.2, r'$w$', 'resultat', 'm', weight='bold')
text(ax, P(1, 2)[0] - 2.5, P(1, 2)[1] + 2.5, r'$v$', 'autre', 'm', weight='bold')
text(ax, 70, 38, r'$w = 2u + v$', 'encre', 'm', weight='bold')
text(ax, 70, 31, 'côtés opposés', 'fixe', 's')
text(ax, 70, 26.5, 'parallèles', 'fixe', 's')
save(fig, '58-027')
