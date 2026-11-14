import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _box(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(76)
box(ax, 3, 60, 36, 9, 'sujet', r'$x^2\,(x+3)$'); box(ax, 49, 60, 36, 9, 'fixe', r'$-6x-18$')
text(ax, 21, 74, '1er groupe', 'sujet', 's'); text(ax, 67, 74, '2e groupe', 'fixe', 's')
arrow(ax, (56, 59), (40, 46), 'varie'); text(ax, 24, 53, 'retirer $6$', 'varie', 's')
arrow(ax, (72, 59), (72, 46), 'varie'); text(ax, 74, 53, r'retirer $-6$', 'varie', 's', ha='left')
box(ax, 3, 36, 36, 9, 'limite', r'$6\,(-x-3)$'); box(ax, 49, 36, 36, 9, 'resultat', r'$-6\,(x+3)$')
text(ax, 21, 28, r'$-x-3 \neq x+3$', 'limite', 's'); text(ax, 67, 28, r'même bloc $(x+3)$', 'resultat', 's')
text(ax, 44, 16, 'le signe se choisit', 'fixe', 's'); text(ax, 44, 9, "d'après l'autre groupe", 'fixe', 's')
save(fig, '18-045')
