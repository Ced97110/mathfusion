import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 2, 4, 84, 50, 'sujet', label=None)
text(ax, 44, 48, r'$\mathrm{End}\ \mathbb{Z}$', 'sujet', 'xl', weight='bold')
names = ['tripler', 'doubler', 'ne rien changer', 'tout envoyer sur 0']
pos = [(8, 26), (47, 26), (8, 10), (47, 10)]
for (x, y), n in zip(pos, names):
    box(ax, x, y, 34, 10, 'fixe', label=n, size='s')
text(ax, 44, 59, 'un seul nom pour toutes ces règles', 'sujet', 's')
save(fig, '57-041')
