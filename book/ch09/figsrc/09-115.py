import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
ox, oy, sx, sy = 14, 12, 14, 0.6
P = lambda g, m: (ox + g * sx, oy + m * sy)
arrow(ax, (ox, oy), (ox + 4 * sx + 8, oy), 'fixe'); arrow(ax, (ox, oy), (ox, oy + 100 * sy + 8), 'fixe')
text(ax, ox + 4 * sx + 8, oy - 4, 'g', 'fixe', 'l'); text(ax, ox - 4, oy + 100 * sy + 8, 'm', 'fixe', 'l')
line(ax, [P(0, 0), P(4, 100)], 'sujet', lw=1.1)
for g, m in [(1, 25), (2, 50), (4, 100)]:
    text(ax, P(g, 0)[0], oy - 3, str(g), 'fixe', 's'); text(ax, ox - 4, P(0, m)[1], str(m), 'fixe', 's')
for a, b in [((1, 25), (2, 50)), ((2, 50), (4, 100))]:
    line(ax, [P(a[0], a[1]), P(b[0], a[1]), P(b[0], b[1])], 'varie', dash=True)
text(ax, P(1.5, 0)[0], P(0, 25)[1] - 2.5, '+1', 'varie', 's'); text(ax, P(2, 0)[0] + 4, P(0, 37.5)[1], '+25', 'varie', 's')
text(ax, P(3, 0)[0], P(0, 50)[1] - 2.5, '+2', 'varie', 's'); text(ax, P(4, 0)[0] + 5, P(0, 75)[1], '+50', 'varie', 's')
for g, m in [(1, 25), (2, 50), (4, 100)]: disc(ax, *P(g, m), 1.6, 'varie')
save(fig, '09-115')
