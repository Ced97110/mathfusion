import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ys = [44, 33, 22]
text(ax, 17, 68, 'générateurs en lignes', 'sujet', 's')
text(ax, 62, 68, 'forme normale', 'varie', 's')
for y, v in zip(ys, ['(2, 4)', '(4, 2)', '(6, 6)']):
    box(ax, 4, y, 26, 9, 'sujet', label=v)
arrow(ax, (32, 38.5), (44, 38.5), 'varie', lw=1.3)
for y, v, role in zip(ys, ['(2, 0)', '(0, 6)', '(0, 0)'], ['varie', 'varie', 'fixe']):
    box(ax, 50, y, 26, 9, role, label=v, dash=(role == 'fixe'))
box(ax, 47.5, 30.5, 31, 25, 'resultat', fill=False, lw=1.4)
text(ax, 63, 55 + 3.5, 'cadre : lignes non nulles', 'resultat', 's')
text(ax, 63, 17, 'ligne nulle : superflue', 'fixe', 's')
text(ax, 17, 17, r'$(6,\,6)=(2,\,4)+(4,\,2)$', 'encre', 's')
box(ax, 14, 2, 60, 9, 'resultat', label='base : les lignes du cadre', size='s')
save(fig, '59-141')
