import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role="fixe", label=None, size="m", **k): return _box(ax, x, y, w, h, role, True, label, size, **k)
fig, ax = canvas(70)
text(ax, 44, 65, r'$x = 30^\circ$', 'encre', 'm')
box(ax, 3, 44, 34, 15, 'sujet', r'$\frac{\cos x}{1-\sin x}$', 'm'); text(ax, 44, 51.5, '=', 'encre', 'l')
box(ax, 51, 44, 34, 15, 'autre', r'$\frac{1+\sin x}{\cos x}$', 'm')
text(ax, 20, 38, r'$\frac{0{,}8660}{0{,}5}$', 'sujet', 's'); text(ax, 68, 38, r'$\frac{1{,}5}{0{,}8660}$', 'autre', 's')
arrow(ax, (20, 33), (36, 25), 'varie'); arrow(ax, (68, 33), (52, 25), 'varie')
box(ax, 30, 16, 28, 9, 'resultat', r'$\approx 1{,}732$', 'm')
box(ax, 3, 2, 22, 8, 'resultat', r'$30^\circ$ vérifié', 's')
box(ax, 30, 2, 55, 8, 'fixe', 'autres angles : non vérifiés', 's', dash=True)
save(fig, '31-124')
