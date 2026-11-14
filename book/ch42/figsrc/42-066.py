import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **kw): return _box(ax, x, y, w, h, role, label=label, size=size, **kw)
fig, ax = canvas(58)
box(ax, 4, 32, 22, 14, 'sujet', r'$x=4$', 'l'); arrow(ax, (27, 39), (35, 39), 'varie')
text(ax, 31, 43.5, r'$2x$', 'varie', 's')
box(ax, 36, 32, 20, 14, 'varie', r'$8$', 'l'); text(ax, 63, 39, r'$\neq$', 'limite', 'xl')
box(ax, 70, 32, 14, 14, 'fixe', r'$6$', 'l')
text(ax, 15, 51, 'on essaie', 'sujet', 's'); text(ax, 46, 51, r'ce que vaut $2x$', 'varie', 's'); text(ax, 77, 51, 'énoncé', 'fixe', 's')
arrow(ax, (63, 32), (63, 18), 'limite')
box(ax, 24, 6, 60, 12, 'limite', 'énoncé faux', 'm')
save(fig, '42-066')
