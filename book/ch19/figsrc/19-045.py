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

fig, ax = canvas(66)
def stairs(P, pts, labels, role):
    for (a, b), (c, d), lab in zip(pts, pts[1:], labels):
        line(ax, [P(a, b), P(c, b)], 'fixe', lw=0.9); line(ax, [P(c, b), P(c, d)], 'varie', lw=1.4)
        text(ax, P(c, (b + d) / 2)[0] + 2, P(c, (b + d) / 2)[1], lab, 'varie', 's', ha='left')
    line(ax, [P(*p) for p in pts], role, lw=1.0)
    for p in pts: disc(ax, *P(*p), 1.1, role)
L = plane(ax, 17, 19, 7, 7, -1.3, 2.6, -1.3, 5.6, ticks=False)
stairs(L, [(-1, -1), (0, 1), (1, 3), (2, 5)], ['+2', '+2', '+2'], 'resultat')
R = plane(ax, 54, 19, 7, 7, -0.3, 2.6, -0.3, 4.6, ticks=False)
stairs(R, [(0, 0), (1, 1), (2, 4)], ['+1', '+3'], 'limite')
text(ax, 24, 62, 'alignés : montée +2', 'resultat', 's'); text(ax, 62, 62, 'pas alignés : +1, +3', 'limite', 's')
save(fig, '19-045')
