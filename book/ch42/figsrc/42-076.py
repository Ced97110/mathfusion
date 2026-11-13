import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **kw): return _box(ax, x, y, w, h, role, label=label, size=size, **kw)
fig, ax = canvas(68)
disc(ax, 44, 30, 26, 'sujet'); disc(ax, 44, 28, 13, 'varie')
text(ax, 44, 61, r'$Q$ : les pairs', 'sujet', 'm'); text(ax, 2, 61, r'$P\subseteq Q$', 'resultat', 'm', ha='left')
text(ax, 44, 35, r'$P$ : multiples de 4', 'varie', 's'); text(ax, 38, 26, r'$8$', 'varie', 'm'); text(ax, 50, 26, r'$12$', 'varie', 'm')
save(fig, '42-076')
