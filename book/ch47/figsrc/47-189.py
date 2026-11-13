import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
P = {1: (16, 44), 3: (44, 44), 9: (44, 16), 7: (16, 16)}
for k, (x, y) in P.items(): disc(ax, x, y, 6, 'sujet', label=str(k), size='l')
arrow(ax, (22, 44), (38, 44), 'varie'); arrow(ax, (44, 38), (44, 22), 'varie')
arrow(ax, (38, 16), (22, 16), 'varie'); arrow(ax, (16, 22), (16, 38), 'varie')
d = 6 / math.sqrt(2)
arrow(ax, (16 + d, 44 - d), (44 - d, 16 + d), 'autre', both=True)
text(ax, 72, 40, r'$\times 3$ : 4 pas', 'varie', 'm')
text(ax, 72, 22, r'$\times 9$ : 2 pas', 'autre', 'm')
save(fig, '47-189')
