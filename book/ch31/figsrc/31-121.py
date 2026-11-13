import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role="fixe", label=None, size="m", **k): return _box(ax, x, y, w, h, role, True, label, size, **k)
fig, ax = canvas(68)
text(ax, 44, 63, r'$\theta = 35^\circ$', 'encre', 'm')
box(ax, 4, 44, 32, 12, 'sujet', r'$1+\tan^2\theta$', 'm'); text(ax, 44, 50, r'$\times$', 'encre', 'l')
box(ax, 52, 44, 32, 12, 'autre', r'$1-\sin^2\theta$', 'm')
text(ax, 20, 39, r'$=\sec^2\theta$', 'sujet', 's'); text(ax, 68, 39, r'$=\cos^2\theta$', 'autre', 's')
box(ax, 4, 22, 32, 10, 'sujet', '1,4903', 'm'); text(ax, 44, 27, r'$\times$', 'encre', 'l')
box(ax, 52, 22, 32, 10, 'autre', '0,6710', 'm')
arrow(ax, (44, 20), (44, 13), 'varie')
box(ax, 32, 2, 24, 10, 'resultat', r'$= 1$', 'm')
save(fig, '31-121')
