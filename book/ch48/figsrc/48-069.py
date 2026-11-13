import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
Z = r'\mathbb{Z}'
fig, ax = canvas(72)
text(ax, 44, 67, r"$\bar f(aK)=f(a)$", 'encre', 's')
box(ax, 2, 42, 32, 16, 'sujet', rf"$G={Z}$" + "\n1 et 5", 's')
box(ax, 54, 42, 32, 16, 'autre', rf"$G^{{\prime}}={Z}/4{Z}$" + "\nposition 1", 's')
box(ax, 22, 8, 44, 16, 'fixe', r"$G/K$" + "\npaquet {1, 5, 9, …}", 's')
arrow(ax, (34, 50), (54, 50), 'sujet'); text(ax, 44, 54, r"$f$", 'sujet', 'm')
arrow(ax, (14, 42), (28, 24), 'varie'); text(ax, 15, 31, r"$\nu$", 'varie', 'm')
arrow(ax, (60, 24), (74, 42), 'resultat'); text(ax, 73, 31, r"$\bar f$", 'resultat', 'm')
text(ax, 12, 4, rf"$K=4{Z}$ normal", 'fixe', 's')
text(ax, 75, 12, r"$\bar f$ injectif", 'resultat', 's')
save(fig, '48-069')
