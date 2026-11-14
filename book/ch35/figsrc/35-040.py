import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, oy, u = 44, 38, 7
P = lambda x, y: (ox + x * u, oy + y * u)
poly(ax, [(44, 4), (84, 4), (84, 66), (44, 66)], 'resultat'); poly(ax, [(4, 4), (44, 4), (44, 66), (4, 66)], 'limite')
arrow(ax, (6, oy), (82, oy), 'fixe', lw=0.7); arrow(ax, (ox, 6), (ox, 64), 'fixe', lw=0.7)
arrow(ax, (ox, oy), P(1, -3), 'sujet', lw=1.3); arrow(ax, (ox, oy), P(-1, 3), 'autre', lw=1.3)
disc(ax, *P(1, -3), 1.1, 'sujet'); disc(ax, *P(-1, 3), 1.1, 'autre')
text(ax, 64, 63, '−90° à 90°', 'resultat', 's'); text(ax, 24, 63, 'hors de l’intervalle', 'limite', 's')
text(ax, 34, 59, 'B(−1 ; 3)', 'autre', 's', ha='right'); text(ax, 54, 17, 'A(1 ; −3)', 'sujet', 's', ha='left')
text(ax, 24, 30, 'calculatrice : −71,57°', 'limite', 's'); text(ax, 24, 24, 'angle juste : 108,43°', 'autre', 's')
text(ax, 64, 30, 'calculatrice : −71,57°', 'resultat', 's'); text(ax, 64, 24, 'et c’est juste', 'resultat', 's')
save(fig, '35-040')
