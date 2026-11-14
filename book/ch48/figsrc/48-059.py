import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b, _d = box, disc
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
def disc(ax, x, y, r, role='fixe', label=None, size='m', **k): return _d(ax, x, y, r, role, label=label, size=size, **k)
fig, ax = canvas(74)
text(ax, 44, 69, r'bouton : im $f = G^{\prime}$', 'sujet')
text(ax, 44, 32, r'double : im $f \subset G^{\prime}$', 'varie')
for base, both in [(40, True), (3, False)]:
    box(ax, 2, base - 1, 84, 20, 'fixe', fill=False, dash=True)
    for i in range(4):
        x = 12 + 21 * i; on = both or i % 2 == 0
        box(ax, x - 7, base + 2, 14, 14, ('sujet' if both else 'varie') if on else 'fixe', str(i), 'l')
text(ax, 44, 60, r'$G^{\prime}$ : 4 positions', 'fixe', 's') if False else None
save(fig, '48-059')
