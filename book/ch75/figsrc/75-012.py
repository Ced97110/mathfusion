import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
ox, oy, u = 14, 8, 20
P = lambda a, b: (ox + a * u, oy + b * u)
poly(ax, [P(0, 0), P(2, 1), P(3, 2), P(1, 1)], 'varie')
poly(ax, [P(0, 0), P(1, 0), P(1, 1), P(0, 1)], 'sujet')
arrow(ax, P(0, 0), P(1, 0), 'sujet', lw=1.3); arrow(ax, P(0, 0), P(0, 1), 'sujet', lw=1.3)
arrow(ax, P(0, 0), P(2, 1), 'varie', lw=1.3); arrow(ax, P(0, 0), P(1, 1), 'varie', lw=1.3)
text(ax, *P(0.5, -0.25), r'$e$', 'sujet', 'm'); text(ax, *P(-0.25, 0.5), r'$f$', 'sujet', 'm')
text(ax, *P(1.8, 0.45), r'$\eta e$', 'varie', 'm'); text(ax, *P(0.75, 1.3), r'$\eta f$', 'varie', 'm')
text(ax, *P(1.6, 0.2), 'carré : aire 1', 'sujet', 's', ha='left')
text(ax, *P(2.35, 1.55), 'aire 1', 'varie', 's', ha='left')
save(fig, '75-012')
