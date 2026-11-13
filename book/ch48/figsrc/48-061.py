import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b, _d = box, disc
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
def disc(ax, x, y, r, role='fixe', label=None, size='m', **k): return _d(ax, x, y, r, role, label=label, size=size, **k)
fig, ax = canvas(60)
text(ax, 44, 55, r'multiples de 3, puis position', 'encre')
src = [0, 3, 6, 9, 12]; pos = [0, 3, 2, 1, 0]
for i, (s, p) in enumerate(zip(src, pos)):
    x = 10 + 17 * i
    box(ax, x - 7, 30, 14, 12, 'sujet', str(s), 'l')
    arrow(ax, (x, 30), (x, 20), 'varie')
    box(ax, x - 7, 6, 14, 12, 'resultat' if i < 4 else 'fixe', str(p), 'l')
text(ax, 80, 25, r'$f$', 'varie') if False else None
save(fig, '48-061')
