import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, oy, u = 10, 18, 24
P = lambda a, b: (ox + a * u, oy + b * u)
arrow(ax, P(-0.1, 0), P(1.7, 0), 'fixe', lw=0.9)
arrow(ax, P(0, -0.1), P(0, 1.7), 'fixe', lw=0.9)
# écriture 1 : (1, 1) sur la diagonale Z
arrow(ax, P(0, 0), P(0.95, 0.95), 'varie', lw=1.8)
# écriture 2 : (1, 0) sur X puis (0, 1) sur Y
arrow(ax, P(0, 0), P(0.95, 0), 'sujet', lw=1.8)
arrow(ax, P(1, 0.05), P(1, 0.95), 'autre', lw=1.8)
disc(ax, *P(1, 1), 1.7, 'resultat')
text(ax, P(1, 1)[0] + 3.5, P(1, 1)[1] + 3.5, '(1, 1)', 'resultat', 's', weight='bold')
text(ax, P(1.7, 0)[0] - 1, P(1.7, 0)[1] - 3.5, 'X', 'sujet', 's', weight='bold')
text(ax, P(0, 1.7)[0] + 3, P(0, 1.7)[1], 'Y', 'autre', 's', weight='bold')
text(ax, P(0.55, 0.55)[0] - 3.5, P(0.55, 0.55)[1] + 3.5, 'Z', 'varie', 's', weight='bold')
text(ax, 70, 58, 'écriture 1 :', 'varie', 's', weight='bold')
text(ax, 70, 53, '(1, 1) sur Z', 'varie', 's')
text(ax, 70, 41, 'écriture 2 :', 'sujet', 's', weight='bold')
text(ax, 70, 36, '(1, 0) + (0, 1)', 'sujet', 's')
box(ax, 54, 8, 32, 14, 'limite', label='deux écritures', size='s', weight='bold')
save(fig, '58-263')
