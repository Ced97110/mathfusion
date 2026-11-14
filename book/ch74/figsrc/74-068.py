import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
ox, oy, u = 14, 10, 14
g = lambda a, b: (ox + a*u, oy + b*u)
for i in range(5): line(ax, [g(i, 0), g(i, 3)], 'fixe', lw=0.3)
for j in range(4): line(ax, [g(0, j), g(4, j)], 'fixe', lw=0.3)
pts = [(3, 1), (2, 2), (1, 1), (2, 0)]
line(ax, [g(*p) for p in pts] + [g(*pts[0])], 'sujet', lw=0.7, dash=True)
for p in pts: disc(ax, *g(*p), 1.3, 'sujet')
text(ax, g(3, 1)[0] + 3, g(3, 1)[1], '$P$ = (3 ; 1)', 'sujet', 's', ha='left')
text(ax, g(2, 2)[0], g(2, 2)[1] + 4, '(2 ; 2)', 'sujet', 's')
text(ax, g(1, 1)[0] - 3, g(1, 1)[1], '(1 ; 1)', 'sujet', 's', ha='right')
text(ax, g(2, 0)[0], g(2, 0)[1] - 4, '(2 ; 0)', 'sujet', 's')
disc(ax, *g(2, 1), 1.7, 'resultat')
text(ax, g(2, 1)[0] + 3, g(2, 1)[1], '(2 ; 1)', 'resultat', 's', ha='left')
text(ax, 3, 53, '4 images de $P$', 'sujet', 'm', ha='left')
text(ax, 85, 53, 'centre de gravité', 'resultat', 'm', ha='right')
save(fig, '74-068')
