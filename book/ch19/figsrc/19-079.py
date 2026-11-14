import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
o = (30, 34); ux, uy = 16, 7
P = lambda x, y: (o[0] + x * ux, o[1] + y * uy)
line(ax, [P(-0.6, -1.2), P(1.5, 3)], 'sujet', lw=1.5); line(ax, [P(-0.6, 1.8), P(1.5, -4.5)], 'autre', lw=1.5)
arrow(ax, P(0, 0), P(1, 0), 'fixe', lw=1.0); text(ax, P(0.5, 0)[0], 30.5, 'pas 1', 'fixe', 's')
arrow(ax, P(1, 0), P(1, 2), 'varie', lw=1.2); arrow(ax, P(1, 0), P(1, -3), 'varie', lw=1.2)
text(ax, 49, 41, 'monte 2', 'varie', 's', ha='left'); text(ax, 49, 22, 'descend 3', 'varie', 's', ha='left')
text(ax, 72, 54, r'$m=2$', 'sujet', 'm'); text(ax, 72, 47, r'$|m|=2$', 'sujet', 'm')
text(ax, 72, 26, r'$m=-3$', 'autre', 'm'); text(ax, 72, 19, r'$|m|=3$', 'autre', 'm')
text(ax, 72, 8, '3 > 2 : plus raide', 'resultat', 's', weight='bold')
save(fig, '19-079')
