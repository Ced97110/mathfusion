import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
X = lambda v: 28 + 1.5 * v
text(ax, 3, 52, 'règle de 30 cm', 'fixe', 'm', ha='left')
box(ax, X(0), 38, X(30) - X(0), 8, 'fixe')
text(ax, X(0), 34, '0', 'fixe', 's'); text(ax, X(30), 34, '30', 'fixe', 's')
for v, s in [(-2, '−2'), (31, '31')]:
    disc(ax, X(v), 42, 1.0, 'limite', fill=False); text(ax, X(v), 48, s, 'limite', 's')
text(ax, 3, 27, 'droite des réels', 'sujet', 'm', ha='left')
arrow(ax, (3, 15), (85, 15), 'sujet', both=True)
for v, s in [(-2, '−2'), (31, '31')]:
    disc(ax, X(v), 15, 1.2, 'resultat'); text(ax, X(v), 9, s, 'resultat', 's')
text(ax, X(0), 21, '0', 'sujet', 's'); disc(ax, X(0), 15, 1.2, 'sujet')
save(fig, '12-057')
