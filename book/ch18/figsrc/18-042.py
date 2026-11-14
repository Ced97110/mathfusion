import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _box(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(72)
xs = [3, 24, 45, 66]
for x, t, r in zip(xs, [r'$x^3$', r'$3x^2$', r'$-6x$', r'$-17$'], ['sujet', 'sujet', 'limite', 'limite']): box(ax, x, 56, 18, 9, r, t)
arrow(ax, (22, 54), (21, 40), 'varie'); arrow(ax, (66, 54), (67, 40), 'varie')
box(ax, 3, 30, 38, 10, 'sujet', r'$x^2\,(x+3)$'); box(ax, 49, 30, 36, 10, 'limite', r'$-1\,(6x+17)$')
text(ax, 45, 35, r'$\neq$', 'limite', 'l', weight='bold')
text(ax, 44, 20, r'$x+3$ et $6x+17$ : deux blocs', 'limite', 's')
text(ax, 44, 13, 'pas de bloc commun', 'limite', 's')
text(ax, 44, 5, r'on a changé $18$ en $17$', 'fixe', 's')
save(fig, '18-042')
