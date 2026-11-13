import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ox, oy, u = 4, 14, 11
P = lambda a, b: (ox + a * u, oy + b * u)
poly(ax, [P(0, 0), P(2, 1), P(3, 2), P(1, 1)], 'resultat')
arrow(ax, P(0, 0), P(2, 1), 'varie', lw=1.3); arrow(ax, P(0, 0), P(1, 1), 'autre', lw=1.3)
text(ax, 4, 8, '$(a,\\ b)$ = (2, 1)', 'varie', 's', ha='left'); text(ax, 4, 46, '$(c,\\ d)$ = (1, 1)', 'autre', 's', ha='left')
text(ax, P(2.2, 0.55)[0], P(2.2, 0.55)[1], 'aire 1', 'resultat', 's', ha='left')
box(ax, 46, 48, 38, 10, 'sujet', label=r'$ad$ = 2 × 1 = 2'); text(ax, 65, 44.5, '−', 'encre', 'l')
box(ax, 46, 30, 38, 10, 'varie', label=r'$bc$ = 1 × 1 = 1')
arrow(ax, (65, 30), (65, 24), 'encre'); box(ax, 46, 12, 38, 10, 'resultat', label=r'$ad - bc$ = 2 − 1 = 1')
save(fig, '75-015')
