import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **kw): return _box(ax, x, y, w, h, role, label=label, size=size, **kw)
fig, ax = canvas(48)
box(ax, 2, 32, 30, 12, 'sujet', r'$a=0$', 'm'); arrow(ax, (33.5, 38), (40.5, 38), 'fixe')
box(ax, 42, 32, 44, 12, 'fixe', r'$2x-6=0$ : $x=3$', 'm')
arrow(ax, (17, 32), (17, 22), 'varie')
box(ax, 2, 10, 30, 12, 'varie', r'formule : $\div 2a$', 's'); arrow(ax, (33.5, 16), (40.5, 16), 'limite')
box(ax, 42, 10, 44, 12, 'limite', r'$2a=0$ : sans sens', 'm')
text(ax, 44, 4, r'donc l’hypothèse : $a\neq 0$', 'sujet', 's')
save(fig, '42-074')
