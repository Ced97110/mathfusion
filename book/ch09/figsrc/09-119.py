import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy, sx, sy = 14, 12, 14, 0.6
P = lambda g, m: (ox + g * sx, oy + m * sy)
arrow(ax, (ox, oy), (ox + 4 * sx + 8, oy), 'fixe'); arrow(ax, (ox, oy), (ox, oy + 100 * sy + 6), 'fixe')
line(ax, [P(0, 0), P(4, 100)], 'sujet', lw=1.1)
poly(ax, [P(0, 0), P(2, 0), P(2, 50)], 'varie')
text(ax, P(1, 0)[0], oy - 3.5, 'avancée 2', 'varie', 's'); text(ax, P(2, 0)[0] + 2, P(0, 25)[1], 'montée 50', 'varie', 's', ha='left')
disc(ax, *P(2, 50), 1.6, 'sujet')
text(ax, 32, 58, r'$50 \div 2 = 25$', 'resultat', 'l', weight='bold')
text(ax, ox - 4, P(0, 50)[1], '50', 'fixe', 's')
save(fig, '09-119')
