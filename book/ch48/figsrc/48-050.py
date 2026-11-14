import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b, _d = box, disc
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
def disc(ax, x, y, r, role='fixe', label=None, size='m', **k): return _d(ax, x, y, r, role, label=label, size=size, **k)
fig, ax = canvas(62)
text(ax, 44, 57, r'$f$ n’est pas un homomorphisme', 'limite')
X = [10 + 17 * i for i in range(5)]
for i, x in enumerate(X):
    disc(ax, x, 32, 5, 'sujet' if i < 2 else 'fixe', str(i), 'l')
brace(ax, X[0] - 5, X[1] + 5, 25, 'sujet', r'noyau $\{0 ; 1\}$', True, 'm')
arrow(ax, (X[1] + 1, 38), (X[2] - 1, 38), 'limite', curve=-0.6)
text(ax, (X[1] + X[2]) / 2, 47, '1 + 1 = 2', 'limite')
text(ax, X[2] + 8, 20, '2 sort du noyau', 'limite')
save(fig, '48-050')
