import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **kw): return _box(ax, x, y, w, h, role, label=label, size=size, **kw)
fig, ax = canvas(54)
for x, s in ((8, 'nombre'), (32, 'hypothèse'), (72, 'l’énoncé')): text(ax, x, 49, s, 'fixe', 's')
for y, n, hr, ht, rr, rt, nr in ((28, '7', 'limite', 'non multiple de 4', 'fixe', 'ne dit rien', 'fixe'),
                                  (8, '8', 'resultat', 'multiple de 4', 'resultat', '8 est pair', 'sujet')):
    box(ax, 2, y, 12, 12, nr, '$' + n + '$', 'l')
    box(ax, 18, y, 34, 12, hr, ht, 's'); arrow(ax, (53, y + 6), (59, y + 6), 'fixe')
    box(ax, 60, y, 26, 12, rr, rt, 's')
save(fig, '42-073')
