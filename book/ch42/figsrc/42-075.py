import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **kw): return _box(ax, x, y, w, h, role, label=label, size=size, **kw)
fig, ax = canvas(62)
box(ax, 4, 38, 22, 18, 'sujet', r'$p$', 'xl'); box(ax, 32, 38, 24, 18, 'varie', r'$\Rightarrow$', 'xl'); box(ax, 62, 38, 22, 18, 'resultat', r'$q$', 'xl')
text(ax, 15, 33, 'après « si »', 'sujet', 's'); text(ax, 44, 33, 'implique', 'varie', 's'); text(ax, 73, 33, 'après « alors »', 'resultat', 's')
text(ax, 44, 24, 'ici :', 'fixe', 's')
box(ax, 2, 6, 38, 12, 'sujet', r'$n$ multiple de 4', 's'); arrow(ax, (41.5, 12), (46.5, 12), 'varie')
box(ax, 48, 6, 38, 12, 'resultat', r'$n$ pair', 's')
save(fig, '42-075')
