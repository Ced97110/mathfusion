import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def plane(ax, ox, oy, ux, uy, x0, x1, y0, y1, rx='fixe', ry='fixe', ticks=True):
    arrow(ax, (ox + x0 * ux, oy), (ox + x1 * ux, oy), rx, lw=0.8)
    arrow(ax, (ox, oy + y0 * uy), (ox, oy + y1 * uy), ry, lw=0.8)
    if ticks:
        for i in range(math.ceil(x0), math.floor(x1) + 1):
            if i != 0: line(ax, [(ox + i * ux, oy - 0.9), (ox + i * ux, oy + 0.9)], rx, lw=0.6)
        for j in range(math.ceil(y0), math.floor(y1) + 1):
            if j != 0: line(ax, [(ox - 0.9, oy + j * uy), (ox + 0.9, oy + j * uy)], ry, lw=0.6)
    return lambda a, b: (ox + a * ux, oy + b * uy)

fig, ax = canvas(72)
P = plane(ax, 30, 10, 12, 12, -1.5, 3.0, -0.5, 4.6)
line(ax, [P(-0.5, 0), P(1.6, 4.2)], 'sujet', lw=1.2)
line(ax, [P(0, 1), P(1, 1)], 'resultat', lw=1.8); line(ax, [P(1, 1), P(1, 3)], 'varie', lw=1.8)
disc(ax, *P(0, 1), 1.5, 'autre'); disc(ax, *P(1, 3), 1.0, 'sujet')
text(ax, P(0.5, 1)[0], P(0.5, 1)[1] - 3.5, 'avance de 1', 'resultat', 's')
text(ax, P(1, 2)[0] + 2.5, P(1, 2)[1], 'monte de 2', 'varie', 's', ha='left')
text(ax, P(0.9, 3.6)[0], P(0.9, 3.6)[1], 'pente 2', 'sujet', 'm', ha='right')
text(ax, P(-0.2, 1.7)[0], P(-0.2, 1.7)[1], "coupe l'axe : 1", 'autre', 's', ha='right')
text(ax, 86, 10, r'$x$', 'fixe', 'm', ha='right'); text(ax, 30, 68, r'$y$', 'fixe', 'm')
save(fig, '19-044')
