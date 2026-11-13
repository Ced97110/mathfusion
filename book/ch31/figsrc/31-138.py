import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def lbox(ax, x, y, w, h, role, label=None, **k): return box(ax, x, y, w, h, role, label=label, **k)
fig, ax = canvas(60)
text(ax, 44, 55, 'deux rapports : cos et sin', 'encre', 's')
lbox(ax, 8, 38, 20, 11, 'varie', r'$\cos^2 x$'); text(ax, 33, 43.5, '=', size='l'); lbox(ax, 38, 38, 26, 11, 'fixe', r'$1-\sin x$')
arrow(ax, (18, 37), (18, 25), 'varie'); text(ax, 52, 31, r'remplacer $\cos^2 x$', 'varie', 's')
lbox(ax, 4, 14, 28, 11, 'resultat', r'$1-\sin^2 x$'); text(ax, 37, 19.5, '=', size='l'); lbox(ax, 42, 14, 26, 11, 'fixe', r'$1-\sin x$')
text(ax, 44, 6, 'un seul rapport : sin', 'resultat', 's')
save(fig, '31-138')
