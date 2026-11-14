import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
lv = {0: [(1, 44)], 1: [(2, 24), (3, 44), (5, 64)], 2: [(4, 14), (6, 34), (10, 54), (15, 74)],
      3: [(12, 24), (20, 44), (30, 64)], 4: [(60, 44)]}
Y = {0: 8, 1: 22, 2: 36, 3: 50, 4: 64}
pos = {d: (x, Y[l]) for l, items in lv.items() for d, x in items}
edges = [(d, d * p) for d in pos for p in (2, 3, 5) if d * p in pos]
chainA = {(1, 2), (2, 4), (4, 12), (12, 60)}
chainB = {(1, 5), (5, 10), (10, 30), (30, 60)}
for a, b in edges:
    role = 'varie' if (a, b) in chainA else 'autre' if (a, b) in chainB else 'fixe'
    line(ax, [(pos[a][0], pos[a][1] + 3), (pos[b][0], pos[b][1] - 3)], role, lw=1.6 if role != 'fixe' else 0.7)
for d, (x, y) in pos.items():
    box(ax, x - 5, y - 3, 10, 6, 'sujet', label=str(d), size='s', r=0.6)
text(ax, 44, 72, r'ordres des sous-groupes de $\mathbb{Z}/60$', 'sujet', 's')
save(fig, '64-082')
