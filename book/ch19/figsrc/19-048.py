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

fig, ax = canvas(60)
def stairs(P, pts, labels, role):
    for (a, b), (c, d), lab in zip(pts, pts[1:], labels):
        line(ax, [P(a, b), P(c, b)], 'fixe', lw=0.9); line(ax, [P(c, b), P(c, d)], 'varie', lw=1.4)
        text(ax, P(c, (b + d) / 2)[0] + 1.5, P(c, (b + d) / 2)[1], lab, 'varie', 's', ha='left')
    for p in pts: disc(ax, *P(*p), 1.0, role)
L = plane(ax, 7, 8, 10, 4.4, -0.2, 3.4, -0.2, 9.8, ticks=False)
line(ax, [L(0, 0), L(3, 6)], 'autre', lw=1.1); stairs(L, [(0, 0), (1, 2), (2, 4), (3, 6)], ['+2', '+2', '+2'], 'autre')
R = plane(ax, 50, 8, 10, 4.4, -0.2, 3.4, -0.2, 9.8, ticks=False)
xs = [i / 20 * 3 for i in range(21)]
ax.plot([R(x, x * x)[0] for x in xs], [R(x, x * x)[1] for x in xs], color=COL['sujet'], lw=1.2, zorder=3)
stairs(R, [(0, 0), (1, 1), (2, 4), (3, 9)], ['+1', '+3', '+5'], 'sujet')
text(ax, 22, 56, 'même montée : +2, +2, +2', 'autre', 's'); text(ax, 66, 56, 'la montée change', 'sujet', 's')
save(fig, '19-048')
