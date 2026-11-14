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
P = plane(ax, 14, 14, 16, 10, -0.3, 3.2, -0.3, 5.3, rx='sujet', ticks=False)
for a, b in [(0, 1), (1, 3), (2, 5)]:
    x, y = P(a, b)
    line(ax, [(x, y), (x, P(a, 0)[1])], 'fixe', dash=True)
    disc(ax, x, y, 1.3, 'fixe'); disc(ax, x, P(a, 0)[1], 1.3, 'sujet')
    text(ax, x + 3, y + 1.5, f'({a}, {b})', 'fixe', 's', ha='left')
    text(ax, x, 9, str(a), 'sujet', 'm', weight='bold')
text(ax, 76, 14, r'$x$', 'sujet', 'l'); text(ax, 14, 71, r'$y$', 'fixe', 'l')
text(ax, 44, 2.5, 'premier nombre : $x$', 'sujet', 's')
save(fig, '19-037')
