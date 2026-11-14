import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
R = 5
pos = {1: (44, 12), 2: (24, 36), 3: (44, 36), 5: (64, 36), 6: (24, 60), 10: (44, 60), 15: (64, 60), 30: (44, 82)}
edges = [(1,2),(1,3),(1,5),(2,6),(2,10),(3,6),(3,15),(5,10),(5,15),(6,30),(10,30),(15,30)]
for a, b in edges:
    (x1, y1), (x2, y2) = pos[a], pos[b]
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    line(ax, [(x1 + ux * R, y1 + uy * R), (x2 - ux * R, y2 - uy * R)], 'fixe')
for n, (x, y) in pos.items():
    atom = n in (2, 3, 5)
    disc(ax, x, y, R, 'sujet' if atom else 'fixe', label=str(n), size='m')
text(ax, 2, 36, 'atomes', 'sujet', 's', ha='left')
text(ax, 2, 12, 'plus bas', 'fixe', 's', ha='left')
text(ax, 2, 86, 'divisibilité', 'fixe', 's', ha='left')
text(ax, 44, 3, 'rien entre 1 et chaque atome', 'sujet', 's')
save(fig, '80-214')
