import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
k = 5.2
line(ax, [(44, 4), (44, 63)], 'fixe', lw=0.6, dash=True)
# gauche : multiples de (2, 4)
ox, oy = 8, 8
P = lambda a, b: (ox + a * k, oy + b * k)
arrow(ax, P(-0.5, 0), P(6, 0), 'fixe', lw=0.5)
arrow(ax, P(0, -0.5), P(0, 9.3), 'fixe', lw=0.5)
line(ax, [P(-0.3, -0.6), P(4.3, 8.6)], 'sujet', lw=1.5)
disc(ax, *P(2, 4), 1.1, 'sujet'); disc(ax, *P(4, 8), 1.1, 'sujet')
disc(ax, *P(0, 0), 1.3, 'resultat')
text(ax, P(2, 4)[0] + 2, P(2, 4)[1] - 2.5, '(2, 4)', 'sujet', 's', ha='left')
text(ax, P(4, 8)[0] + 2, P(4, 8)[1] - 2.5, '(4, 8)', 'sujet', 's', ha='left')
text(ax, P(0, 0)[0] + 3, P(0, 0)[1] - 3.5, r'$0\times(2,4)$', 'resultat', 's', ha='left')
text(ax, 22, 61, 'passe par l’origine', 'resultat', 's', weight='bold')
# droite : hauteur 2
qx, qy = 54, 8
Q = lambda a, b: (qx + a * k, qy + b * k)
arrow(ax, Q(-0.5, 0), Q(6, 0), 'fixe', lw=0.5)
arrow(ax, Q(0, -0.5), Q(0, 9.3), 'fixe', lw=0.5)
line(ax, [Q(-0.3, 2), Q(6, 2)], 'limite', lw=1.5)
disc(ax, *Q(0, 0), 1.3, 'limite', fill=False)
text(ax, Q(0, 0)[0] + 3, Q(0, 0)[1] - 3.5, '(0, 0) absent', 'limite', 's', ha='left')
text(ax, Q(3, 2)[0], Q(3, 2)[1] + 3, 'hauteur 2', 'limite', 's')
text(ax, 66, 61, 'ne passe pas par 0', 'limite', 's', weight='bold')
save(fig, '58-120')
