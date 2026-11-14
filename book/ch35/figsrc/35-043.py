import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(56)
u = 7
for ox, k in [(6, 1), (50, 2)]:
    oy = 10
    P = lambda x, y: (ox + x * u, oy + y * u)
    arrow(ax, (ox - 2, oy), (ox + 34, oy), 'fixe', lw=0.7); arrow(ax, (ox, oy - 2), (ox, oy + 36), 'fixe', lw=0.7)
    if k == 1:
        line(ax, [P(0, 0), P(3, 0), P(3, 4)], 'sujet', lw=1.5)
        text(ax, P(1.5, 0)[0], oy - 4, '3', 'sujet', 's'); text(ax, P(3, 2)[0] + 3, P(3, 2)[1], '4', 'sujet', 's')
        text(ax, ox + 18, 52, 'côtés : 3 et 4', 'sujet', 's')
    else:
        line(ax, [P(0, 0), P(3, 4)], 'autre', lw=1.5)
        line(ax, [(ox + 8 * math.cos(math.radians(i * 53.13 / 18)), oy + 8 * math.sin(math.radians(i * 53.13 / 18))) for i in range(19)], 'varie', lw=1.2)
        text(ax, 54.5, 30, '5', 'autre', 'm'); text(ax, 63, 14, '53,13°', 'varie', 's')
        text(ax, ox + 16, 52, 'distance et direction', 'autre', 's')
    disc(ax, *P(3, 4), 1.3, 'resultat')
text(ax, 44, 30, '=', 'encre', 'xl')
save(fig, '35-043')
