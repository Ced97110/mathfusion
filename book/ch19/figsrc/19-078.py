import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
ox, oy, ux, uy = 18, 8, 12, 9
P = lambda x, y: (ox + x * ux, oy + y * uy)
arrow(ax, (ox, oy), (ox + 2.6 * ux, oy), 'fixe', lw=0.8); arrow(ax, (ox, oy), (ox, oy + 4.6 * uy), 'fixe', lw=0.8)
line(ax, [P(0, 4), P(2, 0)], 'sujet', lw=1.5)
disc(ax, *P(0, 4), 1.6, 'sujet'); disc(ax, *P(2, 0), 1.6, 'sujet')
text(ax, 16, P(0, 4)[1], '(0, 4)', 'sujet', 's', ha='right'); text(ax, P(2, 0)[0] + 3, 3.5, '(2, 0)', 'sujet', 's')
arrow(ax, P(0, 4), P(2, 4), 'fixe', lw=1.0); text(ax, P(1, 4)[0], P(0, 4)[1] + 4.5, 'avance +2', 'fixe', 's')
arrow(ax, P(2, 4), P(2, 0), 'varie', lw=1.2); text(ax, P(2, 2)[0] + 3, P(0, 2)[1], 'monte −4', 'varie', 's', ha='left')
text(ax, 72, 38, '−4 sur 2 = −2', 'resultat', 'm', weight='bold')
text(ax, 72, 26, r'$m<0$', 'resultat', 'l')
save(fig, '19-078')
