import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role="fixe", label=None, size="m", **k): return _box(ax, x, y, w, h, role, True, label, size, **k)
fig, ax = canvas(60)
box(ax, 3, 24, 50, 18, 'sujet', r'$(1+\tan^2\theta)(1-\sin^2\theta)$', 'm')
text(ax, 28, 46, 'gauche : le plus compliqué', 'sujet', 's')
text(ax, 28, 19.5, '2 parenthèses, tan et sin', 'sujet', 's')
text(ax, 61, 33, '=', 'encre', 'l')
box(ax, 68, 26, 16, 14, 'fixe', r'$1$', 'l')
text(ax, 76, 46, 'droite', 'fixe', 's')
text(ax, 76, 21, 'un seul nombre', 'fixe', 's')
arrow(ax, (28, 12), (28, 22.5), 'varie')
text(ax, 28, 7, 'on part de ce membre', 'varie', 's')
save(fig, '31-115')
