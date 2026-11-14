import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
ox, oy, u = 14, 12, 9
P = lambda x, y: (ox + x * u, oy + y * u)
arrow(ax, (ox - 6, oy), (ox + 36, oy), 'fixe', lw=0.7); arrow(ax, (ox, oy - 4), (ox, oy + 46), 'fixe', lw=0.7)
poly(ax, [P(0, 0), P(3, 0), P(3, 4)], 'fixe')
line(ax, [P(0, 0), P(3, 4)], 'sujet', lw=1.8)
line(ax, [(ox + 9 * math.cos(math.radians(i * 53.13 / 18)), oy + 9 * math.sin(math.radians(i * 53.13 / 18))) for i in range(19)], 'varie', lw=1.4)
disc(ax, *P(3, 4), 1.2, 'resultat'); disc(ax, ox, oy, 0.9, 'encre')
text(ax, ox - 3, oy - 3, 'O', 'encre', 's'); text(ax, 44, 49, 'A(3 ; 4)', 'resultat', 's', ha='left')
text(ax, P(1.5, 0)[0], oy - 3, '3', 'fixe', 's'); text(ax, 44, P(0, 2)[1], '4', 'fixe', 's')
text(ax, 22, 33, r'$R=5$', 'sujet', 's'); text(ax, 31, 15.5, r'$\alpha=53{,}13^\circ$', 'varie', 's')
box(ax, 50, 30, 36, 10, 'sujet', label='R : distance de O à A', size='s')
box(ax, 50, 14, 36, 10, 'varie', label='α : direction de OA', size='s')
save(fig, '35-035')
