import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b, _d = box, disc
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
def disc(ax, x, y, r, role='fixe', label=None, size='m', **k): return _d(ax, x, y, r, role, label=label, size=size, **k)
fig, ax = canvas(84)
text(ax, 20, 79, r'$H$ : entiers pairs', 'sujet', 's'); text(ax, 68, 79, r'$f(H)$', 'resultat', 's')
rows = [(62, 'a = 2', r'$x = f(2)$', 'sujet'), (42, 'b = 4', r'$y = f(4)$', 'sujet'), (16, 'a − b = −2', r'$x - y = f(-2)$', 'varie')]
for y, l, r, role in rows:
    box(ax, 2, y, 36, 12, role, l, 'm'); box(ax, 50, y, 36, 12, 'resultat', r, 'm')
    arrow(ax, (38, y + 6), (50, y + 6), 'varie'); text(ax, 44, y + 10, r'$f$', 'varie', 's')
text(ax, 20, 8, '−2 est pair : dans H', 'varie', 's')
save(fig, '48-060')
