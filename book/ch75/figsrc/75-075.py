import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
ox, oy, u = 14, 14, 17
P = lambda x, y: (ox + x * u, oy + y * u)
arrow(ax, P(0,0), P(3.6,0), 'fixe'); arrow(ax, P(0,0), P(0,1.6), 'fixe')
for v in range(4):
    line(ax, [(P(v,0)[0], oy - 1), (P(v,0)[0], oy + 1)], 'fixe'); text(ax, P(v,0)[0], oy - 4, str(v), 'fixe', 's')
text(ax, 72, oy + 4, 'position', 'fixe', 's'); text(ax, ox + 2, oy + 1.6 * u + 3, 'vitesse', 'fixe', 's', ha='left')
line(ax, [P(0,1), P(3.4,1)], 'fixe', dash=True)
disc(ax, *P(1,1), 1.5, 'sujet'); disc(ax, *P(3,1), 1.5, 'resultat')
text(ax, P(1,1)[0], oy + u + 5, '(1, 1)', 'sujet', 's'); text(ax, P(3,1)[0], oy + u + 5, '(3, 1)', 'resultat', 's')
arrow(ax, (P(1,1)[0] + 2.5, oy + u), (P(3,1)[0] - 2.5, oy + u), 'varie')
text(ax, P(2,1)[0], oy + u - 4, 'après 2 s', 'varie', 's')
text(ax, 44, 4, 'position + 2 × vitesse', 'varie', 's')
save(fig, '75-075')
