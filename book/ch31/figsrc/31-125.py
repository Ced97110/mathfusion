import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role="fixe", label=None, size="m", **k): return _box(ax, x, y, w, h, role, True, label, size, **k)
fig, ax = canvas(74)
box(ax, 3, 52, 38, 16, 'fixe', r'$\frac{\cos x}{1-\sin x}$', 'm'); box(ax, 47, 52, 38, 16, 'fixe', r'$\frac{1+\sin x}{\cos x}$', 'm')
text(ax, 22, 72, 'gauche : en bas', 'sujet', 's'); text(ax, 66, 72, 'droite : en haut', 'autre', 's')
arrow(ax, (22, 51), (22, 43), 'sujet'); arrow(ax, (66, 51), (66, 43), 'autre')
box(ax, 8, 31, 28, 11, 'sujet', r'$1-\sin x$', 'm'); box(ax, 52, 31, 28, 11, 'autre', r'$1+\sin x$', 'm')
arrow(ax, (37, 36.5), (51, 36.5), 'varie', both=True)
text(ax, 44, 41.5, 'signe opposé', 'varie', 's')
brace(ax, 8, 80, 29, 'varie', 'conjuguées')
box(ax, 8, 4, 72, 10, 'resultat', r'produit : $1-\sin^2 x$', 'm')
save(fig, '31-125')
