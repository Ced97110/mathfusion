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
text(ax, 3, 61, 'Une lettre : un nombre', 'autre', 'm', ha='left')
box(ax, 3, 44, 14, 12, 'autre', label='3', size='l')
text(ax, 3, 36, 'Deux lettres : un couple', 'sujet', 'm', ha='left')
text(ax, 11, 21, '(', 'sujet', 'xl'); text(ax, 73, 21, ')', 'sujet', 'xl'); text(ax, 42, 18.5, ',', 'sujet', 'xl')
box(ax, 15, 15, 22, 12, 'sujet', label='2', size='l'); box(ax, 47, 15, 22, 12, 'sujet', label='5', size='l')
text(ax, 26, 9, r'$a$ remplace $x$', 'sujet', 's'); text(ax, 58, 9, r'$b$ remplace $y$', 'sujet', 's')
save(fig, '19-034')
