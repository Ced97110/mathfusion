import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role="fixe", label=None, size="m", **k): return _box(ax, x, y, w, h, role, True, label, size, **k)
fig, ax = canvas(84)
box(ax, 12, 62, 40, 14, 'sujet', r'$\sec^2 x \times \cos^2 x$', 'm')
text(ax, 70, 69, r'$\sec$ : un rapport', 'varie', 's')
arrow(ax, (32, 61), (32, 50), 'varie')
text(ax, 62, 55.5, r'$\sec x = \frac{1}{\cos x}$', 'varie', 's')
box(ax, 12, 30, 40, 18, 'sujet', r'$\frac{1}{\cos^2 x} \times \cos^2 x$', 'm')
text(ax, 70, 39, r'sinus et cosinus', 'fixe', 's')
arrow(ax, (32, 29), (32, 18), 'varie')
text(ax, 62, 23.5, r'$\cos^2 x$ haut et bas', 'varie', 's')
box(ax, 22, 3, 20, 13, 'resultat', r'$1$', 'l')
save(fig, '31-118')
