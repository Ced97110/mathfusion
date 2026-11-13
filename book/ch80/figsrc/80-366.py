import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
nodes = {'T': (44, 26, r'$T=\{2\}$ : 8', 'sujet'), 'a': (22, 50, r'$\{2,3\}$ : 4', 'varie'),
         'b': (66, 50, r'$\{2,5\}$ : 2', 'varie'), 'c': (44, 74, r'$\{2,3,5\}$ : 1', 'varie')}
for p, q in [('T', 'a'), ('T', 'b'), ('a', 'c'), ('b', 'c')]:
    line(ax, [(nodes[p][0], nodes[p][1] + 5), (nodes[q][0], nodes[q][1] - 5)], 'fixe')
for k, (x, y, s, r) in nodes.items(): box(ax, x - 12, y - 5, 24, 10, r, label=s, size='s')
arrow(ax, (86, 31), (86, 70), 'varie'); text(ax, 82, 50, 'au-dessus', 'varie', 's', rot=90)
text(ax, 44, 88, r'$g(T)=8+4+2+1=15$', 'resultat', 'm')
text(ax, 44, 10, r'chaque $U$ au-dessus de $T$ : $f(U)$', 'fixe', 's')
save(fig, '80-366')
