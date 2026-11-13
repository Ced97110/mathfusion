import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b, _d = box, disc
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
def disc(ax, x, y, r, role='fixe', label=None, size='m', **k): return _d(ax, x, y, r, role, label=label, size=size, **k)
fig, ax = canvas(92)
text(ax, 44, 87, r'$\times 3$ : noyau $\{0\}$', 'sujet')
for i in range(4):
    x = 3 + 21 * i
    box(ax, x, 62, 19, 16, 'sujet', None, dash=False)
    disc(ax, x + 9.5, 70, 2.2, 'sujet')
text(ax, 44, 55, '1 élément par fibre', 'sujet', 's')
text(ax, 44, 42, r'bouton : noyau $4\mathbb{Z}$', 'varie')
for i in range(4):
    x = 3 + 21 * i
    box(ax, x, 12, 19, 25 , 'varie', None)
    for j in range(4): disc(ax, x + 9.5, 17 + 5 * j, 1.8, 'varie')
text(ax, 44, 5, 'une infinité par fibre', 'varie', 's')
save(fig, '48-057')
