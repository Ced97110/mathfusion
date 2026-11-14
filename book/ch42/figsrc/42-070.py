import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **kw): return _box(ax, x, y, w, h, role, label=label, size=size, **kw)
fig, ax = canvas(78)
text(ax, 44, 73, 'départ', 'fixe', 's')
box(ax, 14, 56, 60, 12, 'fixe', r'$p$ : on part de $4k$', 'm')
arrow(ax, (44, 56), (44, 34), 'varie'); text(ax, 48, 45, r'$4k=2\times(2k)$', 'varie', 'm', ha='left')
box(ax, 14, 22, 60, 12, 'sujet', r'$q$ : il est pair', 'm', lw=1.8)
text(ax, 44, 17, r'$q$ est la partie à établir', 'varie', 's', weight='bold')
text(ax, 44, 10, r'$q$ atteinte : preuve finie', 'resultat', 's', weight='bold')
text(ax, 44, 4.5, r'pair : de la forme $2\times$ entier', 'fixe', 's')
save(fig, '42-070')
