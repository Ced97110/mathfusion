import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
s = 7.0; ox, oy = 28.0, 30.0
P = lambda x, y: (ox + s * x, oy + s * y)
v = (3, 1)
line(ax, [P(-3, -1), P(5, 5 / 3)], 'fixe', lw=0.4, dash=True)
for a in (-1, 1, 2):
    disc(ax, *P(a * v[0], a * v[1]), 1.0, 'varie')
disc(ax, *P(0, 0), 1.5, 'resultat')
arrow(ax, P(0, 0), P(*v), 'sujet', lw=1.5)
text(ax, P(3, 1)[0] + 1, P(3, 1)[1] - 5, r'$1\times(3,\,1)$', 'sujet', 's')
text(ax, P(-3, -1)[0] + 1, P(-3, -1)[1] - 5, r'$-1\times$', 'varie', 's')
text(ax, P(6, 2)[0] - 2, P(6, 2)[1] + 5, r'$2\times$', 'varie', 's')
text(ax, P(0, 0)[0] + 2, P(0, 0)[1] - 6, r'$0\times(3,\,1)=(0,\,0)$', 'resultat', 's', ha='left')
text(ax, 44, 64, r'multiples de $(3,\,1)$', 'fixe', 's')
text(ax, 44, 8, r'$3\times$ nombre $=0$ : seul le nombre $0$ convient', 'resultat', 's')
save(fig, '58-160')
