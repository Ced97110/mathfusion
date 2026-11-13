import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
s = 6.2
O = (40, 36)
box(ax, 8, 78, 72, 10, 'sujet', label=r'forme hermitienne : $x\cdot\bar y$', size='m')
arrow(ax, (20, 77), (20, 68), 'varie'); text(ax, 24, 72.5, r'$x=y=z$', 'varie', 's', ha='left')
box(ax, 2, 56, 34, 11, 'resultat', label=r'$z\bar z=N(z)$', size='m')
text(ax, 2, 50, r'$3+4i$ : $z\bar z=25$', 'resultat', 's', ha='left')
text(ax, 2, 45, r'$1+2i$ : $z\bar z=5$', 'resultat', 's', ha='left')
arrow(ax, (8, 36), (80, 36), 'fixe'); arrow(ax, (40, 6), (40, 66), 'fixe')
text(ax, 74, 31, 'réel', 'fixe', 's'); text(ax, 56, 64, 'imaginaire', 'fixe', 's')
P, Q = (40 + 3 * s, 36 + 4 * s), (40 + 3 * s, 36 - 4 * s)
arrow(ax, O, P, 'sujet', lw=1.3); arrow(ax, O, Q, 'autre', lw=1.3)
line(ax, [P, Q], 'fixe', dash=True)
text(ax, 76, 58, r'$z=3+4i$', 'sujet', 's'); text(ax, 74, 10, r'$\bar z=3-4i$', 'autre', 's')
text(ax, 18, 42, r'$z=1+2i$ : $z\bar z=5$', 'resultat', 's', ha='left') if False else None
save(fig, '77-142')
