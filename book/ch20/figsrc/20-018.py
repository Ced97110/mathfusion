import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
# haut : droite des nombres, x > 2, point vide en 2
f = numberline(ax, 8, 66, 88, 0, 4, arrow_right=True)
line(ax, [(f(2), 88), (f(4) + 4, 88)], 'resultat', lw=2.2)
disc(ax, f(2), 88, 1.4, 'sujet', fill=False, lw=1.0)
text(ax, 44, 98, r'$x > 2$', 'sujet', 'l')
text(ax, f(2), 78, 'point vide en 2', 'sujet', 's')
# bas : plan, y > x + 1, droite en pointillés
S = 6; X0 = 8; Y0 = 4; XM = -2; YM = -1.5
P = lambda x, y: (X0 + (x - XM) * S, Y0 + (y - YM) * S)
poly(ax, [P(-2, -1), P(4, 5), P(-2, 5)], 'resultat')
line(ax, [P(-2, -1.5), P(4, -1.5), P(4, 5), P(-2, 5), P(-2, -1.5)], 'fixe', lw=0.5)
line(ax, [P(-2, 0), P(4, 0)], 'fixe'); line(ax, [P(0, -1.5), P(0, 5)], 'fixe')
line(ax, [P(-2, -1), P(4, 5)], 'sujet', lw=1.1, dash=True)
text(ax, 56, 62, r'$y > x + 1$', 'sujet', 'l', ha='left')
text(ax, 58, 44, 'pointillé :', 'sujet', 's', ha='left')
text(ax, 58, 40, 'ligne de couples', 'sujet', 's', ha='left')
text(ax, 58, 36, 'exclue', 'sujet', 's', ha='left')
text(ax, *P(-0.9, 3.6), 'zone', 'resultat', 's')
arrow(ax, (f(2), 76), (P(1, 2)[0] - 0.5, P(1, 2)[1] + 0.8), 'varie', curve=-0.0)
save(fig, '20-018')
