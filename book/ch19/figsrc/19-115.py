import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, ux, uy, x0, x1, y0, y1):
    arrow(ax, (ox + x0 * ux, oy), (ox + x1 * ux + 3, oy), "fixe", lw=0.8)
    arrow(ax, (ox, oy + y0 * uy), (ox, oy + y1 * uy + 3), "fixe", lw=0.8)
    return lambda x, y: (ox + x * ux, oy + y * uy)
fig, ax = canvas(64); P = plane(ax, 10, 8, 8, 8, 0, 8, 0, 5.5)
line(ax, [P(0.5, 5), P(7.8, 5)], 'sujet', lw=1.4)
for x in (2, 7):
    line(ax, [P(x, 0), P(x, 5)], 'fixe', dash=True)
    disc(ax, *P(x, 5), 1.3, 'sujet')
    text(ax, P(x, 0)[0], 3.6, str(x), 'sujet', 's')
text(ax, 6.2, P(0, 5)[1], '5', 'sujet', 's')
text(ax, P(4.5, 3.2)[0], P(4.5, 3.2)[1], 'montée 5 − 5 = 0', 'varie', 's')
text(ax, P(4.5, 2.0)[0], P(4.5, 2.0)[1], 'avancée 7 − 2 = 5', 'varie', 's')
text(ax, 50, 59, r'pente $= 0 \div 5 = 0$', 'resultat', 'l', weight='bold')
save(fig, '19-115')
