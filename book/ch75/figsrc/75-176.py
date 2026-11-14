import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
ox, oy, u = 44, 12, 22
P = lambda x, y: (ox + x*u, oy + y*u)
poly(ax, [P(0, 0), P(1, 0), P(1, 1), P(0, 1)], 'sujet')
poly(ax, [P(0, 0), P(0, 1), P(-1, 1), P(-1, 0)], 'resultat')
arrow(ax, P(.85, .85), P(-.85, .85), 'varie', curve=0.6)
text(ax, P(.5, .5)[0], P(.5, .5)[1], 'aire 1', 'sujet', 'm', weight='bold')
text(ax, P(-.5, .5)[0], P(-.5, .5)[1], 'aire 1', 'resultat', 'm', weight='bold')
text(ax, ox, P(0, 1.55)[1]+3, r'quart de tour $\eta$', 'varie', 's')
text(ax, ox, 4, r'$\det\eta=1$ : volume conservé', 'resultat', 's', weight='bold')
text(ax, ox+11, oy-3, 'avant', 'sujet', 's'); text(ax, ox-11, oy-3, 'après', 'resultat', 's')
save(fig, '75-176')
