import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
dims = [2, 1, 0]
for k, y in enumerate((38, 26, 14)):
    text(ax, 2, y + 4, f'k = {k} : {dims[k]}', 'resultat', 's', ha='left')
    for c in range(2):
        if c < dims[k]:
            box(ax, 22 + 9 * c, y, 8, 8, 'sujet', r=0.4)
        elif c == 0:
            box(ax, 22, y, 8, 8, 'fixe', fill=False, dash=True, r=0.4)
for ytop in (41, 29):
    line(ax, [(39, ytop), (41, ytop), (41, ytop - 10), (39, ytop - 10)], 'fixe')
box(ax, 52, 31, 34, 8, 'varie', label='exposant 1 : 2 − 1 = 1', size='s')
box(ax, 52, 19, 34, 8, 'varie', label='exposant 2 : 1 − 0 = 1', size='s')
arrow(ax, (41, 36), (51, 35), 'varie')
arrow(ax, (41, 24), (51, 23), 'varie')
box(ax, 52, 3, 34, 9, 'resultat', label='listes e et f : 1 et 2', size='s')
arrow(ax, (69, 19), (69, 12.5), 'resultat')
save(fig, '60-069')
