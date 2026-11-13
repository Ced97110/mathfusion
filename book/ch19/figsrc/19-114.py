import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, ux, uy, x0, x1, y0, y1):
    arrow(ax, (ox + x0 * ux, oy), (ox + x1 * ux + 3, oy), "fixe", lw=0.8)
    arrow(ax, (ox, oy + y0 * uy), (ox, oy + y1 * uy + 3), "fixe", lw=0.8)
    return lambda x, y: (ox + x * ux, oy + y * uy)
fig, ax = canvas(62); P = plane(ax, 12, 8, 10, 10, 0, 6, 0, 4)
line(ax, [P(0.3, 3), P(5.8, 3)], 'sujet', lw=1.4)
for x in (1, 5):
    disc(ax, *P(x, 3), 1.3, 'sujet')
    text(ax, P(x, 3)[0], P(x, 3)[1] + 4.2, f'({x}, 3)', 'sujet', 's')
brace(ax, P(1, 3)[0], P(5, 3)[0], P(0, 3)[1] - 2, 'varie', label='avancée 5 − 1 = 4')
text(ax, 44, 48, 'montée 3 − 3 = 0', 'varie', 'm')
text(ax, 44, 57, r'pente $= 0 \div 4 = 0$', 'resultat', 'l', weight='bold')
save(fig, '19-114')
