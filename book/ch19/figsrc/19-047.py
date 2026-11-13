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

fig, ax = canvas(74)
P = plane(ax, 20, 8, 22, 8, -0.3, 2.9, -0.3, 7.6, ticks=False)
line(ax, [P(0, 1), P(2, 5)], 'resultat', lw=1.1)
line(ax, [P(1, 3), P(2, 7)], 'limite', dash=True)
for a, b in [(0, 1), (1, 3)]:
    line(ax, [P(a, b), P(a + 1, b)], 'fixe', lw=1.0); line(ax, [P(a + 1, b), P(a + 1, b + 2)], 'varie', lw=1.6)
    text(ax, P(a + 0.5, b)[0], P(a + 0.5, b)[1] - 3.5, '+1', 'fixe', 's'); text(ax, P(a + 1, b + 1)[0] + 2.5, P(a + 1, b + 1)[1], '+2', 'varie', 's', ha='left')
for p in [(0, 1), (1, 3), (2, 5)]: disc(ax, *P(*p), 1.2, 'sujet')
disc(ax, *P(2, 7), 1.2, 'limite', fill=False)
text(ax, P(1.7, 6.8)[0], P(1.7, 6.8)[1], 'si la montée était 4', 'limite', 's', ha='right')
text(ax, P(2.1, 5)[0], P(2.1, 5)[1], 'ligne droite', 'resultat', 's', ha='left')
save(fig, '19-047')
