import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# 41-026 : le vent (100) est l'hypoténuse du triangle O, V, pied de V ; côtés 50 et 86,6
fig, ax = canvas(84)
s = 0.6
O = (14, 22)
V = (O[0] + 50 * s, O[1] + 86.6 * s)
P = (V[0], O[1])
arrow(ax, (6, O[1]), (82, O[1]), 'fixe', lw=0.7)
line(ax, [V, P], 'resultat', lw=1.6)
line(ax, [O, P], 'sujet', lw=1.6)
arrow(ax, O, V, 'varie', lw=1.6)
d = 2.2
line(ax, [(P[0] - d, P[1]), (P[0] - d, P[1] + d), (P[0], P[1] + d)], 'fixe', lw=0.6)
disc(ax, O[0], O[1], 0.9, 'encre'); disc(ax, V[0], V[1], 0.9, 'encre'); disc(ax, P[0], P[1], 0.9, 'encre')
text(ax, O[0] - 3, O[1] - 3.5, '$O$', 'encre')
text(ax, V[0] + 3, V[1] + 1, '$V$', 'encre')
text(ax, P[0] + 4.5, P[1] - 3.5, 'pied de $V$', 'encre', 's')
text(ax, (O[0] + P[0]) / 2, O[1] - 4, '50', 'sujet', 'm')
text(ax, P[0] + 2.5, (P[1] + V[1]) / 2, '86,6', 'resultat', 'm', ha='left')
text(ax, (O[0] + V[0]) / 2 - 3.5, (O[1] + V[1]) / 2 + 3, '100', 'varie', 'm', ha='right')
text(ax, 44, 12, '2 500 + 7 500 = 10 000', 'encre', 's')
text(ax, 44, 5.5, 'carrés des trois côtés', 'fixe', 's')
save(fig, '41-026')
