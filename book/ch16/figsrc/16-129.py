import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role="fixe", label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(62)
text(ax, 22, 57, r'$x$ + 3 = 7', 'sujet', 'l')
box(ax, 2, 38, 40, 10, 'limite', r'$x$ = 5 : 8 = 7')
box(ax, 2, 24, 40, 10, 'resultat', r'$x$ = 4 : 7 = 7')
text(ax, 22, 14, 'au moins une valeur vraie', 'resultat', 's')
text(ax, 66, 57, '−19 = −18', 'sujet', 'l')
for i in range(3):
    box(ax, 46, 44 - i * 12, 40, 9, 'limite', r'valeur de $y$ : faux', 's')
text(ax, 66, 14, 'aucune valeur vraie', 'limite', 's')
save(fig, '16-129')
