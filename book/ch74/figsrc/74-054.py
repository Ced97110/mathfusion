import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, oy, u = 8, 30, 10.5
P = lambda x, y: (ox + x * u, oy + y * u)
line(ax, [P(-0.2, 0), P(7, 0)], 'resultat', lw=1.4)
text(ax, P(7, 0)[0] + 1.5, P(0, 0)[1], r'$D$', 'resultat', 'l', ha='left')
# point on D: slides by 5
disc(ax, *P(0, 0), 1.2, 'sujet'); disc(ax, *P(5, 0), 1.2, 'varie')
text(ax, P(0, 0)[0] - 3.5, P(0, 0)[1] + 3, r'$P$', 'sujet', 'm')
text(ax, P(5, 0)[0] + 3.8, P(0, 0)[1] + 3, r'$P^\prime$', 'varie', 'm')
# point off D: flipped across D, then slides by 5
disc(ax, *P(0, 1.3), 1.2, 'sujet'); text(ax, P(0, 1.3)[0] - 3.5, P(0, 1.3)[1], r'$Q$', 'sujet', 'm')
line(ax, [P(0, 1.3), P(0, -1.3)], 'fixe', lw=0.7, dash=True)
disc(ax, *P(0, -1.3), 1.2, 'fixe', fill=False)
text(ax, P(0, -1.3)[0] + 2, P(0, -1.3)[1] - 4, 'miroir de $Q$', 'fixe', 's')
disc(ax, *P(5, -1.3), 1.2, 'varie'); text(ax, P(5, -1.3)[0] + 3.8, P(5, -1.3)[1], r'$Q^\prime$', 'varie', 'm')
arrow(ax, (P(0, -1.3)[0] + 1.6, P(0, -1.3)[1]), (P(5, -1.3)[0] - 1.6, P(5, -1.3)[1]), 'varie')
arrow(ax, (P(0, 0)[0] + 1.6, P(0, 0)[1] + 1.8), (P(5, 0)[0] - 1.6, P(5, 0)[1] + 1.8), 'varie', curve=-0.2)
text(ax, P(2.5, 0)[0], P(0, 0)[1] + 8, r'$x_1\to x_1+5$', 'varie', 'm')
text(ax, 44, 65, 'retourner, puis glisser', 'resultat', 'm')
text(ax, 44, 5, r'$b_1=5\neq 0$ : aucun point fixe', 'limite', 'm')
save(fig, '74-054')
