import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(68)
text(ax, 44, 64, r'image de $n \mapsto 2n$ dans $G^{\prime}$', 'sujet', 'm')
X = [10 + 22 * i for i in range(4)]
for i, x in enumerate(X): box(ax, x - 8, 26, 16, 14, 'sujet' if i % 2 == 0 else 'fixe', str(i), 'l')
arrow(ax, (X[2] - 3, 41.5), (X[0] + 3, 41.5), 'sujet', curve=0.5)
text(ax, X[1], 56, '2 + 2 = 0 : reste dedans', 'sujet', 's')
text(ax, X[0], 18, 'neutre dedans', 'sujet', 's')
text(ax, X[2], 18, r'opposé $-2 = 2$', 'sujet', 's')
text(ax, 44, 6, r'sous-groupe de $G^{\prime}$', 'resultat', 'm', weight='bold')
save(fig, '48-058')
