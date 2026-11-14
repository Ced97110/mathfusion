import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
# deux directions non alignées u, v : chaque point reçoit un couple (a, b) pour a u + b v
x0, y0, u = 8, 6, 7.4
P = lambda a, b: (x0 + a * u, y0 + b * u)
W = lambda a, b: (2 * a + b, a + 2 * b)       # point a u + b v dans le quadrillage
lat = [(a, b) for a in range(0, 4) for b in range(0, 4) if 2 * a + b <= 7 and a + 2 * b <= 5]
for (a, b) in lat:
    disc(ax, *P(*W(a, b)), 0.9, 'fixe')
arrow(ax, P(0, 0), P(2, 1), 'sujet', lw=2.0)
arrow(ax, P(0, 0), P(1, 2), 'autre', lw=2.0)
disc(ax, *P(*W(2, 1)), 1.8, 'resultat')
disc(ax, *P(*W(1, 1)), 1.8, 'resultat')
text(ax, P(1, 0.5)[0] + 2.0, P(1, 0.5)[1] - 3.2, r'$u$', 'sujet', 'm', weight='bold')
text(ax, P(0.5, 1)[0] - 2.4, P(0.5, 1)[1] + 1.2, r'$v$', 'autre', 'm', weight='bold')
text(ax, P(5, 4)[0] + 3.0, P(5, 4)[1] + 0.8, '2 et 1', 'resultat', 's', ha='left', weight='bold')
text(ax, P(3, 3)[0] - 3.0, P(3, 3)[1] + 3.5, '1 et 1', 'resultat', 's', ha='right', weight='bold')
text(ax, 72, 14, 'un seul couple\npar point', 'resultat', 's', ha='center')
save(fig, '58-029')
