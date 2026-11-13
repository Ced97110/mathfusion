import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **kw): return _box(ax, x, y, w, h, role, label=label, size=size, **kw)
fig, ax = canvas(72)
text(ax, 2, 69, 'sans verbe : pas un énoncé', 'limite', 's', ha='left')
box(ax, 2, 52, 50, 12, 'sujet', r'$3+56-13+8/2$', 'm'); arrow(ax, (54, 58), (61, 58), 'fixe')
box(ax, 62, 52, 24, 12, 'fixe', r'nombre $50$', 'm')
text(ax, 2, 43, 'avec un verbe : un énoncé', 'resultat', 's', ha='left')
box(ax, 2, 24, 26, 12, 'sujet', 'expression', 'm'); text(ax, 32, 30, '+', 'encre', 'l')
box(ax, 36, 24, 22, 12, 'varie', 'un verbe', 'm'); arrow(ax, (59.5, 30), (63.5, 30), 'resultat')
box(ax, 64, 24, 22, 12, 'resultat', 'énoncé', 'm')
text(ax, 47, 17, '« est égale à 50 »', 'varie', 's')
save(fig, '42-068')
