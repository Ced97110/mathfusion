import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(86)
text(ax, 20, 82, r'dans $G$', 'sujet'); text(ax, 68, 82, r'dans $G^{\prime}$', 'autre')
rows = [(58, r'$g\,k\,g^{-1}$', r"$f(g)\,1'\,f(g)^{-1}$", 's'), (34, '3 + 8 − 3', '3 + 0 − 3', 'm'), (10, '= 8', r"$= 1' = 0$", 'l')]
for y, a, b, sz in rows:
    box(ax, 2, y, 36, 14, 'sujet', a, sz); box(ax, 50, y, 36, 14, 'autre', b, sz)
    arrow(ax, (38, y + 7), (50, y + 7), 'varie'); text(ax, 44, y + 11, r'$f$', 'varie')
for y in (58, 34):
    arrow(ax, (20, y), (20, y - 10), 'fixe'); arrow(ax, (68, y), (68, y - 10), 'fixe')
save(fig, '48-054')
