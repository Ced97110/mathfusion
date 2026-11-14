import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 68, 'une même chaîne', 'fixe', 'm', weight='bold')
for i, n in enumerate(('8', '4', '2', '1')):
    y = 50 - 13 * i
    box(ax, 34, y, 20, 9, 'fixe', label=n, size='m')
    if i < 3: arrow(ax, (44, y - 0.5), (44, y - 3.5), 'fixe')
line(ax, [(31, 59.5), (29, 59.5), (29, 11.5), (31, 11.5)], 'sujet')
line(ax, [(57, 59.5), (59, 59.5), (59, 11.5), (57, 11.5)], 'autre')
box(ax, 2, 31, 25, 11, 'sujet', label='suite normale', size='s')
text(ax, 14.5, 25, 'ce chapitre', 'sujet', 's')
box(ax, 61, 31, 25, 11, 'autre', label='suite sous-normale', size='s')
text(ax, 73.5, 25, 'chez Judson', 'autre', 's')
save(fig, '64-032')
