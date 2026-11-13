import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role, label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(50)
xs = [4.5, 26.5, 48.5, 70.5]
labs = [r'$a$', r'$1\cdot a$', r'$0\cdot a$', r'$0$']
roles = ['sujet', 'fixe', 'varie', 'resultat']
for x, l, r in zip(xs, labs, roles): box(ax, x, 22, 13, 11, r, l, 'm')
why = ['M2', r'$1=0$', r'$0\cdot a=0$']
for k in range(3):
    arrow(ax, (xs[k] + 14, 27.5), (xs[k + 1] - 1, 27.5), 'varie' if k == 1 else 'fixe', lw=1.4 if k == 1 else 1.0)
    text(ax, xs[k] + 18, 17, why[k], 'varie' if k == 1 else 'fixe', 's')
text(ax, 11, 40, 'départ', 'sujet', 's'); text(ax, 77, 40, 'arrivée', 'resultat', 's')
text(ax, 44, 40, 'étape clé', 'varie', 's')
arrow(ax, (44, 38), (44, 36), 'varie')
text(ax, 44, 7, r'$a=1\cdot a=0\cdot a=0$', 'resultat', 'l')
save(fig, '51-270')
