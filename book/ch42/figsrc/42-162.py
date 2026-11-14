import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ys = [54, 34, 14]
for y, t, c in zip(ys, [r'$S\cup T$', r'$S\cap T$', r'$S\times T$'], ['autre', 'autre', 'sujet']):
    text(ax, 4, y, t, c, 'm', ha='left')
for i, n in enumerate(['1', '2', '3', 'a', r'$b$']):
    disc(ax, 33 + 9 * i, ys[0], 3.6, 'autre', label=n, size='s')
box(ax, 30, ys[1] - 5, 40, 10, 'autre', fill=False, dash=True)
for i in range(3):
    for j in range(2):
        disc(ax, 36 + 12 * i, ys[2] - 4 + 8 * j, 2.2, 'sujet')
for y, t, c in zip(ys, ['5 objets', '0 objet', '6 couples'], ['autre', 'autre', 'sujet']):
    text(ax, 86, y, t, c, 's', ha='right')
save(fig, '42-162')
