import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **kw): return _box(ax, x, y, w, h, role, label=label, size=size, **kw)
fig, ax = canvas(62)
text(ax, 50, 57, r'$p$ : l’hypothèse', 'sujet', 'l')
text(ax, 7, 44, 'si', 'fixe', 'm'); box(ax, 14, 38, 72, 12, 'sujet', 'un nombre est multiple de 4', 'm')
arrow(ax, (50, 38), (50, 26), 'varie'); text(ax, 53, 32, 'supposée vraie', 'varie', 's', ha='left')
text(ax, 7, 20, 'alors', 'fixe', 's'); box(ax, 14, 14, 72, 12, 'fixe', 'il est pair', 'm')
text(ax, 50, 7, r'$q$ : ce qui suit', 'fixe', 's')
save(fig, '42-069')
