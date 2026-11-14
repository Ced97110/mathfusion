import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
box(ax, 10, 14, 68, 58, 'fixe')
text(ax, 44, 66, r'$S = \{1, 2, 3, 4\}$', 'fixe', 'm')
P = {1: (30, 50), 2: (58, 50), 3: (58, 28), 4: (30, 28)}
for k, (x, y) in P.items(): disc(ax, x, y, 4.5, 'sujet', label=str(k), size='l')
arrow(ax, (34.8, 50), (53.2, 50), 'varie'); arrow(ax, (58, 45.2), (58, 32.8), 'varie')
arrow(ax, (53.2, 28), (34.8, 28), 'varie'); arrow(ax, (30, 32.8), (30, 45.2), 'varie')
text(ax, 44, 39, 'quart de tour', 'varie', 's')
text(ax, 44, 6, r'départ = arrivée = $S$', 'sujet', 'm')
save(fig, '44-032')
