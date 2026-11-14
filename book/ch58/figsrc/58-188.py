import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
# le plan W dans l'espace : deux flèches a et b non alignées l'engendrent
u, O = 9.0, (60.0, 26.0)
P = lambda x, y, z: iso(x, y, z, O, u)
for v in [(2.7, 0, 0), (0, 2.7, 0), (0, 0, 2.7)]:
    arrow(ax, O, P(*v), 'fixe', lw=0.7)
a, b = (1, 2, 1), (0, 1, -1)
ab = tuple(i + j for i, j in zip(a, b))
poly(ax, [O, P(*a), P(*ab), P(*b)], 'sujet')
arrow(ax, O, P(*a), 'sujet', lw=1.6)
arrow(ax, O, P(*b), 'sujet', lw=1.6)
pa, pb = P(*a), P(*b)
text(ax, pa[0] - 2, pa[1] + 3, r'$a = (1, 2, 1)$', 'sujet', 's', ha='right')
text(ax, pb[0] - 2, pb[1] - 3, r'$b = (0, 1, -1)$', 'sujet', 's', ha='right')
text(ax, 50, 33, r'plan $W$', 'sujet', 'm', weight='bold')
text(ax, 75, 52, 'les 3 axes :\n3 directions', 'fixe', 's')
text(ax, 44, 5, r'$W$ : 2 directions, $\dim W = 2$', 'resultat', 'm', weight='bold')
save(fig, '58-188')
