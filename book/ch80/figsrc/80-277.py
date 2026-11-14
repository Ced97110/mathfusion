import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
nodes = {1: (38, 20), 2: (22, 38), 3: (54, 38), 6: (38, 56)}
for a, b in [(1, 2), (1, 3), (2, 6), (3, 6)]:
    (xa, ya), (xb, yb) = nodes[a], nodes[b]; L = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5; dx, dy = (xb - xa) / L * 4.5, (yb - ya) / L * 4.5
    line(ax, [(xa + dx, ya + dy), (xb - dx, yb - dy)], 'fixe', lw=0.8)
role = {1: 'varie', 2: 'fixe', 3: 'fixe', 6: 'sujet'}
for d, (x, y) in nodes.items():
    disc(ax, x, y, 4.5, role[d], label=str(d))
text(ax, 45, 56, r'$10\times 1$', 'sujet', 's', ha='left')
text(ax, 16, 38, r'$3\times(-1)$', 'fixe', 's', ha='right')
text(ax, 61, 38, r'$4\times(-1)$', 'fixe', 's', ha='left')
text(ax, 45, 20, r'$1\times 1$ : remis', 'varie', 's', ha='left')
text(ax, 45, 11, 'compté deux fois', 'varie', 's', ha='left')
text(ax, 44, 3.5, r'$f(6)=10-3-4+1=4$', 'resultat', 'm')
save(fig, '80-277')
