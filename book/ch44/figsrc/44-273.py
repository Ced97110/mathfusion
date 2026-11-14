import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 18, 52, r'$S_2$ : 2 façons', 'autre', 'm', weight='bold')
text(ax, 18, 46, '2 racines', 'fixe', 's')
for i, p in enumerate(['1 2', '2 1']):
    box(ax, 9, 31 - i * 11, 18, 9, 'autre', label=p)
text(ax, 62, 52, r'$S_3$ : 6 façons', 'sujet', 'm', weight='bold')
text(ax, 62, 46, '3 racines', 'fixe', 's')
perms = ['1 2 3', '1 3 2', '2 1 3', '2 3 1', '3 1 2', '3 2 1']
for i, p in enumerate(perms):
    box(ax, 46 + (i % 2) * 20, 31 - (i // 2) * 11, 18, 9, 'sujet', label=p)
save(fig, '44-273')
