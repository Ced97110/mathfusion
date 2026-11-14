import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(44)
ox, oy, u = 20, 10, 16
P = lambda x, y: (ox + x * u, oy + y * u)
poly(ax, [P(0,0), P(1,0), P(1,1), P(0,1)], 'fixe')
poly(ax, [P(0,0), P(1,0), P(3,1), P(2,1)], 'sujet')
line(ax, [P(-0.2,0), P(3.2,0)], 'fixe', lw=1.4)
for h, lab in [(0, 'vitesse 0'), (0.5, 'vitesse 0,5'), (1, 'vitesse 1')]:
    text(ax, ox - 4, oy + h * u, lab, 'encre', 's', ha='right')
arrow(ax, P(0.05, 0.5), P(1.95, 0.5), 'varie'); arrow(ax, P(0.05, 1.22), P(2.0, 1.22), 'varie')
text(ax, P(2.15, 0.5)[0], oy + 0.5 * u, 'glisse de 1', 'varie', 's', ha='left')
text(ax, P(2.0, 1.0)[0] + 2, oy + 1.22 * u, 'glisse de 2', 'varie', 's', ha='left')
text(ax, P(1.1, 0)[0] + 1, oy - 4, 'ne bouge pas', 'fixe', 's', ha='left')
text(ax, 4, oy + 1.22 * u + 8, 'carré avant', 'fixe', 's', ha='left')
text(ax, 84, oy + 1.22 * u + 8, 'parallélogramme après', 'sujet', 's', ha='right')
save(fig, '75-070')
