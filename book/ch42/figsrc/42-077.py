import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **kw): return _box(ax, x, y, w, h, role, label=label, size=size, **kw)
fig, ax = canvas(76)
box(ax, 2, 2, 84, 70, 'fixe'); text(ax, 84, 68, 'entiers', 'fixe', 's', ha='right')
disc(ax, 36, 36, 26, 'sujet'); disc(ax, 30, 30, 12, 'varie')
text(ax, 36, 66, r'$Q$ : les pairs', 'sujet', 's')
text(ax, 30, 36, 'multiples de 4', 'varie', 's'); text(ax, 30, 29, r'$8$', 'varie', 'm'); text(ax, 30, 22, r'$P$', 'varie', 's')
text(ax, 52, 47, r'$6$', 'sujet', 'm'); text(ax, 50, 42, r'pair, hors de $P$', 'sujet', 's')
text(ax, 72, 20, r'$7$', 'fixe', 'm'); text(ax, 72, 14, r'hors de $Q$', 'fixe', 's')
save(fig, '42-077')
