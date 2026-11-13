import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
s = 6.0; ox, oy = 34.0, 24.0
P = lambda x, y: (ox + s * x, oy + s * y)
u, v = (3, 1), (1, 2)
node = lambda a, b: P(a * u[0] + b * v[0], a * u[1] + b * v[1])
# quadrillage : parallèles à u (bleu) et à v (orange), croisements = points entiers
for b in range(-1, 3):
    line(ax, [node(-1, b), node(1, b)], 'sujet', lw=0.35)
for a in range(-1, 2):
    line(ax, [node(a, -1), node(a, 2)], 'varie', lw=0.35)
for a in range(-1, 2):
    for b in range(-1, 3):
        disc(ax, *node(a, b), 0.55, 'fixe')
# chemin : -u puis 2v
arrow(ax, P(0, 0), node(-1, 0), 'sujet', lw=1.0)
arrow(ax, node(-1, 0), node(-1, 2), 'varie', lw=1.0)
# flèches de l'énoncé
arrow(ax, P(0, 0), P(*u), 'sujet', lw=1.5)
arrow(ax, P(0, 0), P(*v), 'varie', lw=1.5)
arrow(ax, P(0, 0), P(-1, 3), 'autre', lw=1.5)
disc(ax, *P(-1, 3), 1.1, 'autre')
text(ax, P(3, 1)[0] + 4, P(3, 1)[1] - 2, r'$u$', 'sujet', 'l')
text(ax, P(1, 2)[0] + 3.5, P(1, 2)[1] + 0.5, r'$v$', 'varie', 'l')
text(ax, P(-1, 3)[0] - 4, P(-1, 3)[1] + 1, r'$w$', 'autre', 'l')
text(ax, node(-1, 0)[0] - 1, node(-1, 0)[1] - 3.5, r'$-u$', 'sujet', 'm')
text(ax, node(-1, 1)[0] - 5, node(-1, 1)[1] + 1, r'$2v$', 'varie', 'm')
text(ax, 32, 68, r'$w=-u+2v$', 'autre', 'l')
text(ax, 32, 61, 'w est un croisement', 'fixe', 's')
save(fig, '58-154')
