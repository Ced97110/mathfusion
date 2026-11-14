import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ox, oy, u = 12, 8, 7
P = lambda a, b: (ox + a * u, oy + b * u)
arrow(ax, (ox, oy), (52, oy), 'fixe', lw=0.8); arrow(ax, (ox, oy), (ox, 58), 'fixe', lw=0.8)
arrow(ax, P(0, 0), P(1, 2), 'sujet', lw=1.3); arrow(ax, P(1, 2), P(4, 6), 'autre', lw=1.3); arrow(ax, P(0, 0), P(4, 6), 'resultat', lw=1.5)
text(ax, P(1, 2)[0] - 1.5, P(1, 2)[1] - 1, '(1, 2)', 'sujet', ha='right'); text(ax, P(3, 4)[0] + 2.5, P(3, 4)[1] - 1, '(3, 4)', 'autre', ha='left')
text(ax, P(4, 6)[0] + 2.5, P(4, 6)[1], '(4, 6)', 'resultat', ha='left'); text(ax, ox, 4, '(0, 0)', 'fixe', 's')
text(ax, 70, 36, 'case par case', 'encre', 's'); text(ax, 70, 28, '1 + 3 = 4', 'resultat'); text(ax, 70, 20, '2 + 4 = 6', 'resultat')
save(fig, '45-167')
