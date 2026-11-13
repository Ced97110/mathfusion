import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, ux, uy, x0, x1, y0, y1):
    arrow(ax, (ox + x0 * ux, oy), (ox + x1 * ux + 3, oy), "fixe", lw=0.8)
    arrow(ax, (ox, oy + y0 * uy), (ox, oy + y1 * uy + 3), "fixe", lw=0.8)
    return lambda x, y: (ox + x * ux, oy + y * uy)
fig, ax = canvas(60); P = plane(ax, 12, 8, 8, 8, 0, 5, 0, 5)
line(ax, [P(4, -0.3), P(4, 5.2)], 'sujet', lw=1.4)
for y in (0, 4):
    disc(ax, *P(4, y), 1.3, 'sujet')
    text(ax, P(4, y)[0] - 3, P(4, y)[1], f'(4, {y})', 'sujet', 's', ha='right')
text(ax, P(2.2, 5.4)[0], P(2.2, 5.4)[1], 'la droite existe', 'sujet', 's')
text(ax, 66, 46, 'montée −4', 'varie', 'm'); text(ax, 66, 38, 'avancée 0', 'varie', 'm')
text(ax, 66, 27, r'$-4 \div 0$', 'limite', 'l', weight='bold')
text(ax, 66, 19, 'aucun nombre', 'limite', 's'); text(ax, 66, 14, 'ne convient', 'limite', 's')
save(fig, '19-119')
