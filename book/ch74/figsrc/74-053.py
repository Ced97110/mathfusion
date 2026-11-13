import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
ox, oy, u = 14, 10, 11
P = lambda x, y: (ox + x * u, oy + y * u)
line(ax, [P(-0.5, 0), P(5.5, 0)], 'fixe', dash=True)
text(ax, P(5.5, 0)[0] + 2, oy, r'axe de $A$', 'fixe', 's', ha='left')
line(ax, [P(-0.5, 1), P(5.5, 1)], 'resultat', lw=1.4)
text(ax, P(5.5, 1)[0] + 2, P(0, 1)[1], r'$D$', 'resultat', 'l', ha='left')
for x in (0.5, 2.5, 4.5):
    disc(ax, *P(x, 1), 1.2, 'resultat')
text(ax, P(2.5, 1)[0], P(0, 1)[1] + 3.3, 'points de D : fixes', 'resultat', 's')
disc(ax, *P(1.5, 0), 1.2, 'sujet'); disc(ax, *P(1.5, 2), 1.2, 'varie')
arrow(ax, (P(1.5, 0)[0], P(1.5, 0)[1] + 1.5), (P(1.5, 2)[0], P(1.5, 2)[1] - 1.5), 'varie')
text(ax, P(1.5, 0)[0] - 3, P(0, 0)[1] - 3.2, r'$Q$', 'sujet', 'm')
text(ax, P(1.5, 2)[0] - 3, P(0, 2)[1], r'$Q^\prime$', 'varie', 'm', ha='right')
text(ax, 44, 46, r'$b_1=0$ : réflexion d’axe $D$', 'encre', 'm')
save(fig, '74-053')
