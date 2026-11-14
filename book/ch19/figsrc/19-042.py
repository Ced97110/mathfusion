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
P = plane(ax, 24, 14, 12, 12, -0.3, 4.2, -0.3, 3.4)
x, y = P(3, 2)
line(ax, [(x, y), (x, 14)], 'fixe', dash=True); line(ax, [(x, y), (24, y)], 'fixe', dash=True)
disc(ax, x, 14, 1.5, 'varie'); disc(ax, 24, y, 1.5, 'varie'); disc(ax, x, y, 1.8, 'sujet')
text(ax, x, 7.5, '1re fois : 3', 'varie', 's'); text(ax, 20.5, y, '2e fois : 2', 'varie', 's', ha='right')
text(ax, x + 3, y + 3, 'P', 'sujet', 'l', weight='bold')
text(ax, 44, 62, 'même geste : nombre \u2192 point', 'encre', 's')
text(ax, 78, 14, r'$x$', 'fixe', 'l'); text(ax, 24, 57, r'$y$', 'fixe', 'l')
save(fig, '19-042')
