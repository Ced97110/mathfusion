import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
ox, oy, u = 26, 10, 14
P = lambda x, y: (ox + x * u, oy + y * u)
arrow(ax, P(0,0), P(1,0), 'sujet', lw=1.4); text(ax, P(0.5,0)[0], oy - 4, r'$u$', 'sujet', 'm')
text(ax, P(1,0)[0] + 3, oy, 'direction', 'sujet', 's', ha='left')
for h, lab, d in [(1.0, 'coordonnée 1', 'glisse de 2'), (0.5, 'coordonnée 0,5', 'glisse de 1')]:
    y = oy + h * u + 8
    disc(ax, P(0, 0)[0], y, 1.4, 'varie'); text(ax, ox - 4, y, lab, 'encre', 's', ha='right')
    arrow(ax, (ox + 2.4, y), (ox + float(d[-1]) * u - 1.4, y), 'varie')
    disc(ax, ox + float(d[-1]) * u, y, 1.4, 'resultat')
    text(ax, ox + float(d[-1]) * u + 3, y, d, 'varie', 's', ha='left')
text(ax, 44, 42, 'même direction, longueur variable', 'fixe', 's')
save(fig, '75-072')
