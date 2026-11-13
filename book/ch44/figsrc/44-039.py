import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
P = {1: (26, 56), 2: (62, 56), 3: (62, 20), 4: (26, 20)}
poly(ax, list(P.values()), 'fixe', fill=False, lw=0.8)
line(ax, [P[1], P[3]], 'sujet', lw=1.2, dash=True)
arrow(ax, (59.5, 52.5), (28.5, 23.5), 'varie', both=True)
for k, (x, y) in P.items(): disc(ax, x, y, 4.5, 'sujet' if k in (1, 3) else 'varie', label=str(k), size='l')
text(ax, 44, 72, r'$r \circ s$ : 2 et 4 s’échangent', 'varie', 'm')
text(ax, 44, 7, '1 et 3 restent en place', 'sujet', 'm')
text(ax, 11, 64, 'axe', 'sujet', 's')
save(fig, '44-039')
