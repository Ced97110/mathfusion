import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b, _d = box, disc
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
def disc(ax, x, y, r, role='fixe', label=None, size='m', **k): return _d(ax, x, y, r, role, label=label, size=size, **k)
fig, ax = canvas(66)
X = [8 + 14.5 * i for i in range(6)]
for i, x in enumerate(X):
    r = 'sujet' if i in (0, 4) else ('varie' if i in (1, 5) else 'fixe')
    disc(ax, x, 40, 4.5, r, str(i), 'm')
text(ax, 44, 61, r'$f(1) = f(5)$', 'varie')
arrow(ax, (X[1], 34.5), (X[5], 34.5), 'varie', curve=0.35)
text(ax, 44, 20, r'$-1 + 5 = 4$', 'varie')
text(ax, X[4], 51, 'noyau', 'sujet', 's'); text(ax, X[0], 51, 'noyau', 'sujet', 's')
text(ax, 44, 6, r'$4 \neq 0$ est dans le noyau', 'limite')
save(fig, '48-056')
