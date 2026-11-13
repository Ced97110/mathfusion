import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role="fixe", label=None, size="m", **k): return _box(ax, x, y, w, h, role, True, label, size, **k)
fig, ax = canvas(64)
text(ax, 22, 58, 'facteur commun', 'resultat', 's'); text(ax, 66, 58, 'aucun facteur', 'limite', 's')
box(ax, 3, 38, 38, 12, 'sujet', r'$\sin x - \sin^2 x$', 'm')
arrow(ax, (22, 37), (22, 26), 'varie')
text(ax, 22, 32, 'on met en facteur', 'varie', 's')
box(ax, 3, 11, 38, 12, 'resultat', r'$\sin x\,(1-\sin x)$', 'm')
box(ax, 47, 38, 38, 12, 'sujet', r'$\sin x + \cos x$', 'm')
box(ax, 47, 11, 38, 12, 'limite', r'rien à sortir', 'm')
text(ax, 66, 30, '(parties différentes)', 'limite', 's')
save(fig, '31-119')
