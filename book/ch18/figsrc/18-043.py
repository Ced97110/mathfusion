import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _box(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(76)
text(ax, 44, 71, 'deux groupes, un même bloc', 'fixe', 's')
box(ax, 3, 55, 12, 9, 'varie', r'$x^2$'); box(ax, 16, 55, 24, 9, 'sujet', r'$(x+3)$')
text(ax, 44, 59.5, '+', 'encre', 'l')
box(ax, 48, 55, 12, 9, 'varie', r'$-6$'); box(ax, 61, 55, 24, 9, 'sujet', r'$(x+3)$')
arrow(ax, (28, 54), (28, 38), 'sujet'); arrow(ax, (73, 54), (40, 38), 'sujet', curve=0.0)
arrow(ax, (9, 54), (50, 38), 'varie'); arrow(ax, (54, 54), (62, 38), 'varie')
box(ax, 16, 28, 24, 9, 'sujet', r'$(x+3)$'); box(ax, 50, 28, 35, 9, 'varie', r'$(x^2-6)$')
text(ax, 44, 17, r'$x=2$ : $5 \times (-2) = -10$', 'resultat', 's')
text(ax, 44, 9, 'le bloc est retiré une fois', 'sujet', 's')
save(fig, '18-043')
