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

fig, ax = canvas(62)
rows = [('sujet', r'$y = 2x + 1$', '2 lettres : un couple', 46), ('autre', r'$2x + 1 = 7$', '1 lettre : le nombre 3', 28), ('fixe', r'$2x + 1$', "pas d'égalité", 10)]
for role, eq, desc, y in rows:
    box(ax, 3, y, 34, 13, role, label=eq, size='l')
    arrow(ax, (38, y + 6.5), (44, y + 6.5), role)
    text(ax, 46, y + 6.5, desc, role, 'm', ha='left')
save(fig, '19-033')
