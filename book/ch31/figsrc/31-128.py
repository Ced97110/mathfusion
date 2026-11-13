import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role="fixe", label=None, size="m", **k): return _box(ax, x, y, w, h, role, True, label, size, **k)
fig, ax = canvas(66)
text(ax, 44, 61, 'multiplier haut et bas', 'fixe', 's')
box(ax, 4, 42, 14, 12, 'sujet', r'$\frac{1}{2}$', 'm'); text(ax, 26, 48, r'$\times$', 'encre', 'l')
box(ax, 32, 42, 22, 12, 'varie', r'$\frac{2}{2} = 1$', 'm'); text(ax, 62, 48, '=', 'encre', 'l')
box(ax, 68, 42, 16, 12, 'resultat', r'$\frac{2}{4}$', 'm')
box(ax, 3, 22, 30, 14, 'sujet', r'$\frac{\cos x}{1-\sin x}$', 'm'); text(ax, 38, 29, r'$\times$', 'encre', 'l')
box(ax, 43, 22, 42, 14, 'varie', r'$\frac{1+\sin x}{1+\sin x} = 1$', 'm')
box(ax, 4, 3, 80, 12, 'limite', r'interdit si $1+\sin x = 0$ (270°)', 's')
save(fig, '31-128')
