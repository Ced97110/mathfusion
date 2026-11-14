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
P = plane(ax, 30, 20, 14, 14, -1.0, 3.4, -1.0, 3.4)
for i in (1, 2, 3):
    text(ax, P(i, 0)[0], 15.5, str(i), 'fixe', 's'); text(ax, 26.2, P(0, i)[1], str(i), 'fixe', 's', ha='right')
disc(ax, *P(0, 0), 1.8, 'sujet')
text(ax, 25.5, 15.5, r'$O$', 'sujet', 'l', weight='bold'); text(ax, 36, 25.5, '(0, 0)', 'sujet', 'm', ha='left')
text(ax, 56, 24.5, 'second nombre = 0', 'fixe', 's'); text(ax, 33, 62, 'premier nombre = 0', 'fixe', 's', ha='left')
save(fig, '19-040')
