import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _box(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(80)
text(ax, 15, 73, 'terme', 'fixe', 's'); text(ax, 45, 73, 'facteur commun', 'sujet', 's'); text(ax, 74, 73, 'reste', 'varie', 's')
rows = [(r'$9x^3$', r'$9x$', r'$x^2$'), (r'$18x^2$', r'$9x$', r'$2x$'), (r'$27x$', r'$9x$', r'$3$')]
for k, (t, f, r) in enumerate(rows):
    y = 57 - k * 12
    box(ax, 3, y, 24, 9, 'fixe', t); text(ax, 30, y + 4.5, '=', 'encre', 'm')
    box(ax, 34, y, 22, 9, 'sujet', f); text(ax, 59, y + 4.5, r'$\times$', 'encre', 'm')
    box(ax, 62, y, 22, 9, 'varie', r)
arrow(ax, (45, 33), (28, 22), 'sujet'); arrow(ax, (73, 33), (58, 22), 'varie')
box(ax, 14, 11, 18, 10, 'sujet', r'$9x$', 'l'); box(ax, 36, 11, 48, 10, 'varie', r'$(x^2 + 2x + 3)$', 'l')
text(ax, 44, 4, 'une seule fois, devant la parenthèse', 'fixe', 's')
save(fig, '18-035')
