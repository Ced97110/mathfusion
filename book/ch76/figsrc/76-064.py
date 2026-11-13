import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
X = [42, 59, 76]; Y = [8, 30, 52, 74]; bw = 14; bh = 9
nodes = {0: [(59, '1')], 1: [(X[0], r'$e_1$'), (X[1], r'$e_2$'), (X[2], r'$e_3$')],
         2: [(X[0], r'$e_{12}$'), (X[1], r'$e_{13}$'), (X[2], r'$e_{23}$')], 3: [(59, r'$e_{123}$')]}
edges = [((0, 0), (1, 0)), ((0, 0), (1, 1)), ((0, 0), (1, 2)), ((1, 0), (2, 0)), ((1, 0), (2, 1)), ((1, 1), (2, 0)),
         ((1, 1), (2, 2)), ((1, 2), (2, 1)), ((1, 2), (2, 2)), ((2, 0), (3, 0)), ((2, 1), (3, 0)), ((2, 2), (3, 0))]
for (a, i), (b, j) in edges:
    line(ax, [(nodes[a][i][0], Y[a] + bh), (nodes[b][j][0], Y[b])], 'fixe')
for lv, lst in nodes.items():
    for x, lab in lst:
        box(ax, x - bw / 2, Y[lv], bw, bh, 'sujet', label=lab)
for lv, t in enumerate(['niveau 0 : 1', 'niveau 1 : 3', 'niveau 2 : 3', 'niveau 3 : 1']):
    text(ax, 2, Y[lv] + bh / 2, t, 'sujet', 's', ha='left')
save(fig, '76-064')
