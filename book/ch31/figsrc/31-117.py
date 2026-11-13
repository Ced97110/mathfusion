import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role="fixe", label=None, size="m", **k): return _box(ax, x, y, w, h, role, True, label, size, **k)
fig, ax = canvas(86)
rows = [(r'$1-\sin^2 x$', r'$\cos^2 x$'), (r'$1-\cos^2 x$', r'$\sin^2 x$'),
        (r'$1+\tan^2 x$', r'$\sec^2 x$'), (r'$1+\cot^2 x$', r'$\mathrm{cosec}^2 x$')]
text(ax, 20, 80, 'morceau reconnu', 'sujet', 's'); text(ax, 68, 80, 'devient', 'resultat', 's')
for i, (a, b) in enumerate(rows):
    y = 60 - i * 14
    box(ax, 3, y, 34, 10, 'sujet', a, 'm'); box(ax, 52, y, 33, 10, 'resultat', b, 'm')
    arrow(ax, (38, y + 5), (51, y + 5), 'varie')
y = 4
box(ax, 3, y, 34, 10, 'sujet', r'$1$', 'm'); box(ax, 46, y, 39, 10, 'resultat', r'$\sin^2 x + \cos^2 x$', 'm')
arrow(ax, (38, y + 5), (45, y + 5), 'varie')
save(fig, '31-117')
