import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role, label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(88)
ys = [72, 52, 32, 12]
labs = [r'$5$', r'$1\times5$', r'$0\times5$', r'$0$']
roles = ['sujet', 'fixe', 'varie', 'resultat']
for y, l, r in zip(ys, labs, roles): box(ax, 6, y, 24, 11, r, l, 'l')
reasons = ['règle M2 : 1 × a = a', 'on suppose que 1 = 0', 'un produit par 0 vaut 0']
for k, s in enumerate(reasons):
    arrow(ax, (18, ys[k] - 1), (18, ys[k + 1] + 12), 'varie')
    text(ax, 36, ys[k] - 4.5, s, 'varie', 's', ha='left')
text(ax, 36, 17.5, 'tout élément vaut 0', 'resultat', 'm', ha='left')
text(ax, 36, 77.5, 'un élément quelconque', 'sujet', 's', ha='left')
save(fig, '51-269')
