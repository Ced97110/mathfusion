import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ox, oy, u = 28, 16, 10
P = lambda a, b: (ox + a * u, oy + b * u)
arrow(ax, P(-2.6, 0), P(4.4, 0), 'sujet', lw=1.2)
arrow(ax, P(-0.5, -0.5), P(3.9, 3.9), 'varie', lw=1.2)
text(ax, P(4.4, 0)[0] - 1, P(4.4, 0)[1] - 3.5, 'X', 'sujet', 'm', weight='bold')
text(ax, P(3.9, 3.9)[0] + 3, P(3.9, 3.9)[1] + 1, 'Z', 'varie', 'm', weight='bold')
# parallélogramme : O -> x -> P -> z -> O
line(ax, [P(-2, 0), P(1, 3)], 'resultat', dash=True)
line(ax, [P(3, 3), P(1, 3)], 'resultat', dash=True)
arrow(ax, P(0, 0), P(-1.9, 0), 'sujet', lw=1.6)
arrow(ax, P(0, 0), P(2.9, 2.9), 'autre', lw=1.6)
disc(ax, *P(-2, 0), 1.3, 'sujet'); disc(ax, *P(3, 3), 1.3, 'autre'); disc(ax, *P(1, 3), 1.6, 'resultat')
text(ax, P(-2, 0)[0], P(-2, 0)[1] - 4, '(−2, 0)', 'sujet', 's')
text(ax, P(3, 3)[0] + 3.5, P(3, 3)[1] - 3.5, '(3, 3)', 'autre', 's')
text(ax, P(1, 3)[0] - 3, P(1, 3)[1] + 3.5, '(1, 3) = P', 'resultat', 's', weight='bold')
text(ax, 44, 4, 'un seul parallélogramme', 'resultat', 's')
save(fig, '58-257')
