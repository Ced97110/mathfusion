import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b, _d = box, disc
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
def disc(ax, x, y, r, role='fixe', label=None, size='m', **k): return _d(ax, x, y, r, role, label=label, size=size, **k)
fig, ax = canvas(66)
vals = [-8, -4, 0, 4, 8, 12]; X = {v: 10 + 13.2 * i for i, v in enumerate(vals)}
for v in vals: disc(ax, X[v], 34, 4.5, 'resultat' if v == 0 else 'sujet', str(v), 'm')
text(ax, 44, 61, 'noyau = multiples de 4', 'sujet')
text(ax, X[0], 49, r'neutre : $0 \in$ noyau', 'resultat')
arrow(ax, (X[4], 40), (X[12] - 1, 40), 'varie', curve=-0.5); arrow(ax, (X[4] - 6, 40), (X[8] - 2, 40), 'varie', curve=0) if False else None
arrow(ax, (X[4], 39.5), (X[12] - 2, 39.5), 'varie', curve=-0.7)
arrow(ax, (X[8] if False else X[4], 28), (X[-8] + 2, 28), 'varie', curve=-0.4) if False else None
arrow(ax, (X[8] - 1, 28), (X[-8] + 1, 28), 'varie', curve=-0.35)
text(ax, 60, 52, '4 + 8 = 12', 'varie')
text(ax, 42, 12, r'opposé de 8 : $-8$', 'varie')
save(fig, '48-051')
