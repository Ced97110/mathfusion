import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _box(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(66)
text(ax, 44, 61, r'$x^3 + 3x^2 - 6x - 18$', 'sujet', 'l')
xs = [3, 24, 45, 66]
text(ax, 3, 52, 'nombres devant', 'fixe', 's', ha='left')
for x, c in zip(xs, ['1', '3', r'$-6$', r'$-18$']): box(ax, x, 41, 18, 8, 'fixe', c)
text(ax, 3, 34, 'lettre', 'fixe', 's', ha='left')
for x, c, r in zip(xs, [r'$x^3$', r'$x^2$', r'$x$', 'aucune'], ['resultat'] * 3 + ['limite']): box(ax, x, 23, 18, 8, r, c, 's')
text(ax, 44, 15, 'seul 1 divise les quatre nombres', 'fixe', 's')
text(ax, 44, 7, 'aucun facteur commun à tous', 'limite', 's')
save(fig, '18-040')
