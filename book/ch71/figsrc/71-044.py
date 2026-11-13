import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 8, 54, 72, 10, 'autre', label=r'$3e_1^* + 2e_2^* = 0$ partout')
arrow(ax, (44, 53), (44, 42), 'varie'); text(ax, 48, 47.5, r'on applique à $e_1$', 'varie', 's', ha='left')
box(ax, 8, 31, 72, 10, 'sujet', label=r'$3\times 1 + 2\times 0 = 3$')
arrow(ax, (44, 30), (44, 19), 'limite')
box(ax, 8, 8, 72, 10, 'limite', label=r'$3 \neq 0$ : impossible')
save(fig, '71-044')
