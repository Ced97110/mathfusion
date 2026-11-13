import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b, _d = box, disc
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
def disc(ax, x, y, r, role='fixe', label=None, size='m', **k): return _d(ax, x, y, r, role, label=label, size=size, **k)
fig, ax = canvas(78)
rows = [(r'$f(g\,k\,g^{-1})$', 'sujet'), (r'$= f(g)\,f(k)\,f(g)^{-1}$', 'fixe'), (r"$= f(g)\,1'\,f(g)^{-1}$", 'varie'), (r"$= 1'$", 'resultat')]
ys = [62, 44, 26, 8]
for (s, r), y in zip(rows, ys):
    box(ax, 2, y, 54, 12, r, s, 'm')
for y in ys[:3]: arrow(ax, (29, y), (29, y - 6), 'fixe')
text(ax, 71, 53, 'développer', 'fixe', 's'); text(ax, 71, 35, r'$k \in$ noyau', 'varie', 's'); text(ax, 71, 17, 'simplifier', 'fixe', 's')
text(ax, 71, 70, 'départ', 'sujet', 's'); text(ax, 71, 5, 'arrivée', 'resultat', 's')
save(fig, '48-053')
