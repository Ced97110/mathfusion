import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b, _d = box, disc
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
def disc(ax, x, y, r, role='fixe', label=None, size='m', **k): return _d(ax, x, y, r, role, label=label, size=size, **k)
fig, ax = canvas(62)
xs = [3, 33, 60]; ws = [20, 20, 25]
text(ax, 13, 55, r'$a \in G$', 'sujet'); text(ax, 43, 55, r'$f(a)$', 'varie'); text(ax, 72.5, 55, r"$f(a) = 1'$ ?", 'encre')
for y, a, im, ok in [(38, '8', '0', True), (18, '6', '2', False)]:
    box(ax, xs[0], y - 6, ws[0], 12, 'sujet', a, 'l')
    box(ax, xs[1], y - 6, ws[1], 12, 'varie', im, 'l')
    arrow(ax, (xs[0] + ws[0], y), (xs[1], y), 'varie')
    arrow(ax, (xs[1] + ws[1], y), (xs[2], y), 'varie')
    box(ax, xs[2], y - 6, ws[2], 12, 'resultat' if ok else 'limite', 'gardé' if ok else 'rejeté', 'm')
text(ax, 44, 4, r'noyau = éléments gardés', 'resultat')
save(fig, '48-049')
