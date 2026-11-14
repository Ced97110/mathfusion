import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b, _d = box, disc
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
def disc(ax, x, y, r, role='fixe', label=None, size='m', **k): return _d(ax, x, y, r, role, label=label, size=size, **k)
fig, ax = canvas(70)
text(ax, 44, 65, r'$g\,k\,g^{-1}$ avec $g = 3$, $k = 8$', 'encre')
xs = [2, 24, 46, 68]; w_ = 18
top = [('3', 'fixe'), ('8', 'sujet'), ('−3', 'fixe')]
bot = [('3', 'fixe'), ('0', 'sujet'), ('−3', 'fixe')]
for i in range(3):
    box(ax, xs[i], 40, w_, 12, top[i][1], top[i][0], 'l')
    box(ax, xs[i], 12, w_, 12, bot[i][1], bot[i][0], 'l')
    arrow(ax, (xs[i] + w_ / 2, 40), (xs[i] + w_ / 2, 24), 'varie')
box(ax, xs[3], 40, w_, 12, 'resultat', '= 8', 'l'); box(ax, xs[3], 12, w_, 12, 'resultat', '= 0', 'l')
text(ax, 44, 31.5, r'$f$', 'varie', 's', ha='left') if False else None
text(ax, 11, 57, r'dans $G$', 'fixe', 's', ha='left'); text(ax, 11, 6, r'dans $G^{\prime}$', 'fixe', 's', ha='left')
text(ax, 77, 57, 'dans le noyau', 'resultat', 's'); text(ax, 77, 6, 'neutre', 'resultat', 's')
text(ax, 20, 32, r'$f$', 'varie')
save(fig, '48-052')
