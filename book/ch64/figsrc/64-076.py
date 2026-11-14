import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
X = lambda s: 2 + s * 15.5
def chain(y, vals, slots, role, title, facs, ty, fy):
    text(ax, 44, ty, title, role, 's', weight='bold')
    for v, s in zip(vals, slots):
        box(ax, X(s), y, 11, 8, role, label=v)
    for a, b in zip(slots, slots[1:]):
        arrow(ax, (X(a) + 11, y + 4), (X(b), y + 4), 'fixe', lw=0.8)
    text(ax, 44, fy, facs, 'encre', 's')
chain(46, ['24', '12', '4', '1'], [0, 1, 2, 4], 'fixe', 'suite normale : 3 facteurs', 'facteurs 2, 3, 4', 60, 40)
chain(20, ['24', '12', '4', '2', '1'], [0, 1, 2, 3, 4], 'resultat', 'composition : 4 facteurs', 'facteurs 2, 3, 2, 2', 34, 15)
text(ax, 44, 5.5, 'Jordan-Hölder : compositions,\nmêmes longueur et facteurs', 'sujet', 's', weight='bold')
save(fig, '64-076')
