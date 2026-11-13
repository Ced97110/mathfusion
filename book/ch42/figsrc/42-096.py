import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 4, 86, 'pour tout x, il existe y', 'resultat', 'm', ha='left', weight='bold')
for i, (a, b) in enumerate([(5, 6), (100, 101)]):
    y = 70 - i * 12
    box(ax, 10, y - 4, 16, 8, 'sujet', label=f'x = {a}', size='s')
    box(ax, 60, y - 4, 20, 8, 'resultat', label=f'y = {b}', size='s')
    arrow(ax, (26, y), (60, y), 'resultat')
text(ax, 43, 74, 'y = x + 1', 'resultat', 's')
text(ax, 4, 44, 'il existe y, pour tout x', 'limite', 'm', ha='left', weight='bold')
box(ax, 58, 22, 22, 10, 'autre', label='y = 1000', size='s')
box(ax, 10, 30, 18, 8, 'sujet', label='x = 5', size='s')
box(ax, 10, 12, 20, 8, 'limite', label='x = 1000', size='s')
arrow(ax, (28, 34), (58, 29), 'resultat'); arrow(ax, (30, 16), (58, 25), 'limite')
text(ax, 44, 4, '1000 > 1000 : faux', 'limite', 's')
save(fig, '42-096')
