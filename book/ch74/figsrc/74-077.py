import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
ox, oy, u = 26, 8, 8
g = lambda a, b: (ox + a*u, oy + b*u)
for i in range(-3, 4):
    for j in range(5): disc(ax, *g(i, j), 0.6, 'fixe')
arrow(ax, g(0, 0), g(-2, 2), 'sujet', lw=1.3); arrow(ax, g(0, 0), g(3, 3), 'autre', lw=1.3)
disc(ax, *g(-2, 2), 1.4, 'sujet'); disc(ax, *g(3, 3), 1.4, 'autre')
text(ax, g(-2, 2)[0] + 2, g(-2, 2)[1] + 5, r'$Ac+b=(-2\,;\,2)$', 'sujet', 's')
text(ax, g(3, 3)[0] - 2, g(3, 3)[1] + 5, r'$b+c=(3\,;\,3)$', 'autre', 's')
box(ax, 58, 22, 28, 8, 'resultat', label=r'$f \mapsto A$ : oui', size='s')
box(ax, 58, 10, 28, 8, 'limite', label=r'$f \mapsto b$ : non', size='s')
save(fig, '74-077')
