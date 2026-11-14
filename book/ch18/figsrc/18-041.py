import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _box(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(62)
text(ax, 44, 56, 'aucun facteur commun aux 4 termes', 'limite', 's')
xs = [3, 24, 45, 66]
for x, t, r in zip(xs, [r'$x^3$', r'$3x^2$', r'$-6x$', r'$-18$'], ['sujet', 'sujet', 'autre', 'autre']): box(ax, x, 38, 18, 9, r, t)
brace(ax, 3, 42, 37, 'sujet', r'même facteur : $x^2$')
brace(ax, 45, 84, 37, 'autre', r'même facteur : $-6$')
text(ax, 44, 8, 'on regroupe deux par deux', 'varie', 's')
save(fig, '18-041')
