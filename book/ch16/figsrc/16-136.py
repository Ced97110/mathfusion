import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role="fixe", label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(58)
text(ax, 25, 53, '$x$', 'sujet', 'm'); text(ax, 63, 53, '$x$ + 2', 'sujet', 'm')
box(ax, 8, 34, 34, 13, 'sujet', '215', 'l'); box(ax, 46, 34, 34, 13, 'sujet', '217', 'l')
brace(ax, 8, 80, 32, 'resultat', 'somme 432')
for x in (8, 46):
    box(ax, x, 3, 34, 11, 'limite', 'impair, pas pair', 's')
    arrow(ax, (x + 17, 33 - 12), (x + 17, 15), 'limite') if False else None
save(fig, '16-136')
