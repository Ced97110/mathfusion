import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def row(ax, x0, y, n, roles, labels=None, st=5.6, w=5.0, h=5.0):
    for k in range(1, n + 1):
        r = roles.get(k)
        box(ax, x0 + (k - 1) * st, y, w, h, r or "fixe", fill=r is not None, dash=r is None,
            label=(labels or {}).get(k), size="s", r=0.6)

fig, ax = canvas(66)
text(ax, 2, 61, r'$\varphi(p) = p - 1$', 'resultat', 'l', ha='left')
y = 42
for p in (5, 7, 11):
    text(ax, 2, y + 9, f'$p$ = {p} : {p - 1} nombres = {p} − 1', 'encre', 'm', ha='left')
    row(ax, 4, y, p, {k: 'resultat' for k in range(1, p)}, st=6.5, w=5.6)
    y -= 16
text(ax, 2, 2.5, 'gris : $p$ lui-même, non compté', 'fixe', 's', ha='left')
save(fig, '46-136')
