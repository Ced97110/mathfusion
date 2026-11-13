import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy, u = 30, 6, 5.0
P = lambda a, b: (ox + a * u, oy + b * u)
arrow(ax, (ox - 6 * u, oy), (ox + 4 * u, oy), 'fixe', lw=0.6)
arrow(ax, (ox, oy), (ox, oy + 11.5 * u), 'fixe', lw=0.6)
for (a, b), role in [((1, 2), 'sujet'), ((3, 4), 'autre'), ((-5, 10), 'resultat')]:
    arrow(ax, (ox, oy), P(a, b), role, lw=1.0)
    disc(ax, *P(a, b), 1.2, role)
text(ax, P(1, 2)[0] + 2.5, P(1, 2)[1] - 1, r'$z$', 'sujet', 's', ha='left')
text(ax, P(3, 4)[0] + 2.5, P(3, 4)[1], r'$w$', 'autre', 's', ha='left')
text(ax, P(-5, 10)[0] + 3, P(-5, 10)[1] + 2.5, r'$zw=-5+10i$', 'resultat', 's', ha='left')
text(ax, P(1, 2)[0] - 8, P(1, 2)[1] + 3, r'$1+2i$', 'sujet', 's')
text(ax, P(3, 4)[0] + 2.5, P(3, 4)[1] - 4, r'$3+4i$', 'autre', 's', ha='left')
X = 52
text(ax, X, 56, r'$1^2+2^2=5$', 'sujet', ha='left')
text(ax, X, 47, r'$3^2+4^2=25$', 'autre', ha='left')
text(ax, X, 38, r'$5\times25=125$', 'fixe', ha='left')
text(ax, X, 26, r'$(-5)^2+10^2$', 'resultat', ha='left')
text(ax, X, 18, r'$=25+100=125$', 'resultat', ha='left')
save(fig, '39-143')
