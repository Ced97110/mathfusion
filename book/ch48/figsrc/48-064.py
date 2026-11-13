import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b, _d = box, disc
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
def disc(ax, x, y, r, role='fixe', label=None, size='m', **k): return _d(ax, x, y, r, role, label=label, size=size, **k)
fig, ax = canvas(78)
text(ax, 4, 73, r'$H = \{0 ; 1\}$ dans $\mathbb{Z}$', 'sujet', ha='left')
for k in range(3):
    disc(ax, 12 + 16 * k, 56, 5, ['sujet', 'sujet', 'limite'][k], str(k), 'l')
    if k < 2:
        disc(ax, 12 + 16 * k, 22, 5, 'resultat', str(k), 'l'); arrow(ax, (12 + 16 * k, 50.5), (12 + 16 * k, 27.5), 'varie')
disc(ax, 44, 22, 5, 'limite', '2', 'l')
arrow(ax, (14, 62), (26, 62), 'limite', curve=-0.7)
arrow(ax, (14, 28), (26, 28), 'limite', curve=-0.7)
text(ax, 62, 56, '1 + 1 = 2', 'limite', ha='left'); text(ax, 62, 22, '1 + 1 = 2', 'limite', ha='left')
text(ax, 4, 40, r'$f$', 'varie', ha='left')
text(ax, 4, 8, r'$f(H)$ : 2 est hors de $f(H)$', 'limite', 's', ha='left')
save(fig, '48-064')
