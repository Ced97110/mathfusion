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

fig, ax = canvas(76)
text(ax, 44, 69, '(a, b)', 'sujet', 'xl', weight='bold')
arrow(ax, (40, 65), (22, 56), 'sujet'); arrow(ax, (48, 65), (66, 56), 'sujet')
box(ax, 4, 44, 36, 11, 'sujet', label=r'1er : $x = a$'); box(ax, 48, 44, 36, 11, 'sujet', label=r'2e : $y = b$')
text(ax, 44, 49.5, 'puis', 'fixe', 's')
for (a, b, y) in [(2, 5, 31), (0, 1, 17)]:
    text(ax, 9, y, f'({a}, {b})', 'fixe', 'm')
    text(ax, 26, y, f'$a = {a}$', 'sujet', 'm'); text(ax, 70, y, f'$b = {b}$', 'sujet', 'm')
    arrow(ax, (33, y), (21, y), 'fixe') if False else None
save(fig, '19-039')
