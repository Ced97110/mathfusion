import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
X = lambda v: 44 + v * 11
line(ax, [(8, 40), (80, 40)], 'fixe')
cols = {1: 'sujet', 0: 'fixe', 2: 'varie', 3: 'varie', -1: 'autre', -2: 'autre', -3: 'autre'}
for v, role in cols.items():
    disc(ax, X(v), 40, 3.4, role, label=str(v), size='s')
arrow(ax, (X(1), 44.5), (X(2), 44.5), 'varie', curve=-0.5); arrow(ax, (X(2), 44.5), (X(3), 44.5), 'varie', curve=-0.5)
arrow(ax, (X(1), 35.5), (X(-1), 35.5), 'autre', curve=-0.4); arrow(ax, (X(2), 35.5), (X(-2), 35.5), 'autre', curve=-0.3)
text(ax, 20, 62, 'départ : f(1) = g(1)', 'sujet', 's', ha='left')
text(ax, X(1), 56, '1 est dans E', 'sujet', 's')
text(ax, 66, 24, 'sommes', 'varie', 's'); text(ax, 22, 24, 'inverses', 'autre', 's')
text(ax, X(0), 24, 'neutre', 'fixe', 's')
box(ax, 4, 28, 80, 22, 'resultat', fill=False, dash=True)
text(ax, 44, 8, 'E est un sous-groupe : E = G', 'resultat', 'm', weight='bold')
save(fig, '48-186')
