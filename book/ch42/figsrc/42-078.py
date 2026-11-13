import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **kw): return _box(ax, x, y, w, h, role, label=label, size=size, **kw)
fig, ax = canvas(62)
text(ax, 44, 58, r'départ : $p\Rightarrow q$', 'fixe', 'm')
box(ax, 2, 40, 32, 12, 'sujet', 'multiple de 4', 'm'); arrow(ax, (36, 46), (52, 46), 'fixe'); box(ax, 54, 40, 32, 12, 'autre', 'pair', 'm')
arrow(ax, (18, 39), (70, 25), 'varie'); arrow(ax, (70, 39), (18, 25), 'varie')
box(ax, 2, 12, 32, 12, 'autre', 'pair', 'm'); arrow(ax, (36, 18), (52, 18), 'varie'); box(ax, 54, 12, 32, 12, 'sujet', 'multiple de 4', 'm')
text(ax, 44, 5, r'réciproque : $q\Rightarrow p$', 'varie', 'm')
save(fig, '42-078')
