import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role="fixe", label=None, size="m", **k): return _box(ax, x, y, w, h, role, True, label, size, **k)
fig, ax = canvas(88)
box(ax, 4, 66, 40, 16, 'sujet', r'$\frac{\cos x + \sin x}{\cos x}$', 'm')
arrow(ax, (24, 65), (24, 54), 'varie'); text(ax, 36, 59.5, 'séparer', 'varie', 's')
box(ax, 4, 36, 40, 16, 'fixe', r'$\frac{\cos x}{\cos x} + \frac{\sin x}{\cos x}$', 'm')
arrow(ax, (24, 35), (24, 24), 'varie')
box(ax, 4, 8, 40, 14, 'resultat', r'$1 + \tan x$', 'm')
box(ax, 52, 56, 32, 14, 'sujet', r'$\frac{1}{2} + \frac{1}{3}$', 'm')
arrow(ax, (68, 55), (68, 44), 'varie'); text(ax, 76, 49.5, 'réunir', 'varie', 's')
box(ax, 52, 28, 32, 14, 'resultat', r'$\frac{5}{6}$', 'm')
save(fig, '31-120')
