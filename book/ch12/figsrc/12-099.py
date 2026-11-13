import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
dims = [(i, j, k) for i in range(2) for j in range(3) for k in range(4)]
u = 5
cubes(ax, [c for c in dims if c[2] != 3], (24, 12), u, 'fixe')
cubes(ax, [c for c in dims if c[2] == 3], (24, 12), u, 'sujet')
cubes(ax, [c for c in dims if c[0] != 0], (66, 12), u, 'fixe')
cubes(ax, [c for c in dims if c[0] == 0], (66, 12), u, 'autre')
text(ax, 24, 51, '(2 · 3) · 4 = 24', 'sujet', 'm')
text(ax, 66, 51, '2 · (3 · 4) = 24', 'autre', 'm')
text(ax, 24, 5, '6 par couche, 4 couches', 'sujet', 's')
text(ax, 66, 5, '12 par tranche, 2 tranches', 'autre', 's')
save(fig, '12-099')
