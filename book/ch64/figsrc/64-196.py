import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 22, 79, '5 chapitres fournis', 'autre', 'm', weight='bold')
text(ax, 72, 79, 'ce chapitre', 'sujet', 'm', weight='bold')
rows = ('ch. 46 : cycles, $A_n$', 'ch. 47 : normaux', 'ch. 48 : isomorphismes', 'ch. 50 : centre, Cauchy', 'ch. 56 : Eisenstein')
ys = [8 + i * 13.5 for i in range(5)][::-1]
box(ax, 58, 8, 28, 61, 'sujet', label=None)
text(ax, 72, 38.5, 'chapitre\n64', 'sujet', 'l', weight='bold')
for y, t in zip(ys, rows):
    box(ax, 2, y, 44, 11, 'autre', label=t, size='s')
    arrow(ax, (47, y + 5.5), (57, y + 5.5), 'varie')
save(fig, '64-196')
