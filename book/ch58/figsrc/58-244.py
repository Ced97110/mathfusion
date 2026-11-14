import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy, u = 14, 14, 11
P = lambda a, b: (ox + a * u, oy + b * u)
arrow(ax, P(-0.4, 0), P(6.2, 0), 'sujet', lw=1.2)
arrow(ax, P(0, -0.4), P(0, 5.0), 'autre', lw=1.2)
text(ax, 78, oy + 3.2, 'riz pur', 'sujet', 's')
text(ax, 22, 69, 'lentilles pur', 'autre', 's')
# (5, 4) = (5, 0) + (0, 4) : rectangle de pointillés
line(ax, [P(5, 0), P(5, 4)], 'resultat', dash=True)
line(ax, [P(0, 4), P(5, 4)], 'resultat', dash=True)
disc(ax, *P(5, 0), 1.5, 'sujet')
disc(ax, *P(0, 4), 1.5, 'autre')
disc(ax, *P(5, 4), 1.7, 'resultat')
text(ax, P(5, 0)[0], P(5, 0)[1] - 5, '(5, 0)', 'sujet', 's')
text(ax, P(0, 4)[0] + 2, P(0, 4)[1] + 5, '(0, 4)', 'autre', 's')
text(ax, P(5, 4)[0], P(5, 4)[1] + 5, '(5, 4)', 'resultat', 's', weight='bold')
text(ax, 44, 4, '(5, 4) = (5, 0) + (0, 4)', 'resultat', 'm', weight='bold')
save(fig, '58-244')
