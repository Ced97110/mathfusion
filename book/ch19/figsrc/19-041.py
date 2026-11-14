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
P = plane(ax, 14, 12, 14, 14, -0.3, 4.4, -0.3, 3.3, ticks=False)
x, y = P(3, 2)
line(ax, [(x, y), (x, 12)], 'resultat', dash=True); line(ax, [(x, y), (14, y)], 'resultat', dash=True)
line(ax, [(15.8, 13.8), (x - 1.8, 13.8)], 'varie', lw=1.6); arrow(ax, (x - 1.8, 13.8), (x - 1.8, y - 1.8), 'varie', lw=1.6)
disc(ax, x, y, 1.6, 'sujet'); disc(ax, x, 12, 1.2, 'resultat'); disc(ax, 14, y, 1.2, 'resultat')
text(ax, x, 7, '3', 'resultat', 'm', weight='bold'); text(ax, 9.5, y, '2', 'resultat', 'm', weight='bold')
text(ax, x + 3, y + 4, 'P (3, 2)', 'sujet', 'm', ha='left')
text(ax, 35, 18, 'avance de 3', 'varie', 's'); text(ax, x - 5, 26, 'monte de 2', 'varie', 's', ha='right')
text(ax, 22, 58, 'couple \u2192 point', 'varie', 's', ha='left'); text(ax, 22, 53, 'point \u2192 couple', 'resultat', 's', ha='left')
text(ax, 78, 12, r'$x$', 'fixe', 'l'); text(ax, 14, 62, r'$y$', 'fixe', 'l')
save(fig, '19-041')
