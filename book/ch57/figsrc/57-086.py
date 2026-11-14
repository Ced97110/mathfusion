import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
cx, cy, u = 44, 30, 6
line(ax, [(4, cy), (84, cy)], 'fixe', lw=0.5)
line(ax, [(cx, 6), (cx, 56)], 'fixe', lw=0.5)
P = (cx + 6 * u, cy + 3 * u); Q = (cx - 6 * u, cy - 3 * u)
arrow(ax, (cx, cy), P, 'sujet', lw=1.3)
arrow(ax, (cx, cy), Q, 'autre', lw=1.3)
disc(ax, cx, cy, 1.4, 'resultat')
text(ax, 70, 53, '3x = (6 ; 3)', 'sujet', 's')
text(ax, 22, 7, r'$(-3)x$ = (−6 ; −3)', 'autre', 's')
text(ax, 54, 25.5, '(0 ; 0)', 'resultat', 's')
text(ax, 23, 52, 'somme = (0 ; 0) : opposés', 'resultat', 's')
save(fig, '57-086')
