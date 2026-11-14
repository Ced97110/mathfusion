import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role, label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(64)
rows = [(r'$i\times(-i)=1$', 'resultat', r'$-i$ : entier de Gauss'),
        (r'$2\times\frac{1}{2}=1$', 'limite', r'$\frac{1}{2}$ : pas entier'),
        (r'$(1+i)\times\frac{1-i}{2}=1$', 'limite', r'$\frac{1-i}{2}$ : pas entier')]
for k, (l, role, r) in enumerate(rows):
    y = 44 - k * 20
    box(ax, 2, y, 40, 14, 'sujet', l, 's')
    arrow(ax, (43.5, y + 7), (50.5, y + 7), role)
    box(ax, 52, y, 34, 14, role, r, 's')
text(ax, 44, 61, 'l’inverse est-il un entier de Gauss ?', 'encre', 's')
save(fig, '51-262')
