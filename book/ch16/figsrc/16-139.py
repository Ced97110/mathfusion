import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role="fixe", label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(54)
box(ax, 11, 34, 66, 11, 'resultat', 'cette année : 44 €', 'm')
box(ax, 11, 18, 61.5, 11, 'sujet', "l'an dernier : 41", 'm'); box(ax, 72.5, 18, 4.5, 11, 'varie', '3', 's')
text(ax, 77, 14, '+ 3 de plus', 'varie', 's', ha='right')
box(ax, 19, 1, 50, 9, 'resultat', '41 + 3 = 44 : vrai', 'm')
save(fig, '16-139')
