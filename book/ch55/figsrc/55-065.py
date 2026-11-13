import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
ox, oy, u = 12, 10, 13
arrow(ax, (ox - 2, oy), (ox + 5 * u + 6, oy), 'fixe', lw=0.7)
arrow(ax, (ox, oy - 2), (ox, oy + 5 * u + 6), 'fixe', lw=0.7)
line(ax, [(ox, oy), (ox + 5.4 * u, oy + 5.4 * u)], 'resultat', lw=1.0, dash=True)
text(ax, ox + 4.6 * u, oy + 5.2 * u, r'$y=x$', 'resultat', 's')
def P(a, b): return (ox + a * u, oy + b * u)
pairs = [((1, 3), (3, 1)), ((0, 5), (5, 0))]
for (a, b), (c, d) in pairs:
    p, q = P(a, b), P(c, d)
    arrow(ax, p, q, 'varie', both=True)
    disc(ax, p[0], p[1], 1.6, 'sujet'); disc(ax, q[0], q[1], 1.6, 'autre')
text(ax, P(1, 3)[0] - 8, P(1, 3)[1] + 3, '(1, 3)', 'sujet', 's')
text(ax, P(3, 1)[0] + 8, P(3, 1)[1] - 3, '(3, 1)', 'autre', 's')
text(ax, P(0, 5)[0] + 9, P(0, 5)[1] + 1, '(0, 5)', 'sujet', 's')
text(ax, P(5, 0)[0] - 1, P(5, 0)[1] + 5, '(5, 0)', 'autre', 's')
disc(ax, *P(2, 2), 1.8, 'fixe')
text(ax, 26, 30, '(2, 2) ne bouge pas', 'fixe', 's')
save(fig, '55-065')
