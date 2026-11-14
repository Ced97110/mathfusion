import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# 41-033 : a = 100 × 0,5 = 50 ; b = 100 × 0,8660 = 86,60 ; 50² + 86,6² ≈ 100² : on retrouve la norme
fig, ax = canvas(92)
s = 0.45
O = (12, 44)
V = (O[0] + 50 * s, O[1] + 86.6 * s)
P = (V[0], O[1])
arrow(ax, (6, O[1]), (62, O[1]), 'fixe', lw=0.6)
line(ax, [V, P], 'resultat', lw=1.6)
line(ax, [O, P], 'sujet', lw=1.6)
arrow(ax, O, V, 'varie', lw=1.6)
d = 2.0
line(ax, [(P[0] - d, P[1]), (P[0] - d, P[1] + d), (P[0], P[1] + d)], 'fixe', lw=0.6)
text(ax, (O[0] + P[0]) / 2, O[1] - 4, '100 × 0,5 = 50', 'sujet', 's')
text(ax, P[0] + 2.5, (P[1] + V[1]) / 2, '100 × 0,8660 = 86,60', 'resultat', 's', ha='left')
text(ax, (O[0] + V[0]) / 2 - 3, (O[1] + V[1]) / 2 + 2.5, '100', 'varie', 'm', ha='right')
# contrôle : les carrés des composantes redonnent le carré de la norme
yb = 18; h = 12
box(ax, 1.5, yb, 24, h, 'sujet', label='50² = 2 500', size='s')
text(ax, 28, yb + h / 2, '+', 'encre', 'l')
box(ax, 30.5, yb, 26, h, 'resultat', label='86,6² ≈ 7 500', size='s')
text(ax, 59, yb + h / 2, '=', 'encre', 'l')
box(ax, 61.5, yb, 25, h, 'varie', label='100² = 10 000', size='s')
text(ax, 44, 8, 'on retrouve la norme 100', 'fixe', 's')
save(fig, '41-033')
