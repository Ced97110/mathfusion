import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cols = (16, 44, 72)
for c, t, r in zip(cols, ('trop peu', 'juste', 'trop'), ('limite', 'resultat', 'limite')):
    text(ax, c, 56, t, r, 'l', weight='bold')
for i in range(5):
    y = 44 - 6 * i
    if i % 2 == 0: box(ax, 5, y, 22, 4, 'sujet', r=0.5)
    else: box(ax, 5, y, 22, 4, 'limite', fill=False, dash=True, r=0.5, label='?', size='s')
    box(ax, 33, y, 22, 4, 'resultat', r=0.5)
for i in range(12):
    box(ax, 61, 46 - 2.6 * i, 22, 1.8, 'varie', r=0.3)
text(ax, 16, 10, 'il ne suit plus', 'limite', 's'); text(ax, 44, 10, 'il vérifie chaque ligne', 'resultat', 's')
text(ax, 72, 10, 'il s’ennuie', 'limite', 's')
save(fig, '42-105')
