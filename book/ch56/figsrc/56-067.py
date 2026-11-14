import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
rows = [(48, ['$2$', '$2$', '$3$'], ['sujet'] * 3, ''),
        (28, ['$3$', '$2$', '$2$'], ['varie'] * 3, 'autre ordre'),
        (8, ['$(-2)$', '$3$', '$(-2)$'], ['varie', 'sujet', 'varie'], '$-2$ associé à $2$')]
for y, labs, roles, com in rows:
    text(ax, 3, y + 5, '$12=$', 'encre', ha='left')
    for i, (l, r) in enumerate(zip(labs, roles)):
        box(ax, 17 + i * 14, y, 11, 10, r, label=l)
    if com:
        text(ax, 60, y + 5, com, 'varie', 's', ha='left')
save(fig, '56-067')
