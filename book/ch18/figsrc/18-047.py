import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _box(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(78)
box(ax, 6, 52, 18, 18, 'sujet', r'$a^2$', 'l'); text(ax, 15, 48, r'$a$', 'sujet', 'm'); text(ax, 27, 61, r'$a$', 'sujet', 'm')
text(ax, 62, 61, r'$a^2 = a \times a$', 'sujet', 'm')
u = 3.5
def sq(x, y, n, extra=False):
    for i in range(n):
        for j in range(n): box(ax, x + i * u, y + j * u, u, u, 'sujet', r=0.1, lw=0.5)
    if extra: box(ax, x + n * u, y, u, u, 'limite', r=0.1, lw=0.5)
sq(6, 18, 3); sq(30, 18, 4); sq(56, 18, 3, True)
text(ax, 11, 11, r'$3^2=9$', 'sujet', 's'); text(ax, 37, 11, r'$4^2=16$', 'sujet', 's'); text(ax, 66, 11, '10 : pas un carré', 'limite', 's')
save(fig, '18-047')
