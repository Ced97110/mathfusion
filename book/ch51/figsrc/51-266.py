import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role, label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(80)
box(ax, 24, 66, 40, 11, 'sujet', r'$(1+j)(1+i)$', 'm')
arrow(ax, (44, 65), (44, 58), 'varie')
text(ax, 62, 61.5, 'distributivité', 'varie', 's', ha='left')
prods = [r'$1\cdot1$', r'$1\cdot i$', r'$j\cdot1$', r'$j\cdot i$']
vals = [r'$1$', r'$i$', r'$j$', r'$-k$']
xs = [12, 33, 54, 75]
for k, x in enumerate(xs):
    role = 'varie' if k == 3 else 'fixe'
    box(ax, x - 9, 44, 18, 11, role, prods[k], 's')
    arrow(ax, (x, 43), (x, 34), role)
    box(ax, x - 7, 22, 14, 11, role, vals[k], 'm')
brace(ax, 5, 82, 20, 'resultat', None, True, 's', 2)
box(ax, 22, 5, 44, 11, 'resultat', r'$1+i+j-k$', 'l')
save(fig, '51-266')
