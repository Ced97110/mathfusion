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
text(ax, 44, 66, r'$y = 2x + 1$', 'sujet', 'l')
for i, (a, b) in enumerate([(-1, -1), (0, 1), (1, 3), (2, 5)]):
    c = 14 + 20 * i
    box(ax, c - 8.5, 44, 17, 10, 'varie', label=f'$x = {a}$'.replace('-', '\u2212'))
    arrow(ax, (c, 44), (c, 35), 'sujet')
    box(ax, c - 8.5, 25, 17, 10, 'resultat', label=f'$y = {b}$'.replace('-', '\u2212'))
    text(ax, c, 16, f'$({a},\\,{b})$'.replace('-', '\u2212'), 'sujet', 'm')
save(fig, '19-043')
