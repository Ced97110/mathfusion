import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(40)
ox, oy, u = 12, 12, 12
P = lambda x, y: (ox + x * u, oy + y * u)
line(ax, [P(-0.5,0), P(6,0)], 'fixe', lw=1.4)
text(ax, 62, oy - 5, r'$B(x,u)=0$', 'fixe', 's')
arrow(ax, P(0,0), P(0.95,0), 'sujet', lw=1.6); text(ax, P(0.5,0)[0], oy - 4, r'$u$', 'sujet', 'm')
disc(ax, *P(1,0), 1.3, 'resultat'); text(ax, P(1,0)[0]+1, oy + 5.5, r'$\tau(u)=u$', 'resultat', 's')
disc(ax, *P(3,0), 1.3, 'resultat'); text(ax, P(3,0)[0], oy + 4.5, '(3, 0)', 'resultat', 's')
text(ax, P(3,0)[0], oy - 4.5, 'ne bouge pas', 'resultat', 's')
disc(ax, *P(3,1), 1.3, 'varie'); text(ax, P(3,1)[0] - 2, oy + 1 * u + 5, '(3, 1)', 'varie', 's')
arrow(ax, (P(3,1)[0] + 2.5, oy + u), (P(5,1)[0] - 2, oy + u), 'varie')
disc(ax, *P(5,1), 1.3, 'autre'); text(ax, P(5,1)[0] + 1, oy + u + 5, 'bouge', 'autre', 's')
save(fig, '75-073')
