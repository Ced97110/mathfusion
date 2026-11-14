import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
o = (44, 34); s = 8
G = lambda x, y: (o[0] + x * s, o[1] + y * s)
arrow(ax, G(-5.2, 0), G(6.6, 0), 'fixe', lw=0.6); arrow(ax, G(0, -2.3), G(0, 2.6), 'fixe', lw=0.6)
for c in (1, -1): line(ax, [G(c - 4, 2), G(c + 4, -2)], 'sujet', lw=1.3)
arrow(ax, G(1, 0), G(-1, 1), 'varie', lw=1.3)
disc(ax, *G(1, 0), 1.0, 'sujet'); disc(ax, *G(-1, 1), 1.0, 'resultat')
text(ax, G(1, 0)[0] + 2, G(1, 0)[1] - 3, r'$(1,0)$', 'sujet', 's', ha='left')
text(ax, G(-1, 1)[0] - 2, G(-1, 1)[1] + 3, r'$(-1,1)$', 'resultat', 's', ha='right')
text(ax, 44, 59, r'$Q=(x+2y)^2=1$ : droites entières', 'sujet', 's')
text(ax, 4, 6, r'$z=(-2,1)$ : radical, même direction', 'varie', 's', ha='left')
text(ax, 4, 13, r'$(1,0)+z=(-1,1)$ : même courbe', 'resultat', 's', ha='left')
save(fig, '71-197')
