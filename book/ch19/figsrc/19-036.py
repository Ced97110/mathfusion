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

fig, ax = canvas(80)
box(ax, 30, 66, 28, 11, 'sujet', label='(5, 2)', size='l')
arrow(ax, (36, 66), (23, 54), 'sujet'); arrow(ax, (52, 66), (65, 54), 'sujet')
text(ax, 17, 61, r'$y = 2$', 'sujet', 's'); text(ax, 71, 61, r'$x = 5$', 'sujet', 's')
box(ax, 6, 40, 34, 13, 'autre', label='2', size='l'); box(ax, 48, 40, 34, 13, 'varie', label=r'$2 \times 5 + 1 = 11$', size='m')
text(ax, 44, 46, r'$\neq$', 'limite', 'l')
text(ax, 23, 35, 'côté gauche', 'autre', 's'); text(ax, 65, 35, 'côté droit', 'varie', 's')
arrow(ax, (44, 38), (44, 27), 'limite')
box(ax, 14, 12, 60, 14, 'limite', label=r'$2 \neq 11$ : faux', size='l')
save(fig, '19-036')
