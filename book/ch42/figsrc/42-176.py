import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cols = [26, 42, 58]; rows = {'a': 40, 'b': 24}
box(ax, 18, 16, 48, 32, 'fixe', fill=False, dash=True)
text(ax, 42, 56, r'$S\times T$ : 6 couples', 'fixe', 'm')
for x, n in zip(cols, '123'): text(ax, x, 10, n, 'sujet', 's')
for n, y in rows.items(): text(ax, 10, y, rf'${n}$', 'autre', 's')
chosen = {(0, 'a'), (1, 'a'), (2, 'b')}
for i, x in enumerate(cols):
    for n, y in rows.items():
        if (i, n) in chosen: disc(ax, x, y, 2.8, 'sujet')
        else: disc(ax, x, y, 1.6, 'fixe', fill=False)
arrow(ax, (72, 24), (62, 24), 'sujet'); text(ax, 77, 31, 'graphe :', 'sujet', 's'); text(ax, 77, 27.5, '3 couples', 'sujet', 's')
save(fig, '42-176')
