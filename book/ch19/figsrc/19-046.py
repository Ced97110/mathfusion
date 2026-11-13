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

fig, ax = canvas(54)
s = 4.2; x0 = 8
def bar(y, roles):
    for i, r in enumerate(roles): box(ax, x0 + i * s, y, s, s, r, r=0.3, lw=0.5)
bar(40, ['sujet'] * 14 + ['fixe']); bar(16, ['sujet'] * 14 + ['varie'] * 2 + ['fixe'])
text(ax, x0, 47.5, 'x = 7 : y = 15', 'encre', 'm', ha='left'); text(ax, x0, 23.5, 'x = 8 : y = 17', 'encre', 'm', ha='left')
brace(ax, x0, x0 + 14 * s, 40, 'sujet', r'$2x = 14$'); brace(ax, x0 + 14 * s, x0 + 15 * s, 40, 'fixe', '+1')
brace(ax, x0 + 14 * s, x0 + 16 * s, 16, 'varie', '+2'); brace(ax, x0 + 16 * s, x0 + 17 * s, 16, 'fixe', '+1')
text(ax, 44, 28, r'$x$ augmente de 1', 'varie', 'm')
save(fig, '19-046')
