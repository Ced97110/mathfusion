import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
ox, oy, u = 44, 30, 8
P = lambda x, y: (ox + x * u, oy + y * u)
arrow(ax, (6, oy), (82, oy), 'fixe', lw=0.7); arrow(ax, (ox, 4), (ox, 57), 'fixe', lw=0.7)
line(ax, [P(1.5, -4.5), P(-1.5, 4.5)], 'fixe', dash=True)
arrow(ax, (ox, oy), P(1, -3), 'sujet', lw=1.4); arrow(ax, (ox, oy), P(-1, 3), 'autre', lw=1.4)
disc(ax, *P(1, -3), 1.1, 'sujet'); disc(ax, *P(-1, 3), 1.1, 'autre')
text(ax, 55, 6, 'A(1 ; −3)', 'sujet', 's', ha='left'); text(ax, 55, 11.5, '−71,57°', 'sujet', 's', ha='left')
text(ax, 33, 54, "A'(−1 ; 3)", 'autre', 's', ha='right'); text(ax, 33, 48.5, '108,43°', 'autre', 's', ha='right')
text(ax, 67, 52, 'même droite : tan = −3', 'fixe', 's'); text(ax, 21, 6, 'directions opposées', 'varie', 's')
save(fig, '35-039')
