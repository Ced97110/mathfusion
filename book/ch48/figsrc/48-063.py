import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b, _d = box, disc
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
def disc(ax, x, y, r, role='fixe', label=None, size='m', **k): return _d(ax, x, y, r, role, label=label, size=size, **k)
fig, ax = canvas(84)
text(ax, 4, 80, r'$f^{-1}(H^{\prime})$ : entiers pairs', 'sujet', ha='left')
for n in range(6):
    x = 8 + 14 * n
    disc(ax, x, 66, 5, 'sujet' if n % 2 == 0 else 'fixe', str(n), 'l')
Q = {k: 14 + 20 * k for k in range(4)}
for k, x in Q.items(): disc(ax, x, 26, 5, 'resultat' if k % 2 == 0 else 'fixe', str(k), 'l')
for n in range(6):
    x = 8 + 14 * n; q = Q[n % 4]
    d = math.hypot(q - x, 40); ux, uy = (q - x) / d, -40 / d
    arrow(ax, (x + 5.5 * ux, 66 + 5.5 * uy), (q - 5.5 * ux, 26 - 5.5 * uy), 'sujet' if n % 2 == 0 else 'fixe', lw=0.8)
text(ax, 44, 16, r'$f(n)$ = reste de $n$ par 4', 'varie', 's')
text(ax, 4, 6, r'$H^{\prime} = \{0, 2\}$', 'resultat', 's', ha='left')
text(ax, 84, 6, r'$f^{-1}(H^{\prime})$ sous-groupe de $G$', 'sujet', 's', ha='right', weight='bold')
save(fig, '48-063')
