import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
O = (36, 6); u = 7
P = lambda a, b: (O[0] + a * u, O[1] + b * u)
arrow(ax, (3, 6), (60, 6), 'fixe', lw=0.7); arrow(ax, (36, 6), (36, 63), 'fixe', lw=0.7)
line(ax, [P(-4, 7), P(-4, 0)], 'resultat', dash=True); line(ax, [P(-4, 7), P(0, 7)], 'resultat', dash=True)
arrow(ax, O, P(1, 2), 'sujet', lw=1.3); arrow(ax, O, P(2, 3), 'autre', lw=1.3); arrow(ax, O, P(-4, 7), 'resultat', lw=1.3)
text(ax, 47, 18, '$z$', 'sujet'); text(ax, 54, 28, '$w$', 'autre'); text(ax, 8, 59.5, '$zw$', 'resultat')
text(ax, 8, 2.5, '−4', 'resultat', 's'); text(ax, 32.5, 55, '7', 'resultat', 's')
text(ax, 73, 45, r'$|z|^2=5$', 'sujet'); text(ax, 73, 35, r'$|w|^2=13$', 'autre'); text(ax, 73, 25, r'$|zw|^2=65$', 'resultat')
save(fig, '78-077')
