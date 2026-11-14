import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
# changer le nombre devant u glisse le long de la droite de u ; une seule parallèle à v passe par w
x0, y0, u = 8, 8, 8.0
P = lambda a, b: (x0 + a * u, y0 + b * u)
for a in range(0, 8):
    line(ax, [P(a, 0), P(a, 5)], 'fixe', lw=0.2)
for b in range(0, 6):
    line(ax, [P(0, b), P(7, b)], 'fixe', lw=0.2)
line(ax, [P(0, 0), P(7, 3.5)], 'sujet', lw=1.0)
# parallèles à v = (1, 2) menées de u, 2u, 3u jusqu'en haut du quadrillage
for k, role in [(1, 'limite'), (2, 'resultat'), (3, 'limite')]:
    bx, by = 2 * k, k
    t = (5 - by) / 2
    line(ax, [P(bx, by), P(bx + t, 5)], role, lw=1.6 if k == 2 else 1.0, dash=(k != 2))
    disc(ax, *P(bx, by), 1.3, 'sujet')
text(ax, P(2, 1)[0] + 1.5, P(2, 1)[1] - 3.2, r'$u$', 'sujet', 's', weight='bold')
text(ax, P(4, 2)[0] + 1.5, P(4, 2)[1] - 3.2, r'$2u$', 'sujet', 's', weight='bold')
text(ax, P(6, 3)[0] + 1.5, P(6, 3)[1] - 3.2, r'$3u$', 'sujet', 's', weight='bold')
disc(ax, *P(5, 4), 1.7, 'resultat')
text(ax, P(5, 4)[0] + 3.2, P(5, 4)[1] + 1.5, r'$w$', 'resultat', 'm', weight='bold', ha='left')
arrow(ax, P(0, 0), P(1, 2), 'autre', lw=1.8)
text(ax, P(1, 2)[0] - 2.2, P(1, 2)[1] + 1.5, r'$v$', 'autre', 'm', weight='bold')
text(ax, 77, 40, 'une seule\nparallèle à $v$\npasse par $w$', 'resultat', 's', weight='bold')
text(ax, 77, 20, 'les autres\nratent $w$', 'limite', 's')
save(fig, '58-028')
